import csv
import functools

from io import BytesIO
from tarfile import open as tar_open
from zipfile import ZipFile


def file_to_rows(filename):
    with open(filename, 'rb') as fin:
        yield from _execute_pipeline(_build_pipeline(filename), fin)


def _build_pipeline(filename):
    return (
        stage
        for extension in _extensions_from_filename(filename)[::-1]
        for stage in _STAGES_BY_EXTENSION[extension]
    )


def _extensions_from_filename(filename):
    return filename.split('.')[1:]


def _execute_pipeline(pipeline, fin):
    return functools.reduce(lambda content, stage: stage(content), pipeline, fin.read())


def _bytes_tgz_to_bytes(content):
    archive = tar_open(fileobj=BytesIO(content), mode='r:gz')
    return archive.extractfile(archive.getmembers()[0]).read()


def _bytes_zip_to_bytes(content):
    archive = ZipFile(BytesIO(content))
    return archive.read(archive.namelist()[0])


def _bytes_to_text(content):
    return bytes.decode(content, encoding='utf-8')


def _text_to_lines(content):
    return str.splitlines(content)


def _lines_to_filtered_lines(content):
    return (line for line in content if line)


def _lines_csv_to_rows(content):
    return csv.reader(content)


def _lines_psv_to_rows(content):
    return csv.reader(content, delimiter='|')


def _lines_tsv_to_rows(content):
    return csv.reader(content, delimiter='\t')


_BYTES_TO_FILTERED_LINES = (_bytes_to_text, _text_to_lines, _lines_to_filtered_lines)

_STAGES_BY_EXTENSION = dict(
    csv=_BYTES_TO_FILTERED_LINES + (_lines_csv_to_rows,),
    psv=_BYTES_TO_FILTERED_LINES + (_lines_psv_to_rows,),
    tsv=_BYTES_TO_FILTERED_LINES + (_lines_tsv_to_rows,),
    tgz=(_bytes_tgz_to_bytes,),
    zip=(_bytes_zip_to_bytes,),
)

# partial functions doing the same thing as the functions above:
# _bytes_to_text = functools.partial(bytes.decode, encoding='utf-8')
# _text_to_lines = str.splitlines
# _lines_to_filtered_lines = functools.partial(filter, None)
# _lines_csv_to_rows = csv.reader
# _lines_psv_to_rows = functools.partial(csv.reader, delimiter='|')
# _lines_tsv_to_rows = functools.partial(csv.reader, delimiter='\t')
