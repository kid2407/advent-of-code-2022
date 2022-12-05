import re
import time
from copy import deepcopy
from typing import List, Tuple, Dict

from InputHelper import InputHelper

helper = InputHelper(5)
data = helper.load_data()


def parse_input_data(lines: List[str]) -> Tuple[Dict[int, List[str]], List[Dict[str, int]]]:
    stacks_data = {}
    instructions_list = []
    instructions_reached = False

    for line in lines:
        if not instructions_reached:
            if len(line) > 0 and "[" in line:
                stack_number = 1
                while len(line) > 0:
                    if stack_number not in stacks_data:
                        stacks_data[stack_number] = []
                    section = line[:3]
                    reg = re.compile(r"\[(?P<crate>\w)]")
                    match = reg.search(section)
                    if match is not None:
                        stacks_data[stack_number].insert(0, match.group("crate"))
                    line = line[4:]
                    stack_number += 1
            else:
                instructions_reached = True
        else:
            reg = re.compile(r"move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)")
            matches = reg.search(line)

            if matches is not None:
                instructions_list.append({
                    'amount': int(matches.group('amount')),
                    'from': int(matches.group('from')),
                    'to': int(matches.group('to'))
                })

    return stacks_data, instructions_list


def move_crates(crate_data: Dict[int, List[str]], movement_instructions: List[Dict[str, int]], is_new_crane_model=False) -> Dict[int, List[str]]:
    local_crate_data = deepcopy(crate_data)
    for instruction in movement_instructions:
        amount = instruction['amount']
        from_stack = instruction['from']
        to_stack = instruction['to']
        if is_new_crane_model:
            moved_crates = local_crate_data[from_stack][-amount:]
            del local_crate_data[from_stack][-amount:]
            local_crate_data[to_stack].extend(moved_crates)
        else:
            for i in range(0, amount):
                crate = local_crate_data[from_stack].pop()
                local_crate_data[to_stack].append(crate)

    return local_crate_data


start = time.time()
stacks, instructions = parse_input_data(data)
print("Parsing the data took {:.2f}ms".format((time.time() - start) * 1000))

start = time.time()
crates = move_crates(stacks, instructions)
top_crates = ""

for key, crate_stack in crates.items():
    top_crates += crate_stack.pop()

print("The crates on the top result in the string \"{}\", calculated in {:.2f}ms".format(top_crates, (time.time() - start) * 1000))

start = time.time()
crates = move_crates(stacks, instructions, True)
top_crates = ""

for key, crate_stack in crates.items():
    if len(crate_stack) > 0:
        top_crates += crate_stack.pop()

print("The crates on the top result with the crane mover 9001 result in the string \"{}\", calculated in {:.2f}ms".format(top_crates, (time.time() - start) * 1000))
