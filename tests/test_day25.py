import json

import pytest

from day25 import app as day25
from tests import get_event_input_raw


def test_day25_1_test():
    event = get_event_input_raw("day25/input_test.txt")
    ret = day25.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 14897079


def test_day25_1():
    event = get_event_input_raw("day25/input.txt")
    ret = day25.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 8740494
