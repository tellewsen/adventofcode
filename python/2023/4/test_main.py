import pytest
from main import part1, part2


@pytest.fixture
def example_input():
    with open("example_input") as f:
        lines = f.read().splitlines()
    return lines


def test_main(example_input):
    assert part1(example_input) == 13
    assert part2(example_input) == 30
