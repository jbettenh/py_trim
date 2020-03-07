#! python 3
# This script will rename files into a defined format.

import argparse
from datetime import datetime
import fnmatch
import os
import re
from pathlib import Path


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

    if args.rs:
        new_file = os.path.join(args.path, 'thisisatestfile.txt')
    elif args.su:
        new_file = os.path.join(args.path, 'this_is_a_test_file.txt')
    elif args.sm:
        new_file = os.path.join(args.path, 'this-is-a-test-file.txt')

    os.rename(old_file, new_file)

    if args.l:
        full_file = os.path.basename(new_file).lower()
        file_case = os.path.join(args.path, full_file)
    elif args.u:
        full_file = os.path.basename(new_file).upper()
        file_case = os.path.join(args.path, full_file)
    elif args.c:
        full_file = os.path.basename(new_file).lower()
        file_case = os.path.join(args.path, full_file)
    # make CamelCase

    os.rename(new_file, file_case)


def main():
    args = arguments()

    for filename in os.listdir(args.path):
        if fnmatch.fnmatch(filename, '* *'):
            print(filename)
            filename = filename.replace(" ", "")
            print(filename)

    # pathlib
   # current_dir = Path(args.path)
    #for path in current_dir.iterdir():
     #   info = path.stat()
      #  print(f'{path.name}\t Last Modified: {convert_date(info.st_mtime)}')

if __name__ == '__main__':
    main()


