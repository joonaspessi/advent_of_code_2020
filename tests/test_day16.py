import json

import pytest

from day16 import app as day16
from tests import get_event_input_raw


def test_day16_1_test():
    event = get_event_input_raw("day16/input_test.txt")
    ret = day16.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 71


def test_day16_1():
    event = get_event_input_raw("day16/input.txt")
    ret = day16.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 26053


def test_day16_2():
    event = get_event_input_raw("day16/input.txt")
    ret = day16.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 1515506256421
