import json

import pytest

from day23 import app as day23
from tests import get_event_input_raw


def test_day23_1_test():
    event = get_event_input_raw("day23/input_test.txt")
    ret = day23.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 306


def test_day23_1():
    event = get_event_input_raw("day23/input.txt")
    ret = day23.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 31809


def test_day23_2_test():
    event = get_event_input_raw("day23/input_test.txt")
    ret = day23.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 291


def test_day23_2():
    event = get_event_input_raw("day23/input.txt")
    ret = day23.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 32835
