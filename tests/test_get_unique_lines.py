#!/bin/env python3

import pytest

from tools.get_unique_lines.get_unique_lines import read_items, compare_items


def test_read_items():
    """
    Check if can read from file
    """
    import tempfile
    import pathlib

    tmp = tempfile.mkstemp(dir="/tmp")
    f = pathlib.Path(tmp[1])
    f.write_text("123\n456")
    items = read_items(str(f))
    assert items == ["123", "456"]


@pytest.mark.parametrize(
    "opts",
    [
        {
            "content": {"f1": [1, 2, 3, 4], "f2": [3, 4, 5]},
            "expected": {"f1": [1, 2], "f2": [5]}
        },
        {
            "content": {"f1": [1, 2, 3, 4], "f2": []},
            "expected": {"f1": [1, 2, 3, 4]}
        },
        {
            "content": {"f1": [1, 2, 3, 4]},
            "expected": {"f1": [1, 2, 3, 4]}
        },

    ],
    ids=["Two files, have difference", "Second file is empty", "Single file"]
)
def test_compare_items(opts):
    """
    Check comparison logic
    """
    actual = compare_items(opts["content"])
    assert actual == opts["expected"]
