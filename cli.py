import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='remove sections from each line of files')
    parser.add_argument('files', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--bytes', '-b', metavar='LIST',
                        help='select only these bytes')
    parser.add_argument('--characters', '-c', metavar='LIST',
                        help='select only these characters')
    parser.add_argument('--delimiter', '-d', metavar='DELIM',
                        help='use DELIM instead of TAB for field delimiter')
    parser.add_argument('--fields', '-f', metavar='LIST',
                        help='select  only  these  fields;  also print any line that contains no delimiter character, unless the -s option is specified')
    parser.add_argument('-n',
                        help='(ignored)')
    parser.add_argument('--complement', 
                        help='complement the set of selected bytes, characters or fields')
    parser.add_argument('--only-delimited', '-s',
                        help='do not print lines not containing delimiters')
    parser.add_argument('--output-delimiter', metavar='STRING',
                        help='use STRING as the output delimiter the default is to use the input delimiter')
    parser.add_argument('--zero-terminated', '-z',
                        help='line delimiter is NUL, not newline')
    parser.add_argument('--version', 
                        help='output version information and exit')

    args = parser.parse_args()
    return parser, args


if __name__ == '__main__':
    parse_args()
