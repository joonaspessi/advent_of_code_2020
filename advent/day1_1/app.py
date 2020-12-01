import json


def lambda_handler(event, context):
    """Advent of code day 1, excercise 1
    """

    body = json.loads(event["body"])
    report = body["report"]

    result, entries = calculate_result(report)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result,
            "entries": entries
        }),
    }


def calculate_result(report):
    entries = (0, 0)
    for i, ii in enumerate(report):
        for x, xx in enumerate(report):
            if i != x and ii + xx == 2020:
                entries = (xx, ii)

    result = entries[0] * entries[1]

    return (result, entries)
