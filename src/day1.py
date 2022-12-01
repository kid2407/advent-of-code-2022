import time
from typing import List

from InputHelper import InputHelper

helper = InputHelper(1)
data = helper.load_data()


def count_calories(lines) -> List[int]:
    elves = []
    current = 0
    for line in lines:
        if line == "" and current > 0:
            elves.append(current)
            current = 0
        else:
            current += int(line)
    if current > 0:
        elves.append(current)

    return elves


start = time.time()
calorie_list = count_calories(data)
max_calories = max(calorie_list)

print("The most calories any one elf carries is {}, calculated in {:.2f}ms".format(max_calories, (time.time() - start) * 1000))

start = time.time()
calorie_list.sort(reverse=True)
top_elves = calorie_list[:3]
top_calories = sum(top_elves)

print("The top three elves have a combined total of {} calories, calculated in {:.2f}ms".format(top_calories, (time.time() - start) * 1000))
