import json
import itertools


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day9/input.txt", 'r') as f:
            lines = f.readlines()

    return [int(line) for line in lines]


def get_allowed_numbers(preamble):
    allowed = set()
    for index, number in enumerate(preamble):
        for index2, number2 in enumerate(preamble):
            if index != index2:
                allowed.add(number + number2)
    return allowed


def is_ok_number(preamble_size, index, numbers):
    preamble = numbers[index-preamble_size:index]
    allowed_numbers = get_allowed_numbers(preamble)
    is_allowed = numbers[index] in allowed_numbers
    return is_allowed


def get_list_sum(numbers: int) -> int:
    sum = 0
    for number in numbers:
        sum += number
    return sum


def lambda_handler(event, _):
    """Advent of code day 9, excercise 1
    """
    numbers = get_input(event)
    preamble_size = 25
    for index, number in enumerate(numbers[preamble_size:]):
        if is_ok_number(preamble_size, index + preamble_size, numbers):
            continue
        failed_number = number
        break

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": failed_number
        }),
    }


def lambda_handler_2(event, _):
    """Advent of code day 9, excercise 2
    """
    numbers = get_input(event)
    found = False
    magic_number = 22406676
    for index, _ in enumerate(numbers):
        for index2, _ in enumerate(numbers):
            if index2 + -1 > index:
                sequence = numbers[index:index2]
                sum = get_list_sum(sequence)
                if sum == magic_number:
                    found = True
                    break
                if sum >= magic_number:
                    break
        if found:
            break

    if not found:
        raise Exception("not found")
    encryption_weakness = min(sequence) + max(sequence)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": encryption_weakness
        }),
    }
