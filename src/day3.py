import time
from typing import List

from InputHelper import InputHelper

helper = InputHelper(3)
data = helper.load_data()


def calculate_score_for_character(character: str) -> int:
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38


def analyze_rucksacks(rucksacks: List[str]) -> int:
    priorities_sum = 0

    for rucksack in rucksacks:
        half_size = int(len(rucksack) / 2)
        left = rucksack[:half_size]
        right = rucksack[half_size:]

        for char in left:
            if char in right:
                priorities_sum += calculate_score_for_character(char)
                break

    return priorities_sum


def find_elves_group_badges(rucksacks: List[str]) -> int:
    badge_priorities = 0
    index = 0

    while index < len(rucksacks):
        first_elf = rucksacks[index]
        second_elf = rucksacks[index + 1]
        third_elf = rucksacks[index + 2]

        for char in first_elf:
            if char in second_elf and char in third_elf:
                badge_priorities += calculate_score_for_character(char)
                break
        index += 3

    return badge_priorities


start = time.time()
priority_sum = analyze_rucksacks(data)

print("The priority sum above all rucksacks is {}, calculated in {:.2f}ms".format(priority_sum, (time.time() - start) * 1000))

start = time.time()
badges_sum = find_elves_group_badges(data)

print("The priority sum for all badges is {}, calculated in {:.2f}ms".format(badges_sum, (time.time() - start) * 1000))
