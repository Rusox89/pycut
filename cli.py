import argparse
import sys

import functions

def parse_args():
    parser = argparse.ArgumentParser(description='remove sections from each line of files')
    parser.add_argument('files', type=argparse.FileType('r'), default=[sys.stdin],
                        nargs='*'
                        )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--bytes', '-b', metavar='LIST',
                       type=functions.ranges,
                        help='select only these bytes')
    group.add_argument('--characters', '-c', metavar='LIST',
                       type=functions.ranges,
                       help='select only these characters')
    group.add_argument('--fields', '-f', metavar='LIST',
                       type=functions.ranges,
                       help='select  only  these  fields;  also print any line that contains no delimiter character, unless the -s option is specified')

    parser.add_argument('--delimiter', '-d', metavar='DELIM',
                        default='\t',
                        help='use DELIM instead of TAB for field delimiter')

    parser.add_argument('-n',
                        help='(ignored)')
    parser.add_argument('--complement', action='store_true',
                        help='complement the set of selected bytes, characters or fields')
    parser.add_argument('--only-delimited', '-s', action='store_true',
                        help='do not print lines not containing delimiters')
    parser.add_argument('--output-delimiter', metavar='STRING',
                        help='use STRING as the output delimiter the default is to use the input delimiter')
    parser.add_argument('--zero-terminated', '-z',
                        dest='line_delimiter', action='store_const', const='\0',
                        help='line delimiter is NUL, not newline')
    parser.add_argument('--version', action='store_true',
                        help='output version information and exit')

    parser.set_defaults(line_delimiter='\n')

    args = parser.parse_args()
    return parser, args


if __name__ == '__main__':
    parser, args = parse_args()
    print(args)
