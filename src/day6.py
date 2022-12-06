import re
import time
from copy import deepcopy
from typing import List, Tuple, Dict

from InputHelper import InputHelper

helper = InputHelper(6)
data = helper.load_data(as_string=True)


def find_sequence_position(line: str, message=False) -> int:
    opening_sequence_start = 0
    if message:
        section_size = 14
    else:
        section_size = 4

    for position in range(section_size, len(line)):
        current_chars = line[position - section_size:position]
        chars_as_set = set(current_chars)
        if len(chars_as_set) == section_size:
            opening_sequence_start = position
            break

    return opening_sequence_start


start = time.time()
opening_sequence_position = find_sequence_position(data)

print("The opening sequence is located at postion {} with the pair of \"{}\", calculated in {:.2f}ms".format(opening_sequence_position, data[opening_sequence_position - 4:opening_sequence_position], (time.time() - start) * 1000))

start = time.time()
message_sequence_position = find_sequence_position(data, True)

print("The message sequence is located at postion {} with the pair of \"{}\", calculated in {:.2f}ms".format(message_sequence_position, data[message_sequence_position - 14:message_sequence_position], (time.time() - start) * 1000))
