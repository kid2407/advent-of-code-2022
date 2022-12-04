import re
import time
from typing import List

from InputHelper import InputHelper

helper = InputHelper(4)
data = helper.load_data()


def find_overlapping_pair_count(lines: List[str], in_part=False) -> int:
    overlapping_pairs = 0

    for line in lines:
        reg = re.compile(r"^(?P<first_elf_start>\d+)-(?P<first_elf_end>\d+),(?P<second_elf_start>\d+)-(?P<second_elf_end>\d+)$")
        result = reg.search(line)

        if result is not None:
            first_elf_start = int(result.group("first_elf_start"))
            first_elf_end = int(result.group("first_elf_end"))
            second_elf_start = int(result.group("second_elf_start"))
            second_elf_end = int(result.group("second_elf_end"))

            if in_part:
                if first_elf_start <= second_elf_start <= first_elf_end or first_elf_start <= second_elf_end <= first_elf_end or second_elf_start <= first_elf_start <= second_elf_end or second_elf_start <= first_elf_end <= second_elf_end:
                    overlapping_pairs += 1
            else:
                if (first_elf_start >= second_elf_start and first_elf_end <= second_elf_end) or (second_elf_start >= first_elf_start and second_elf_end <= first_elf_end):
                    overlapping_pairs += 1

    return overlapping_pairs


start = time.time()
overlap_count = find_overlapping_pair_count(data)

print("The number of completely overlapping pairs is {}, calculated in {:.2f}ms".format(overlap_count, (time.time() - start) * 1000))

start = time.time()
overlap_count = find_overlapping_pair_count(data, True)

print("The number of partly overlapping pairs is {}, calculated in {:.2f}ms".format(overlap_count, (time.time() - start) * 1000))
