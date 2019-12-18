#! python 3
# This script will rename files into a defined format.
import os
import sys
import argparse




def arguments():
    parser = argparse.ArgumentParser(description='A tutorial of argparse!')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-rs', action='store_true', help="This removes spaces")
    group.add_argument('-su', action='store_true', help="This changes spaces to underscores")
    group.add_argument('-sm', action='store_true', help="This changes spaces to minuses")

    group_case = parser.add_mutually_exclusive_group()
    group_case.add_argument('-l', action='store_true', help="This makes all letters lower case")
    group_case.add_argument('-u', action='store_true', help="This makes all letters upper case")
    group_case.add_argument('-c', action='store_true', help="This makes the words camel case")

    args = parser.parse_args()
    print(args)
    print(args.rs)
    print(args.su)
    print(args.sm)
    print(args.l)
    print(args.u)
    print(args.c)


def main():
    # Based on
    if os.path.exists("test.txt"):
        src = os.path.realpath("test.txt");

        os.rename('test.txt','test01.txt')


if __name__ == "__main__":
    #input command line parameters
    #get path
    #get format
    arguments()