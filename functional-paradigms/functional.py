import csv
import sys

from io import BytesIO
from tarfile import open as tar_open
from zipfile import ZipFile


def rows(filename):
    with open(filename, 'rb') as fin:
        content = fin.read()
        for function in _build_pipeline(filename):
            content = function(content)
        yield from content


def _extensions(filename):
    return filename.split('.')[1:]


def _build_pipeline(filename):
    return (
        stage
        for extension in _extensions(filename)[::-1]
        for stage in _STAGES_BY_EXTENSION[extension]
    )


def _raw_tgz_to_raw(zipped):
    archive = tar_open(fileobj=BytesIO(zipped), mode='r:gz')
    return archive.extractfile(archive.getmembers()[0]).read()


def _raw_zip_to_raw(zipped):
    archive = ZipFile(BytesIO(zipped))
    with open(archive.namelist()[0], 'rb') as fin:
        return fin.read()


def _raw_to_text(raw):
    return raw.decode('utf-8')


_text_to_rows = str.splitlines


def _rows_to_filtered_rows(rows):
    return filter(lambda x: x, rows)


def _rows_csv_to_values(rows):
    return csv.reader(rows)


def _rows_tsv_to_values(rows):
    return csv.reader(rows, delimiter='\t')


_RAW_TO_FILTERED_ROWS = (_raw_to_text, _text_to_rows, _rows_to_filtered_rows)

_STAGES_BY_EXTENSION = dict(
    csv=_RAW_TO_FILTERED_ROWS + (_rows_csv_to_values,),
    tsv=_RAW_TO_FILTERED_ROWS + (_rows_tsv_to_values,),
    tgz=(_raw_tgz_to_raw,),
    zip=(_raw_zip_to_raw,),
)


def main(filename):
    print(filename)
    print(_extensions(filename))
    for row in rows(filename):
        print(row)


if __name__ == '__main__':
    main(sys.argv[1])
