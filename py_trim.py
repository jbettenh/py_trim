#! python 3
# This script will rename files into a defined format.

import argparse
from datetime import datetime
import fnmatch
import os



def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date


def arguments():
    parser = argparse.ArgumentParser(description='Parser')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-rs', action='store_true', help='This removes spaces')
    group.add_argument('-su', action='store_true', help='This changes spaces to underscores')
    group.add_argument('-sm', action='store_true', help='This changes spaces to minuses')

    group_case = parser.add_mutually_exclusive_group()
    group_case.add_argument('-l', action='store_true', help='This makes all letters lower case')
    group_case.add_argument('-u', action='store_true', help='This makes all letters upper case')
    group_case.add_argument('-c', action='store_true', help='This makes the words camel case')

    parser.add_argument('--path', type=dir_path, help='This is the path to the folder')

    return parser.parse_args()


def rename():
    # old_file = os.path.join(args.path, 'this is a test file.txt')
    # old_file = os.path.join(args.path, 'THIS_IS_A_TEST_FILE.TXT')
    os.rename(new_file, file_case)


def main():
    args = arguments()

    for filename in os.listdir(args.path):
        #info = filename.stat()
        #print(f'{filename.name}\t Last Modified: {convert_date(info.st_mtime)}')
        oldfile = os.path.join(args.path, filename)

        # Convert to upper or lower case
        if args.l:
            filename = filename.lower()
        elif args.u:
            filename = filename.upper()
        # elif args.c:  # make CamelCase

        # Change spaces
        if fnmatch.fnmatch(filename, '* *'):
            if args.rs:
                filename = filename.replace(" ", "")
            elif args.su:
                filename = filename.replace(" ", "_")
            elif args.sm:
                filename = filename.replace(" ", "-")

        newfile = os.path.join(args.path, filename)
        os.rename(oldfile, newfile)
        print(filename)

if __name__ == '__main__':
    main()


