## Py Trim
I wrote this program to be able to quickly modify folders and files to a desired naming convention.
py_trim.py
It has the following dependencies: argparse,fnmatch, and os.

## Description
py_trim can remove or change spaces in folders and file names as well as change the case to upper case or lower case.

## SYNOPSIS ##
py_trim [OPTIONS]
py_trim [-Space Control -Case Control --Input Control]

Example: [-rs -l --path "D:\code\python3\py_trim\test"]

## OPTIONS ##
### Generic Program Information ###
    --help, Print a usage message  briefly  summarizing  these  command-line options and then exit.

### Input Control ###
       --path, This is the path to the folder

### General Output Control ###
#### Space Control ####
Please select one of the following:
            
            -rs, This removes spaces
            -su, This changes spaces to underscores
            -sm, This changes spaces to minuses
#### Case Control ####
Please select one of the following:

            -l, This makes all letters lower case
            -u, This makes all letters upper case


## History
December 13, 2019 - Initial commit  
May 26, 2020 - v.1.0


## References
<https://levelup.gitconnected.com/the-easy-guide-to-python-command-line-arguments-96b4607baea1>


## License
MIT License