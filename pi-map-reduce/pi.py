import logging
import os
import random
import uuid

import mincemeat


log = logging.getLogger()


def get_data(mapsize=10, nummaps=4):
    return {i: mapsize for i in range(1, nummaps + 1)}


def mapfn(key, value):
    print('mapfn: {0}, {1}'.format(key, value))
    import random
    import uuid
    random.seed(uuid.uuid4())
    inside = sum((random.random() ** 2 + random.random() ** 2) <= 1. for i in xrange(value))
    yield 'totals', (inside, value)


def reducefn(key, value):
    print('reducefn: {0}, {1}'.format(key, value))
    inside = 0
    total = 0
    for v in value:
        inside += v[0]
        total += v[1]
    return inside, total


def main():
    server = mincemeat.Server()
    data = get_data(mapsize=10000000, nummaps=1000)
    log.info('data: %s', data)
    log.info('waiting for workers...')
    server.datasource = data
    server.mapfn = mapfn
    server.reducefn = reducefn
    results = server.run_server(password='pass')
    inside, total = results['totals']
    print(results, inside, total)
    print('{0}: {1} inside, {2} total, pi ~= {3}'.format('totals', inside, total, 4. * inside / total))


if __name__ == '__main__':
    log.addHandler(logging.StreamHandler())
    log.setLevel(logging.DEBUG)
    main()
