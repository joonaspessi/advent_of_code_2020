import json

import pytest

from day8 import app as day8
from tests import get_event_input_raw


def test_day8_1_test():
    event = get_event_input_raw("day8/input_test.txt")
    ret = day8.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 5


def test_day8_2_test():
    event = get_event_input_raw("day8/input_test.txt")
    ret = day8.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 8


def test_day8_1():
    event = get_event_input_raw("day8/input.txt")
    ret = day8.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 278


def test_day8_2():
    event = get_event_input_raw("day8/input.txt")
    ret = day8.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 672
