import csv
import re

from collections import Counter
from io import StringIO


#
# load the data file and parse into a few useful constructs
#

def read_file(name='SampleCSVFile.csv'):
    with open(name, 'r', encoding='utf-8') as fin:
        contents = fin.read()
        print('file size:', len(contents))
        lines = [line.strip() for line in contents.split('\n') if len(line) > 0]
        print('lines in file:', len(lines))
        print('count of commas in rows:', Counter([len(re.findall(',', line)) for line in lines]))
        fin.seek(0)
        reader = csv.reader(iter(fin.readline, ''), delimiter=',')
        items = [
            [
                int(row[0]),
                row[1],
                row[2],
                float(row[3]),
                float(row[4]),
                float(row[5]),
                float(row[6]),
                row[7],
                row[8],
                float(row[9]) if row[9] else None,
            ]
            for row in reader
        ]
    return contents, lines, items

contents, lines, items = read_file()
by_id = {r[0]:r for r in items}
regions = set([by_id[k][7].lower() for k in by_id.keys()])
print('regions:', regions)
categories = set([by_id[k][8].lower() for k in by_id.keys()])
print('categories:', categories)

print('sample data:')
for k in range(1, 26):
    print(k, '->', by_id[k])

#
# expressions
#

table_regex = re.compile('.*table.*', re.IGNORECASE)
tables = [item[0] for item in items if table_regex.match(item[1])]
print('table IDs:', tables)
print('but wait... item 1148:', by_id[1148][:2])

table_regex = re.compile('.*\\btable\\b.*', re.IGNORECASE)
tables = [item[0] for item in items if table_regex.match(item[1])]
print('table IDs better:', tables)

chair_regex = re.compile('.*\\bchair\\b.*', re.IGNORECASE)
chairs = [item[0] for item in items if chair_regex.match(item[1])]
print('chair IDs:', chairs)

lesro_tables_regex = re.compile('.*\\blesro\\b.*\\btable\\b.*', re.IGNORECASE)
lesro_tables = [item[0] for item in items if lesro_tables_regex.match(item[1])]
print('lesro table IDs:', lesro_tables)

print('lesro table names:')
for k in lesro_tables:
    print(by_id[k][:2])

print('now we want all the kinds of tables from each lesro table entry')
lesro_table_kinds_regex = re.compile('(lesro\\b.*[^,]) (\\w+(?: table, \\w+)*) table', re.IGNORECASE)
for item in items:
    match = lesro_table_kinds_regex.match(item[1])
    if match:
        print(match.group(1), match.group(2).split(' Table, '))
