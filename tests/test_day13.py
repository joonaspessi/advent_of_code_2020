import json

import pytest

from day13 import app as day13
from tests import get_event_input_raw


def test_day13_1_test():
    event = get_event_input_raw("day13/input_test.txt")
    ret = day13.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 295


def test_day13_1():
    event = get_event_input_raw("day13/input.txt")
    ret = day13.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 1835


def test_day13_2_test():
    event = get_event_input_raw("day13/input_test.txt")
    ret = day13.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 1068781


def test_day13_2():
    event = get_event_input_raw("day13/input.txt")
    ret = day13.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 247086664214628
