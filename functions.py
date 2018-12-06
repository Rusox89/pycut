import re

def split_line_by_delimiter(delimiter="\t"):
    return list(re.split(r"{}".format(delimiter)))

def choose_fields(index_field_list, list_of_fields):
    result = []
    for field in index_field_list:
        try:
            result.append(str(list_of_fields[int(field)]))
        except IndexError:
            result.append("")
    return result

def choose_character(index_character_list, line):
    result = []
    for index in index_character_list:
        try:
            result.append(str(line[index]))
        except IndexError:
            result.append("")
    return result
