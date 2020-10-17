import csv

from io import BytesIO
from tarfile import open as tar_open
from zipfile import ZipFile


def file_to_rows(filename):
    with open(filename, 'rb') as fin:
        content = _execute_pipeline(_build_pipeline(filename), fin.read())
        yield from content


def _build_pipeline(filename):
    return (
        stage
        for extension in _extensions(filename)[::-1]
        for stage in _STAGES_BY_EXTENSION[extension]
    )


def _extensions(filename):
    return filename.split('.')[1:]


def _execute_pipeline(pipeline, content):
    for function in pipeline:
        content = function(content)
    return content


def _bytes_tgz_to_bytes(content):
    archive = tar_open(fileobj=BytesIO(content), mode='r:gz')
    return archive.extractfile(archive.getmembers()[0]).read()


def _bytes_zip_to_bytes(content):
    archive = ZipFile(BytesIO(content))
    with open(archive.namelist()[0], 'rb') as fin:
        return fin.read()


def _bytes_to_text(content):
    return content.decode('utf-8')


_text_to_lines = str.splitlines


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

# _execute_pipeline = functools.partial(functools.reduce, lambda c, fn: fn(c))

# _bytes_to_text = functools.partial(bytes.decode, encoding='utf-8')

# _text_to_lines = str.splitlines

# _lines_to_filtered_lines = functools.partial(filter, lambda x: x)

# _lines_csv_to_rows = csv.reader
# _lines_psv_to_rows = functools.partial(csv.reader, delimiter='|')
# _lines_tsv_to_rows = functools.partial(csv.reader, delimiter='\t')
