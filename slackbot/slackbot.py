import asyncio
import hmac
import logging
import os
import time

from aiohttp import web
from aiohttp import ClientSession


log = logging.getLogger(__name__)


#
# config
#

SLACK_SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET')


#
# bot implementation
#

class Slackbot:

    app = web.Application()

    def __init__(self):
        routes = [
            web.get('/healthz', self.healthz),
            web.post('/slack', self.slack),
        ]
        self.app.add_routes(routes)

    async def run(self):
        log.info('starting slackbot')
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8000)
        self.client = ClientSession()
        try:
            await site.start()
            while True:
                await asyncio.sleep(600)
        except asyncio.CancelledError:
            log.info('received cancellation signal')
            await site.stop()
        except Exception as e:
            log.exception('unhandled exception: %s', e)
        finally:
            await self.client.close()
        log.info('stopped slackbot')

    async def healthz(self, request):
        log.info('health check')
        response = dict(success=True, timestamp=time.time())
        return web.json_response(response)

    async def slack(self, request):
        log.info('slack')
        try:
            await self.validate_slack_message(request)
            asyncio.get_event_loop().create_task(self.send_response(request))
            return web.Response()
        except Exception as e:
            log.exception(e)
            raise web.HTTPUnauthorized()

    async def validate_slack_message(self, request):
        log.debug('validating')
        headers = request.headers
        body = await request.text()
        timestamp = headers.get('X-Slack-Request-Timestamp')
        log.debug('timestamp: %s', timestamp)
        if not timestamp or abs(time.time() - int(timestamp)) > 60:
            log.error('message is too old')
            raise AssertionError('invalid timestamp')
        digest = await self.compute_slack_digest(timestamp, body)
        expected = headers.get('X-SLACK-SIGNATURE')
        if not hmac.compare_digest(digest, expected):
            log.debug('hash mismatch: %s %s', digest, expected)
            raise AssertionError('slack validation failed')

    async def compute_slack_digest(self, timestamp, body):
        document = f'v0:{timestamp}:{body}'.encode()
        log.debug('document: %s', document)
        digest = hmac.new(SLACK_SIGNING_SECRET.encode(), document, 'sha256').hexdigest()
        log.debug('digest: %s', digest)
        return f'v0={digest}'

    async def send_response(self, request):
        try:
            log.debug('reversing a string seems hard...')
            data = await request.post()
            log.debug('data: %s', data)
            for i in range(5):
                log.debug('thinking...')
                await asyncio.sleep(1)
            message = data.get('text')
            reply = message[::-1]
            log.info('sending reply: %s', reply)
            async with self.client.post(data.get('response_url'), json=dict(text=reply)):
                log.debug('successfully sent reply')
        except Exception as e:
            log.exception(e)


#
# main loop
#

def main():
    log.info('startup')
    event_loop = asyncio.get_event_loop()
    event_loop.set_debug(True)
    bot = Slackbot()
    task = asyncio.Task(bot.run(), loop=event_loop)
    try:
        event_loop.run_until_complete(task)
    except KeyboardInterrupt:
        log.info('stopping...')
        cancel(event_loop, task)
    event_loop.close()
    log.info('shutdown')


#
# keyboard interrupt handling
#

def cancel(event_loop, task):
    task.cancel()
    while asyncio.all_tasks(event_loop):
        log.debug('awaiting in-process task completion')
        event_loop.run_until_complete(asyncio.sleep(1))
    try:
        task.exception()
    except asyncio.CancelledError:
        log.debug('consumed cancellation exception')
    log.info('all tasks stopped')


#
# entrypoint
#

if __name__ == '__main__':
    rootLogger = logging.getLogger()
    rootLogger.addHandler(logging.StreamHandler())
    rootLogger.setLevel(getattr(logging, os.environ.get('LOG_LEVEL', 'debug').upper()))
    logging.getLogger('asyncio').setLevel(logging.WARNING)
    log.debug('debug log')
    main()
