
FILENAME = "day_two.txt"

with open(FILENAME, 'r') as f:
    lines = f.readlines()

counter_for_first = 0

for el in lines:
    if el[0] == "B" and el[2] == "X":
        counter_for_first = counter_for_first + 1
    elif el[0] == "A" and el[2] == "X":
        counter_for_first = counter_for_first + 4
    elif el[0] == "C" and el[2] == "X":
        counter_for_first = counter_for_first + 7

    elif el[0] == "A" and el[2] == "Y":
        counter_for_first = counter_for_first + 8
    elif el[0] == "B" and el[2] == "Y":
        counter_for_first = counter_for_first + 5
    elif el[0] == "C" and el[2] == "Y":
        counter_for_first = counter_for_first + 2

    elif el[0] == "A" and el[2] == "Z":
        counter_for_first = counter_for_first + 3
    elif el[0] == "B" and el[2] == "Z":
        counter_for_first = counter_for_first + 9
    elif el[0] == "C" and el[2] == "Z":
        counter_for_first = counter_for_first + 6


print(counter_for_first)