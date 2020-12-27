import json

import pytest

from day20 import app as day20
from tests import get_event_input_raw


def test_day20_1_test():
    event = get_event_input_raw("day20/input_test.txt")
    ret = day20.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 20899048083289


def test_day20_1():
    event = get_event_input_raw("day20/input.txt")
    ret = day20.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 32287787075651


def test_day20_2():
    event = get_event_input_raw("day20/input.txt")
    ret = day20.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 1939
