import json

import pytest

from day1 import app as day1
from tests import get_event_input_raw


def test_day1_1():
    event = get_event_input_raw("day1/input.txt")
    ret = day1.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 751776


def test_day1_2():
    event = get_event_input_raw("day1/input.txt")
    ret = day1.lambda_handler_2(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 42275090
