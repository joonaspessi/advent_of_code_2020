import json
import math


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day5/input.txt", 'r') as f:
            lines = f.readlines()

    lines = map(lambda n: n.rstrip(), lines)
    return lines


def get_row(row, lower_limit, upper_limit):
    next = row[0]
    if (len(row) > 1):
        mid_limit = int(lower_limit + (1 + upper_limit-lower_limit) / 2)
        if next == "F":
            return get_row(row[1:], lower_limit, mid_limit - 1)
        else:
            return get_row(row[1:], mid_limit, upper_limit)
    else:
        if next == "F":
            return lower_limit
        else:
            return upper_limit


def get_column(column, lower_limit, upper_limit):
    next = column[0]
    if (len(column) > 1):
        mid_limit = int(lower_limit + (1 + upper_limit-lower_limit) / 2)
        if next == "L":
            return get_column(column[1:], lower_limit, mid_limit - 1)
        else:
            return get_column(column[1:], mid_limit, upper_limit)
    else:
        if next == "L":
            return lower_limit
        else:
            return upper_limit


def get_seat_id(row_id, column_id, magic_multiplier=8):
    return row_id * magic_multiplier + column_id


def lambda_handler(event, _context):
    boarding_passes = get_input(event)

    highest_seat_id = 0
    for boarding_pass in boarding_passes:
        row_id = get_row(boarding_pass[:7], 0, 127)
        column_id = get_column(boarding_pass[7:], 0, 7)
        seat_id = get_seat_id(row_id, column_id)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": highest_seat_id
        }),
    }


def lambda_handler_2(event, _context):
    boarding_passes = get_input(event)

    seat_ids = []
    for boarding_pass in boarding_passes:
        row_id = get_row(boarding_pass[:7], 0, 127)
        column_id = get_column(boarding_pass[7:], 0, 7)
        seat_id = get_seat_id(row_id, column_id)
        seat_ids.append(seat_id)
    seat_ids_sorted = sorted(seat_ids)
    min_id = min(seat_ids_sorted)
    max_id = max(seat_ids_sorted)
    seat_range = list(range(min_id, max_id+1))

    missing_seat_id = 0
    for id in seat_range:
        if id not in seat_ids_sorted:
            missing_seat_id = id
            break

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": missing_seat_id
        }),
    }
