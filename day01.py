import pandas as pd

input_list = pd.read_csv('day01.txt', header=None)[0]
input_set = set(input_list)
total_sum = 2020


def find_sumbers(target_sum):
    for i in input_set:
        x = target_sum - i
        if x in input_set:
            return i*x
    return 0


print('Part 1 answer:', find_sumbers(total_sum))

for j in input_set:
    next_sum = total_sum - j
    result = find_sumbers(next_sum)
    if result != 0:
        print('Part 2 answer:', j*result)
        break
