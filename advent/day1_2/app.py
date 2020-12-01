import json


def lambda_handler(event, context):
    """Advent of code day 1, excercise 2
    """

    body = json.loads(event["body"])
    report = body["report"]

    entries = []

    for i, ii in enumerate(report):
        for x, xx in enumerate(report):
            for y, yy in enumerate(report):
                if i != x and x != y and ii + xx + yy == 2020:
                    entries = [xx, ii, yy]

    result = entries[0] * entries[1] * entries[2]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "entries": entries,
            "result": result
        }),
    }
