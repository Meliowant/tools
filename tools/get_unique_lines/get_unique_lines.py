#!/bin/env python3
"""
Compare a list of items in files
"""

import pathlib
import sys


def read_items(fname:str = "") -> list:
    """
    Make a list of items that are stored in the file


    Returns
    """
    items = []
    input_file = pathlib.Path(fname)
    if input_file.exists():
        with open(input_file) as f:
            itms = f.readlines()
            items = map(lambda x: x.strip(), itms)

    return list([itm for itm in items if len(str(itm)) > 0])


def compare_items(files:dict = {}) -> {}:
    """
    Find all items that are unique in each file
    """
    uniques = {k: [] for k in files.keys()}
    final_uniques = {}
    all_items = []
    for x in files.values():
        all_items.extend(x)

    unique_items = list(filter(lambda x: all_items.count(x) == 1, all_items))
    for k, v in files.items():
        uniques[k] = list([v_ for v_ in v if v_ in unique_items])

    final_uniques = dict({k: v for k, v in uniques.items() if v})
    return final_uniques


def usage():
    print(f"USAGE: {sys.argv[0]} file1 ... fileN")
    sys.exit(0)


def main(files:list = []):
    files_ = {
        k: read_items(k) for k in files
    }
    got_items = compare_items(files_)
    for k, v in got_items.items():
        print(f"{len(v)} item(s) in {k}:")
        for v_ in v:
            print(v_)

        print()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        main(files=sys.argv[1:])
