import math

with open("input", "r") as f:
    data = f.readlines()


# Part 1
def rocket_equation_simple(mass):
    return math.floor(mass / 3) - 2


print("#1: ", sum(rocket_equation_simple(int(i)) for i in data))


# Part 2
def rocket_equation_recursive(mass):
    if mass < 0:
        return 0
    else:
        boo = rocket_equation_recursive(rocket_equation_simple(mass))
        return rocket_equation_simple(mass) + (boo if boo > 0 else 0)


print("#2: ", sum(rocket_equation_recursive(int(i)) for i in data))
