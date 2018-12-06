import re

from hypothesis.internal.intervalsets import IntervalSet


def ranges(spec):
    """Return a range like object, parsed from the string spec
    """
    patt = re.compile(r'(\d+)?(-)?(\d+)?')
    return [(int(r[0] or '0'), int(r[2] or '1000')) for r in patt.findall(spec) if r[0] or r[2]]


def split_line_by_delimiter(line, delimiter="\t"):
    if len(delimiter) != 1:
        raise ValueError("the delimiter must be a single character")
    return list(re.split(r"{}".format(delimiter), str(line)))

def choose_fields(index_field_list, list_of_fields, complement=False):
    if min(index_field_list) < 1:
        raise ValueError("fields are numbered from 1")
    result = []
    if complement:
        index_field_list = set(range(len(list_of_fields))) - set(index_field_list)
    for field in index_field_list:
        try:
            result.append(str(list_of_fields[int(field-1)]))
        except IndexError:
            result.append("")
    return result

def choose_character(index_character_list, line, complement=False):
    if min(index_character_list) < 1:
        raise ValueError("byte/character positions are numbered from 1")
    result = []
    if complement:
        index_character_list = set(range(len(line))) - set(index_character_list)
    for index in index_character_list:
        try:
            result.append(str(line[index-1]))
        except IndexError:
            result.append("")
    return result

def choose_byte(index_byte_list, line, complement=False):
    if min(index_byte_list) < 1:
        raise ValueError("byte/character positions are numbered from 1")
    try:
        bytes_line = str.encode(line)
    except TypeError as e:
        raise e

    result = []

    if complement:
        index_byte_list = set(range(len(line))) - set(index_byte_list)

    for byte_index in index_byte_list:
        try:
            b = bytes_line[byte_index - 1]
            result.append(ord(b))
        except IndexError:
            result.append(ord(""))

    return result

assert split_line_by_delimiter("Hello World", " ") == ["Hello", "World"]
assert choose_fields([1], split_line_by_delimiter("Hello World", " ")) == ["Hello"]
assert choose_fields([1], split_line_by_delimiter("Hello World", " "), complement=True) == ["World"]
assert choose_fields([1,2], split_line_by_delimiter("Hello World", " ")) == ["Hello", "World"]

assert choose_character([1,2,3,4], "Hello World") == ["H", "e", "l", "l"]
assert choose_character([1,2,3,4], "Hello", complement=True) == ["o"]

assert choose_character([1], "Hello World") == ["H"]

assert choose_byte([1,2,3,4,5], "Hello") == [72, 101, 108, 108, 111]
assert choose_byte([1,2,3,4], "Hello World") == [72, 101, 108, 108]
assert choose_byte([1,2,3,4], "Hello", complement=True) == [111]

