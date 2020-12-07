import json


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day1/input.txt", 'r') as f:
            lines = f.readlines()
    return [int(line) for line in lines]


def calculate_result(report):
    entries = (0, 0)
    for i, ii in enumerate(report):
        for x, xx in enumerate(report):
            if i != x and ii + xx == 2020:
                entries = (xx, ii)

    result = entries[0] * entries[1]

    return (result, entries)


def lambda_handler(event, context):
    """Advent of code day 1, excercise 1
    """

    report = get_input(event)
    result, entries = calculate_result(report)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def lambda_handler_2(event, context):
    """Advent of code day 1, excercise 2
    """

    report = get_input(event)
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
            "result": result
        })
    }
