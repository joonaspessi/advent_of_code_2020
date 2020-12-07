import json
import math


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day5/input.txt", 'r') as f:
            lines = f.readlines()
    return lines


def get_group_declarations(input_lines):
    group = []
    declarations = []
    for line in input_lines:
        line = line.rstrip()
        if line == "":
            flat_group = [item for sub_list in group for item in sub_list]
            distinct_group = set(flat_group)
            declarations.append(distinct_group)
            group = []
            continue
        group.append([char for char in line])

    flat_group = [item for sub_list in group for item in sub_list]
    distinct_group = set(flat_group)
    declarations.append(distinct_group)

    return declarations


def group_answer_2(group):
    answers = [set(answer) for answer in group]
    return set.intersection(*answers)


def get_group_declarations_2(input_lines):
    group = []
    declarations = []
    for line in input_lines:
        line = line.rstrip()
        if line == "":
            declarations.append(group_answer_2(group))
            group = []
            continue
        group.append([char for char in line])

    declarations.append(group_answer_2(group))

    return declarations


def lambda_handler(event, _context):
    """Advent of code day 6, excercise 1
    """
    input_lines = get_input(event)
    declarations = get_group_declarations(input_lines)

    sum = 0
    for declaration in declarations:
        sum += len(declaration)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": sum
        }),
    }


def lambda_handler_2(event, _context):
    """Advent of code day 6, excercise 2
    """
    input_lines = get_input(event)
    declarations = get_group_declarations_2(input_lines)

    sum = 0
    for declaration in declarations:
        sum += len(declaration)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": sum
        }),
    }
