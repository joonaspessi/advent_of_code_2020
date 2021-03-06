import json

import pytest

from day10 import app as day10
from tests import get_event_input_raw


def test_day10_1_test():
    event = get_event_input_raw("day10/input_test.txt")
    ret = day10.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 220


def test_day10_1():
    event = get_event_input_raw("day10/input.txt")
    ret = day10.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2414


def test_day10_2_test():
    event = get_event_input_raw("day10/input_test.txt")
    ret = day10.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 19208


def test_day10_2():
    event = get_event_input_raw("day10/input.txt")
    ret = day10.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 21156911906816
