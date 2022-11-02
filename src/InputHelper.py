from os.path import isfile
from typing import List


class InputHelper:
    def __init__(self, day):
        self.day = day

    def load_data(self) -> List[str]:
        file_path = "../inputs/day{}.txt".format(self.day)

        if not isfile(path=file_path):
            print("File \"{}\" does not exist!\n".format(file_path))
            exit(1)

        lines = []
        handle = open(file=file_path, mode='rt')
        for line in handle:
            lines.append(line)

        return lines
