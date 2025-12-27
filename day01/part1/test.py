from __future__ import annotations

import pytest

from . import solution


@pytest.mark.parametrize(
    ("output"),
    [
        (3),
    ],
)
def test_input(output):
    assert solution.main("test_input.txt") == output
