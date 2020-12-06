import json

import pytest

from tests import get_event_input_raw

from day4 import app as day4


def test_byr_validation():
    assert day4.is_valid_byr("1919") == False
    assert day4.is_valid_byr("1920") == True
    assert day4.is_valid_byr("1999") == True
    assert day4.is_valid_byr("2000") == True
    assert day4.is_valid_byr("2002") == True
    assert day4.is_valid_byr("2003") == False


def test_iyr_validation():
    assert day4.is_valid_iyr("2009") == False
    assert day4.is_valid_iyr("2010") == True
    assert day4.is_valid_iyr("2020") == True
    assert day4.is_valid_iyr("2021") == False


def test_eyr_validation():
    assert day4.is_valid_eyr("1999") == False
    assert day4.is_valid_eyr("2009") == False
    assert day4.is_valid_eyr("2010") == True
    assert day4.is_valid_eyr("2015") == True
    assert day4.is_valid_eyr("2020") == True
    assert day4.is_valid_eyr("2021") == True
    assert day4.is_valid_eyr("2029") == True
    assert day4.is_valid_eyr("2030") == True
    assert day4.is_valid_eyr("2031") == False


def test_hgt_validation():
    assert day4.is_valid_hgt("58in") == False
    assert day4.is_valid_hgt("59in") == True
    assert day4.is_valid_hgt("61in") == True
    assert day4.is_valid_hgt("76in") == True
    assert day4.is_valid_hgt("77in") == False

    assert day4.is_valid_hgt("149cm") == False
    assert day4.is_valid_hgt("150cm") == True
    assert day4.is_valid_hgt("180cm") == True
    assert day4.is_valid_hgt("193cm") == True
    assert day4.is_valid_hgt("194cm") == False
    assert day4.is_valid_hgt("200cm") == False


def test_hcl_validation():
    assert day4.is_valid_hcl("#123abc") == True
    assert day4.is_valid_hcl("123abc") == False


def test_day4_1_given_input(mocker):
    event = get_event_input_raw("day4/input.txt")
    ret = day4.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 254


def test_day3_2_given_input(mocker):
    event = get_event_input_raw("day4/input.txt")
    ret = day4.lambda_handler_2(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["result"] == 184
