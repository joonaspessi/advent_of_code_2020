import json

import pytest

from day11 import app as day11
from tests import get_event_input_raw


def test_day11_1_test():
    event = get_event_input_raw("day11/input_test.txt")
    ret = day11.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 37


def test_day11_1():
    event = get_event_input_raw("day11/input.txt")
    ret = day11.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2472


def test_day11_2_test():
    event = get_event_input_raw("day11/input_test.txt")
    ret = day11.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 26


def test_day11_2():
    event = get_event_input_raw("day11/input.txt")
    ret = day11.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2197
