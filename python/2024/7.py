from operator import mul, add
from itertools import product


def solver(text):
    candidates = {}
    for i in text.splitlines():
        a, b = i.split(": ")
        candidates[int(a)] = [int(i) for i in b.split(" ")]
    return p1(candidates, operations=[mul, add]), p1(
        candidates, operations=[mul, add, concat]
    )


def is_a_match(nums, ops, target):
    val = nums[0]
    for i in range(len(ops)):
        val = ops[i](val, nums[i + 1])
    return val == target


def concat(a, b):
    return int(str(a) + str(b))


def p1(candidates: dict[int, list[int]], operations) -> int:
    matches = 0
    for res, nums in candidates.items():
        for op_choice_set in product(operations, repeat=len(nums) - 1):
            if is_a_match(nums, op_choice_set, res):
                matches += res
                break
    return matches


# 4440170732049 low!
