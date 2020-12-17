import json

import pytest

from day17 import app as day17
from tests import get_event_input_raw


def test_day17_1_test():
    event = get_event_input_raw("day17/input_test.txt")
    ret = day17.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 112


def test_day17_1():
    event = get_event_input_raw("day17/input.txt")
    ret = day17.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 346


def test_day17_2_test():
    event = get_event_input_raw("day17/input_test.txt")
    ret = day17.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 848


def test_day17_2():
    event = get_event_input_raw("day17/input.txt")
    ret = day17.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 1632
