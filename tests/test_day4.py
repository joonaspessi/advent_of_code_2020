import json

import pytest

from tests import get_event_input

from day4 import app as day4


def test_day4_1_given_input(mocker):
    event = get_event_input("day4/input.txt")
    ret = day4.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 0


def test_day3_2_given_input(mocker):
    event = get_event_input("day4/input.txt")
    ret = day4.lambda_handler_2(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 0
