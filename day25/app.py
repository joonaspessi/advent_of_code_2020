import json
import sys


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


def get_loop_size(pk):
    loop_size = 1
    subject_number = 7
    value = 1
    while True:
        value = value * subject_number
        value = value % 20201227
        if value == pk:
            break
        loop_size += 1
    return loop_size


def transform(pk, loop_size):
    value = 1
    for _ in range(loop_size):
        value = value * pk
        value = value % 20201227
    return value


def lambda_handler(event, _):
    input = get_input(event)
    card_pk, door_pk = [int(line) for line in input.splitlines()]

    card_loop_size = get_loop_size(card_pk)

    encryption_key = transform(door_pk, card_loop_size)
    print(encryption_key)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": encryption_key
        })
    }


if __name__ == "__main__":
    lambda_handler({"fileName": sys.argv[1]}, {})
