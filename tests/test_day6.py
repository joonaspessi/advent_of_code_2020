import json

import pytest

from day6 import app as day6
from tests import get_event_input_raw


def test_day6_1_test():
    event = get_event_input_raw("day6/input_test.txt")
    ret = day6.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 11


def test_day6_2_test():
    event = get_event_input_raw("day6/input_test.txt")
    ret = day6.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 6


def test_day6_1():
    event = get_event_input_raw("day6/input.txt")
    ret = day6.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 6799


def test_day6_2():
    event = get_event_input_raw("day6/input.txt")
    ret = day6.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 3354
