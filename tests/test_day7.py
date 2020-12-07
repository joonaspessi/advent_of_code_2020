import json

import pytest

from day7 import app as day7
from tests import get_event_input_raw


def test_day7_1_test():
    event = get_event_input_raw("day7/input_test.txt")
    ret = day7.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 4


def test_day7_2_test():
    event = get_event_input_raw("day7/input_test2.txt")
    ret = day7.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 126


def test_day7_1():
    event = get_event_input_raw("day7/input.txt")
    ret = day7.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 278


def test_day7_2():
    event = get_event_input_raw("day7/input.txt")
    ret = day7.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 45157
