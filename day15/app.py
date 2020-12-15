import json


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open("day12/input.txt", 'r') as f:
            lines = f.read()
    return lines


def lambda_handler(event, _):
    input = get_input(event)
    turns = [int(n) for n in input.split(",")]
    last_lookup = {}

    for i, num in enumerate(turns[:-1]):
        last_lookup[num] = i

    while len(turns) < 2020:
        turn_index = len(turns) - 1
        previous = turns[-1]
        next_val = turn_index - last_lookup.get(previous, turn_index)
        last_lookup[previous] = turn_index
        turns.append(next_val)
    result = turns[-1:]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result[0]
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    turns = [int(n) for n in input.split(",")]
    last_lookup = {}

    for i, num in enumerate(turns[:-1]):
        last_lookup[num] = i

    while len(turns) < 30000000:
        index = len(turns) - 1
        previous = turns[-1]
        next_val = index - last_lookup.get(previous, index)
        last_lookup[previous] = index
        turns.append(next_val)
    result = turns[-1:]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result[0]
        })
    }
