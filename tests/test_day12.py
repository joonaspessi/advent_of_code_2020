import json

import pytest

from day12 import app as day12
from tests import get_event_input_raw


def test_day12_1_test():
    event = get_event_input_raw("day12/input_test.txt")
    ret = day12.lambda_handler_3(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 25


def test_day12_1():
    event = get_event_input_raw("day12/input.txt")
    ret = day12.lambda_handler_3(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 1603


def test_day12_2_test():
    event = get_event_input_raw("day12/input_test.txt")
    ret = day12.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 286


def test_day12_2():
    event = get_event_input_raw("day12/input.txt")
    ret = day12.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 52866
