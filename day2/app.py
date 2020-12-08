import json
import re


def get_input(event, backup_file_name):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open(backup_file_name, 'r') as f:
            lines = f.readlines()
    return lines


def tokenize_line(line):
    pattern = r'(\d+)-(\d+) (\w): (\w+)'
    return {
        "min": int(re.search(pattern, line).group(1)),
        "max": int(re.search(pattern, line).group(2)),
        "password": re.search(pattern, line).group(4),
        "required": re.search(pattern, line).group(3)
    }


def is_valid_password(password):
    count = password.get("password").count(password.get("required"))
    if count >= password.get("min") and count <= password.get("max"):
        return True
    return False


def is_valid_password_2(password):
    pwd = password.get("password")
    required = password.get("required")
    try:
        index_min = pwd[int(password.get("min")) - 1]
        index_max = pwd[int(password.get("max")) - 1]

        if ((index_max == required and index_min != required) or (index_max != required and index_min == required)):
            return True
        return False
    except:
        return False


def lambda_handler(event, context):
    """Advent of code day 2, excercise 1
    """

    input = get_input(event, "day1/input.txt")

    count = 0
    for line in input:
        print(line)
        password = tokenize_line(line)
        if is_valid_password(password):
            count += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": count
        }),
    }


def lambda_handler_2(event, context):
    """Advent of code day 2, excercise 2
    """

    input = get_input(event, "day1/input.txt")

    count = 0
    for line in input:
        print(line)
        password = tokenize_line(line)
        if is_valid_password_2(password):
            count += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": count
        }),
    }
