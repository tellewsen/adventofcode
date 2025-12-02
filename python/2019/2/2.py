# Read data
foo = []


def read_file():
    output = []
    with open("input", "r") as f:
        for line in f.readlines():
            input = line.split(",")
    for l in input:
        output.append(int(l))
    return output


# Raplace pos 1 with valkue 12 and pos 2 with value 2
original = read_file()


# Part 1
def intcode(ins):
    for index in range(0, len(ins), 4):
        try:
            if ins[index] == 1:
                ins[ins[index + 3]] = ins[ins[index + 1]] + ins[ins[index + 2]]
            elif ins[index] == 2:
                ins[ins[index + 3]] = ins[ins[index + 1]] * ins[ins[index + 2]]
            elif ins[index] == 99:
                return
            else:
                raise Exception("Weird value at pos {}: {} ".format(index, ins[index]))
        except IndexError:
            continue
        except Exception as e:
            print(e, index)
            raise


part1 = original.copy()
part1[1] = 12
part1[2] = 2
intcode(part1)
print("#1 Solution: ", part1[0])


# Part 2
for i in range(0, 10000):
    for j in range(0, 10000):
        copy = original.copy()
        copy[1] = i
        copy[2] = j
        intcode(copy)
        if copy[0] == 19690720:
            print("#2 Solution: ", "i =", i, ",", "j =", j)
            print("#2 Answer is: ", 100 * i + j)
            break
    else:
        continue
    break
