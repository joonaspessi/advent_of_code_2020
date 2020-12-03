import json

import pytest

from day2 import app as day2


def get_event_input(inputFilePath):
    with open(inputFilePath, 'r') as f:
        input_data = f.read()
        lines = []
        for line in input_data.splitlines():
            lines.append(line)

    return {
        "body": json.dumps({"input": lines})
    }


def test_day2_1(mocker):
    event = get_event_input("day2/input.txt")
    ret = day2.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 586


def test_day2_2(mocker):
    event = get_event_input("day2/input.txt")
    ret = day2.lambda_handler_2(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 352
