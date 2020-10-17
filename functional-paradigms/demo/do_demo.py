import sys

import parse_csv


def main(filename):
    file_to_rows = parse_csv.FileToRows(filename)
    print(file_to_rows.filename())
    print(file_to_rows.extensions())
    for row in file_to_rows:
        print(row)


if __name__ == '__main__':
    main(sys.argv[1])
