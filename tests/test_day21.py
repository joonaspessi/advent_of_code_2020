import json

import pytest

from day21 import app as day21
from tests import get_event_input_raw


def test_day21_1_test():
    event = get_event_input_raw("day21/input_test.txt")
    ret = day21.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 5


def test_day21_1():
    event = get_event_input_raw("day21/input.txt")
    ret = day21.lambda_handler(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == 2162


def test_day21_2_test():
    event = get_event_input_raw("day21/input_test.txt")
    ret = day21.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == "mxmxvkd,sqjhc,fvjkl"


def test_day21_2():
    event = get_event_input_raw("day21/input.txt")
    ret = day21.lambda_handler_2(event, {})
    data = json.loads(ret["body"])
    assert data.get("result") == "lmzg,cxk,bsqh,bdvmx,cpbzbx,drbm,cfnt,kqprv"
