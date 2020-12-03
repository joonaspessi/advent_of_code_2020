import json


def lambda_handler(event, context):
    """Advent of code day 4, excercise 1
    """
    body = json.loads(event["body"])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        }),
    }


def lambda_handler_2(event, context):
    """Advent of code day 3, excercise 2
    """
    body = json.loads(event["body"])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        }),
    }
