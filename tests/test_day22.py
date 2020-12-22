import json

import pytest

from day22 import app as day22
from tests import get_event_input_raw


def test_day22_1_test():
    event = get_event_input_raw("day22/input_test.txt")
    ret = day22.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 306


def test_day22_1():
    event = get_event_input_raw("day22/input.txt")
    ret = day22.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 31809


def test_day22_2_test():
    event = get_event_input_raw("day22/input_test.txt")
    ret = day22.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 291


def test_day22_2():
    event = get_event_input_raw("day22/input.txt")
    ret = day22.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 32835
