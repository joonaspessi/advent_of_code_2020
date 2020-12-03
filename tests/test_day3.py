import json

import pytest

from tests import get_event_input

from day3 import app as day3


def get_event_input2(inputFilePath):
    with open(inputFilePath, 'r') as f:
        input_data = f.read()
        lines = []
        for line in input_data.splitlines():
            lines.append(line)

    return {
        "body": json.dumps({"input": lines})
    }


def test_day3_1_overlap_x_axis(mocker):

    event = get_event_input("day3/test_input.txt")
    puzzle = day3.parse_event_to_puzzle(event)
    position = day3.Position(x=8, y=0, page=0, puzzle_length_x=len(
        puzzle[0]), puzzle_length_y=len(puzzle))
    new_pos = day3.move(position, 3, 1)

    assert new_pos.x == 0
    assert new_pos.y == 1
    assert new_pos.page == 1


def test_day3_1_overlap_x_axis2(mocker):

    event = get_event_input("day3/test_input.txt")
    puzzle = day3.parse_event_to_puzzle(event)
    position = day3.Position(x=9, y=0, page=0, puzzle_length_x=len(
        puzzle[0]), puzzle_length_y=len(puzzle))
    new_pos = day3.move(position, 3, 1)

    assert new_pos.x == 1
    assert new_pos.y == 1
    assert new_pos.page == 1


def test_day3_1_move_to_edge(mocker):

    event = get_event_input("day3/test_input.txt")
    puzzle = day3.parse_event_to_puzzle(event)
    position = day3.Position(x=7, y=0, page=0, puzzle_length_x=len(
        puzzle[0]), puzzle_length_y=len(puzzle))
    new_pos = day3.move(position, 3, 1)

    assert new_pos.x == 10
    assert new_pos.y == 1
    assert new_pos.page == 0


def test_day3_1_test_data(mocker):
    event = get_event_input("day3/test_input.txt")
    ret = day3.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 7


def test_day3_1_given_input(mocker):
    event = get_event_input("day3/input.txt")
    ret = day3.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 228


def test_day3_2_given_input(mocker):
    event = get_event_input("day3/input.txt")
    ret = day3.lambda_handler_2(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 6818112000
