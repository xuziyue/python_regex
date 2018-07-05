""" Wrapped re functions
"""
import re

# All following function can add flags:
# re.I (ignore cases) re.M (multiple lines) re.S (dot can represent /)

def SEARCH(pattern, string):
    # Function
    # return re.search(pattern, string)
    p = re.compile(pattern)
    match = p.search(string)
    if match:
        return match.group(0)


def MATCH(pattern, string):
    p = re.compile(pattern)
    match = p.match(string)
    if match:
        return match.group(0)  
    

def FIND_ALL(pattern, string):
    p = re.compile(pattern)
    # get a list of all substrings in string that matches pattern
    strings_matched = p.find_all(string)
    return strings_matched


def SPLIT(pattern, string, max_split_number = None):
    p = re.compile(pattern)
    # get max_split_number pieces of substrings in string splited by pattern
    if max_split_number:
        others = p.split(string, max_split_number)
    else:
        others = p.split(string)
    return others


def FIND_ITER(pattern, string):
    p = re.compile(pattern)
    # iterate the match list
    for match in p.finditer(string):
        if match:
            print(match.group(0))


def SUB(pattern, replace, string, count = 0, flags = 0):
    p = re.compile(pattern)
    if count == 0:
        after_replacement = p.sub(replace, string)
    else:
        after_replacement = p.sub(replace, string, count)
    return after_replacement
