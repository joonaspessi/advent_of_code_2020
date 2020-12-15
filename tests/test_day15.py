import json

import pytest

from day15 import app as day15
from tests import get_event_input_raw


def test_day15_1_test():
    event = get_event_input_raw("day15/input_test.txt")
    ret = day15.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 436


def test_day15_1():
    event = get_event_input_raw("day15/input.txt")
    ret = day15.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 447


def test_day15_2_test():
    event = get_event_input_raw("day15/input_test2.txt")
    ret = day15.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2578


def test_day15_2():
    event = get_event_input_raw("day15/input.txt")
    ret = day15.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 11721679
