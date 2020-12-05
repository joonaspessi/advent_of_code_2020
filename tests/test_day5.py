import json

import pytest

from day5 import app as day5
from tests import get_event_input_raw


def test_get_row():
    assert day5.get_row("FFFBBBF", 0, 127) == 14
    assert day5.get_row("FBFBBFF", 0, 127) == 44
    assert day5.get_row("BFFFBBF", 0, 127) == 70
    assert day5.get_row("BBFFBBF", 0, 127) == 102


def test_get_column():
    assert day5.get_column("RRR", 0, 7) == 7
    assert day5.get_column("RLL", 0, 7) == 4


def test_day5_1():
    event = get_event_input_raw("day5/input.txt")
    ret = day5.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 806


def test_day5_2():
    event = get_event_input_raw("day5/input.txt")
    ret = day5.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 562
