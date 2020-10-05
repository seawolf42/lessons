import csv

from io import BytesIO
from zipfile import ZipFile


class FileToRows():

    def __init__(self, filename):
        self._filename = filename
        parts = filename.split('.')
        self._name, self._extensions = parts[0], parts[1:]

    def __repr__(self):
        return f"FileToRows(filename='{self._filename}')"

    def filename(self):
        return self._filename

    def extensions(self):
        return self._extensions

    def rows(self):
        return list(self)

    def __iter__(self):
        with open(self._filename, 'rb') as fin:
            content = fin.read()
            if self._extensions[-1] == 'zip':
                content = self._zip_to_binary(content)
            content = content.decode('utf-8')
            for row in self._text_to_rows(content):
                yield row

    def _text_to_rows(self, content):
        return csv.reader(line for line in content.split() if line)

    def _zip_to_binary(self, content):
        archive = ZipFile(BytesIO(content))
        file = archive.namelist()[0]
        with open(file, 'rb') as fin:
            return fin.read()
