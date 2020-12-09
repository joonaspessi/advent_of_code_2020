import json

import pytest

from day9 import app as day9
from tests import get_event_input_raw


def test_day9_1():
    event = get_event_input_raw("day9/input.txt")
    ret = day9.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 22406676


def test_day9_2():
    event = get_event_input_raw("day9/input.txt")
    ret = day9.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2942387
