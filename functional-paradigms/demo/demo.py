import sys

import parser


def main(filename):
    file_to_rows = parser.FileToRows(filename)
    print(file_to_rows.filename())
    print(file_to_rows.extensions())
    for row in file_to_rows:
        print(row)


if __name__ == '__main__':
    main(sys.argv[1])
