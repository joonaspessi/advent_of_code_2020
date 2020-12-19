import json

import pytest

from day19 import app as day19
from tests import get_event_input_raw


def test_day19_1_test():
    event = get_event_input_raw("day19/input_test.txt")
    ret = day19.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2


def test_day19_1():
    event = get_event_input_raw("day19/input.txt")
    ret = day19.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 265


def test_day19_2_test():
    event = get_event_input_raw("day19/input_test2.txt")
    ret = day19.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 12


def test_day19_2():
    event = get_event_input_raw("day19/input.txt")
    ret = day19.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 394
