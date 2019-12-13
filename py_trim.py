#! python 3
# This program will rename folders and files based on given standard.
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a", default=1, help="This is the 'a' variable")
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('--c', action='store_true', help="This is the 'c' variable")
group.add_argument('--d', action='store_true', help="This is the 'd' variable")

args = parser.parse_args()
a = args.a
print(a)