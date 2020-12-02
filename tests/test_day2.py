import json

import pytest

from day2_1 import app as day2_1
from day2_2 import app as day2_2


def get_event_input(inputFilePath):
    with open(inputFilePath, 'r') as f:
        input_data = f.read()
    return {
        "body": {
            "input": input_data
        }
    }


def test_day2_1(mocker):
    event = get_event_input("day2_1/input.txt")
    ret = day2_1.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 586


def test_day2_2(mocker):
    event = get_event_input("day2_2/input.txt")
    ret = day2_2.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 587
