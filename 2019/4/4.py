"""
No input file this time, just a range
"""
input_start = 146810
input_stop = 612564

matches1 = set()
matches2 = set()
for i in range(input_start, input_stop):
    number = str(i)
    double = False
    asc = True
    # Count occurrences of each digit
    count = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0,
             '9': 0, '0': 0}
    for f in number:
        count[f] += 1
    # Make sure digits are ascending
    for j in range(len(number) - 1):
        if number[j + 1] < number[j]:
            asc = False
    # Check if there is a double digit
    if any(v >= 2 for _, v in count.items()):
        double = True
    # Ascending and contains a double digit. Match for part 1!
    if double and asc:
        matches1.add(i)

    # Part 2
    double = False
    # Make sure the doubles are not part of a bigger group
    if any(v == 2 for _, v in count.items()):
        double = True
    # There is a double, it's not part of a bigger group, digits are ascending.
    # It's a bingo!
    if double and asc:
        matches2.add(i)
print("Part #1: ", len(matches1))
print("Part #2: ", len(matches2))
