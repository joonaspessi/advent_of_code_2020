import json
import re
from dataclasses import dataclass


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day3/input.txt", 'r') as f:
            lines = f.readlines()
    return lines


@dataclass
class Position:
    x: int
    y: int
    page: int
    puzzle_length_x: int
    puzzle_length_y: int


def move(position, delta_x, delta_y):
    page = position.page
    new_x = position.x + delta_x
    new_y = position.y + delta_y

    if new_x >= position.puzzle_length_x:
        new_x = new_x % position.puzzle_length_x
        page += 1

    return Position(x=new_x, y=new_y, page=page, puzzle_length_x=position.puzzle_length_x, puzzle_length_y=position.puzzle_length_y)


def is_end(position):
    return position.y == position.puzzle_length_y - 1


def get_position_element(position: Position, puzzle):
    character = puzzle[position.y][position.x]

    return {
        "free": True if character == "." else False,
        "tree": True if character == "#" else False
    }


def do_slope_puzzle(puzzle, delta_x, delta_y):
    line_length_x = len(puzzle[0])
    line_length_y = len(puzzle)
    position = Position(
        x=0, y=0, page=0, puzzle_length_x=line_length_x, puzzle_length_y=line_length_y)
    tree_count = 0
    completed = False

    while not completed:
        position = move(position, delta_x, delta_y)
        element = get_position_element(position, puzzle)

        if element.get("tree"):
            tree_count += 1

        if is_end(position):
            completed = True

    return tree_count


def lambda_handler(event, context):
    """Advent of code day 3, excercise 1
    """
    puzzle = get_input(event)
    tree_count = do_slope_puzzle(puzzle, 3, 1)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": tree_count
        }),
    }


def lambda_handler_2(event, context):
    """Advent of code day 3, excercise 2
    """
    puzzle = get_input(event)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = map(lambda n: do_slope_puzzle(
        puzzle, delta_x=n[0], delta_y=n[1]), slopes)

    tree_count_multiplied = 1
    for count in tree_counts:
        tree_count_multiplied = tree_count_multiplied * count

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": tree_count_multiplied
        }),
    }
