import json
import re


def get_input(event, backup_file_name):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open(backup_file_name, 'r') as f:
            lines = f.readlines()
    return lines


def get_passport_list(input_lines):
    passports = []
    passport = {}
    for line in input_lines:
        line = line.rstrip()
        if line == "":
            passports.append(passport)
            passport = {}
        else:
            attributes = line.split(" ")
            for attribute in attributes:
                line_split = attribute.split(":")
                passport[line_split[0]] = line_split[1]
    passports.append(passport)

    return passports


def is_valid_passport(passport):
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        return True
    return False


def is_valid_byr(byr):
    """ (Birth Year) - four digits; at least 1920 and at most 2002.
    """
    if re.match(r"^(19[2-9]\d|200[0-2])$", byr):
        return True
    return False


def is_valid_iyr(iyr):
    """ (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    if re.match(r"^(201[0-9]|2020)$", iyr):
        return True
    return False


def is_valid_eyr(eyr):
    """ (Expiration Year) - four digits; at least 2020 and at most 2030.
    """
    if re.match(r"^(20[1-2][0-9]|2030)$", eyr):
        return True
    return False


def is_valid_hgt(hgt):
    """ (Height) - a number followed by either cm or in:
        - If cm, the number must be at least 150 and at most 193.
        - If in, the number must be at least 59 and at most 76.
    """
    if re.match(r"^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$", hgt):
        return True
    return False


def is_valid_hcl(hcl):
    """ (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    if re.match(r"^#[0-9a-f]{6}$", hcl):
        return True
    return False


def is_valid_ecl(ecl):
    """ (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    if re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", ecl):
        return True
    return False


def is_valid_pid(pid):
    """ (Passport ID) - a nine-digit number, including leading zeroes.
    """
    if re.match(r"^[0-9]{9}$", pid):
        return True
    return False


def is_valid_passport_strict(passport):
    if not is_valid_passport(passport):
        return False
    if not is_valid_byr(passport["byr"]):
        return False
    if not is_valid_iyr(passport["iyr"]):
        return False
    if not is_valid_eyr(passport["eyr"]):
        return False
    if not is_valid_hgt(passport["hgt"]):
        return False
    if not is_valid_hcl(passport["hcl"]):
        return False
    if not is_valid_ecl(passport["ecl"]):
        return False
    if not is_valid_pid(passport["pid"]):
        return False

    return True


def lambda_handler(event, context):
    """Advent of code day 4, excercise 1
    """
    input_lines = get_input(event, "day4/input.txt")
    passports = get_passport_list(input_lines)

    valid_passports = 0
    for passport in passports:
        is_valid = is_valid_passport(passport)
        if is_valid:
            valid_passports += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": valid_passports
        }),
    }


def lambda_handler_2(event, context):
    """Advent of code day 4, excercise 2
    """
    input_lines = get_input(event, "day4/input.txt")
    passports = get_passport_list(input_lines)

    valid_passports = 0
    for passport in passports:
        is_valid = is_valid_passport_strict(passport)
        if is_valid:
            valid_passports += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": valid_passports
        }),
    }
