import json

import pytest

from day18 import app as day18
from tests import get_event_input_raw


def test_day18_1_test():
    event = get_event_input_raw("day18/input_test.txt")
    ret = day18.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 112


def test_day18_1():
    event = get_event_input_raw("day18/input.txt")
    ret = day18.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 346


def test_day18_2_test():
    event = get_event_input_raw("day18/input_test.txt")
    ret = day18.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 848


def test_day18_2():
    event = get_event_input_raw("day18/input.txt")
    ret = day18.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 1632
