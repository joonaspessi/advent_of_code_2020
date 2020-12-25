import json

import pytest

from day24 import app as day24
from tests import get_event_input_raw


def test_day24_1_test():
    event = get_event_input_raw("day24/input_test.txt")
    ret = day24.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 10


def test_day24_1():
    event = get_event_input_raw("day24/input.txt")
    ret = day24.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 488


def test_day24_2_test():
    event = get_event_input_raw("day24/input_test.txt")
    ret = day24.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2208


def test_day24_2():
    event = get_event_input_raw("day24/input.txt")
    ret = day24.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 4118
