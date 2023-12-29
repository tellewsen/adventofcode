from collections import Counter
from functools import cmp_to_key
from typing import Literal, Union
import pytest


@pytest.fixture
def example_hands():
    with open("./example_input") as f:
        hands = [(i[0], int(i[1])) for i in (i.split() for i in f.readlines())]
    return hands


def test_parts(example_hands):
    assert main(example_hands, compare_hands) == 6440
    assert main(example_hands, compare_hands2) == 5905


def card_to_val(x: str, part: int = 1):
    mapping = {"T": 10, "J": 11 if part == 1 else 1, "Q": 12, "K": 13, "A": 14}
    return int(mapping.get(x, x))


def compare_hands(x: str, y: str) -> Literal[0] | Literal[1] | Literal[-1]:
    x = x[0]
    y = y[0]
    x_most_common = Counter(x).most_common()
    y_most_common = Counter(y).most_common()
    x_second = str(x_most_common[1][1]) if len(x_most_common) > 1 else "0"
    y_second = str(y_most_common[1][1]) if len(y_most_common) > 1 else "0"
    x_most_common_count = int(str(x_most_common[0][1]) + x_second)
    y_most_common_count = int(str(y_most_common[0][1]) + y_second)
    if x_most_common_count > y_most_common_count:
        return -1
    if y_most_common_count > x_most_common_count:
        return 1
    for i in range(5):
        x_val = card_to_val(x[i])
        y_val = card_to_val(y[i])
        if x_val > y_val:
            return -1
        if y_val > x_val:
            return 1
    return 0


def compare_hands2(x: str, y: str) -> Literal[0] | Literal[1] | Literal[-1]:
    x = x[0]
    y = y[0]
    x_most_common = Counter(x.replace("J", "")).most_common()
    y_most_common = Counter(y.replace("J", "")).most_common()
    x_first = str(x_most_common[0][1]) if len(x_most_common) > 0 else "0"
    y_first = str(y_most_common[0][1]) if len(y_most_common) > 0 else "0"
    x_second = str(x_most_common[1][1]) if len(x_most_common) > 1 else "0"
    y_second = str(y_most_common[1][1]) if len(y_most_common) > 1 else "0"
    x_most_common_count = int(str(x_first) + x_second) + 10 * x.count("J")
    y_most_common_count = int(str(y_first) + y_second) + 10 * y.count("J")
    if x_most_common_count > y_most_common_count:
        return -1
    if y_most_common_count > x_most_common_count:
        return 1
    for i in range(5):
        x_val = card_to_val(x[i], 2)
        y_val = card_to_val(y[i], 2)
        if x_val > y_val:
            return -1
        if y_val > x_val:
            return 1
    return 0


def main(hands, cmp_func):
    sorted_hands = reversed(sorted(hands, key=cmp_to_key(cmp_func)))
    return sum((index + 1) * i[1] for index, i in enumerate(sorted_hands))


if __name__ == "__main__":
    with open("./input") as f:
        hands = [(i[0], int(i[1])) for i in (j.split() for j in f.readlines())]
    print("p1: ", main(hands, compare_hands))
    print("p2: ", main(hands, compare_hands2))
