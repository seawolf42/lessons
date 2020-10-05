import io

from tarfile import open as tar_open
from zipfile import ZipFile


default_data = tuple((chr(i), i, hex(i), oct(i)) for i in range(ord('a'), ord('a') + 6))

# default_data = (
#   ('a', 97, 0x61, 0o141),
#   ('b', 98, 0x62, 0o142),
#   ('c', 99, 0x63, 0o143),
#   ...
# )

def create(data=default_data):
    for extension, data_to_rows in (('csv', stringified_to_csv_rows), ('tsv', stringified_to_tsv_rows)):
        filename = f'abc.{extension}'
        blob = content_to_blob(rows_to_content(data_to_rows(stringified(data))))
        for writer in (raw_writer, zip_writer, tgz_writer):
            writer(filename, blob)

def stringified(data):
    return ((str(field) for field in row) for row in data)

def stringified_to_csv_rows(data):
    return (','.join(row) for row in data)

def stringified_to_tsv_rows(data):
    return ('\t'.join(row) for row in data)

def rows_to_content(rows):
    return '\n'.join(rows)

def content_to_blob(content):
    return content.encode()

def raw_writer(filename, blob):
    with open(filename, 'wb') as fout:
        fout.write(blob)

def tgz_writer(filename, blob):
    with tar_open(f'{filename}.tgz', 'w:gz') as fout:
        fout.add(filename)

def zip_writer(filename, blob):
    with ZipFile(f'{filename}.zip', 'w') as fout:
        fout.write(filename)
