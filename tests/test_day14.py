import json

import pytest

from day14 import app as day14
from tests import get_event_input_raw


def test_day14_1_test():
    event = get_event_input_raw("day14/input_test.txt")
    ret = day14.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 165


def test_day14_1():
    event = get_event_input_raw("day14/input.txt")
    ret = day14.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 6559449933360


def test_day14_2_test():
    event = get_event_input_raw("day14/input_test2.txt")
    ret = day14.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 208


def test_day14_2():
    event = get_event_input_raw("day14/input.txt")
    ret = day14.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 3369767240513
