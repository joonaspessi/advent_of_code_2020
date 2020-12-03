import json
import re


def lambda_handler(event, context):
    """Advent of code day 2, excercise 1
    """

    body = event["body"]
    input = json.loads(body)["input"]

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
