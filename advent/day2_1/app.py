import json


def lambda_handler(event, context):
    """Advent of code day 2, excercise 1
    """

    input = event["body"]["input"]

    count = 0
    for line in input.splitlines():
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
    return {
        "password": "a",
        "required": "a",
        min: 1,
        max: 2
    }


def is_valid_password(password):
    # Get count of required letter in password
    # Check if amount is beyond the given boundaries
    pass
