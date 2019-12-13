#! python 3
# This program will rename folders and files based on given standard.
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')

group = parser.add_mutually_exclusive_group()
group.add_argument('--rs',  help="This removes spaces")
group.add_argument('--csu', help="This changes spaces to underscores")
group.add_argument('--csm', help="This changes spaces to minuses")

group_case = parser.add_mutually_exclusive_group()
group_case.add_argument('-l', action='store_true', help="This makes all letters lower case")
group_case.add_argument('-u', action='store_true', help="This makes all letters upper case")
group_case.add_argument('-c', action='store_true', help="This makes the words camel case")

args = parser.parse_args()
a = args.a
print(a)