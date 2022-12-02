import time
from typing import List, Set, Dict

from InputHelper import InputHelper

helper = InputHelper(2)
data = helper.load_data()


def parse_matches(lines: List[str]) -> List[Dict[str, str]]:
    match_list = []

    for line in lines:
        opponent, you = line.split(' ')
        match_list.append({
            "opponent": opponent,
            "you": you
        })

    return match_list


def calculate_matches(match_list: List[Dict[str, str]], refined: bool = False) -> int:
    shape_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        "A": 1,
        "B": 2,
        "C": 3
    }
    score = 0

    for match in match_list:
        opponent = shape_scores[match["opponent"]]
        you = shape_scores[match["you"]]

        if not refined:
            if opponent == you:
                score += 3
            elif you == 1 and opponent == 3:
                score += 6
            elif you == 2 and opponent == 1:
                score += 6
            elif you == 3 and opponent == 2:
                score += 6
            score += you
        else:
            if you == 1:
                score += 3 if opponent == 1 else (1 if opponent == 2 else 2)
            elif you == 2:
                score += 3 + opponent
            elif you == 3:
                score += 6 + (2 if opponent == 1 else (3 if opponent == 2 else 1))

    return score


matches = parse_matches(data)

start = time.time()
final_score = calculate_matches(matches)

print("If they strategy guide works, your score will be {}, calculated in {:.2f}ms".format(final_score, (time.time() - start) * 1000))

start = time.time()
final_score = calculate_matches(matches, True)

print("With the revised strategy guide, your score will be {}, calculated in {:.2f}ms".format(final_score, (time.time() - start) * 1000))
