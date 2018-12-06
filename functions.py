import re

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


assert split_line_by_delimiter("Hello World", " ") == ["Hello", "World"]
assert choose_fields([1], split_line_by_delimiter("Hello World", " ")) == ["Hello"]
assert choose_fields([1], split_line_by_delimiter("Hello World", " "), complement=True) == ["World"]
assert choose_fields([1,2], split_line_by_delimiter("Hello World", " ")) == ["Hello", "World"]

assert choose_character([1,2,3,4], "Hello World") == ["H", "e", "l", "l"]
assert choose_character([1,2,3,4], "Hello", complement=True) == ["o"]

assert choose_character([1], "Hello World") == ["H"]
