#! python 3
# This script will rename files into a defined format.
import os
import sys
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def arguments():
    parser = argparse.ArgumentParser(description='Parser')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-rs', action='store_true', help="This removes spaces")
    group.add_argument('-su', action='store_true', help="This changes spaces to underscores")
    group.add_argument('-sm', action='store_true', help="This changes spaces to minuses")

    group_case = parser.add_mutually_exclusive_group()
    group_case.add_argument('-l', action='store_true', help="This makes all letters lower case")
    group_case.add_argument('-u', action='store_true', help="This makes all letters upper case")
    group_case.add_argument('-c', action='store_true', help="This makes the words camel case")

    parser.add_argument('--path', type=dir_path, help="This is the path to the folder")
    args = parser.parse_args()
    print(args)
    oldfile = os.path.join(args.path, "this is a test file.txt")
    newfile = os.path.join(args.path,"this_is_a_test_file.txt")
    os.rename(oldfile, newfile)


if __name__ == "__main__":
    #input command line parameters
        #get path
        #get format
    arguments()

