import json
import copy


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day10/input.txt", 'r') as f:
            lines = f.readlines()
    input = [list(line.strip()) for line in lines]
    return input


def reserved_seat(y, x, seat_map):
    neighbors = [(0, -1), (1, -1), (1, 0), (1, 1),
                 (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    count_reserved = 0
    for neighbor in neighbors:
        try:
            if not (0 <= y + neighbor[1] < len(seat_map)):
                continue
            if not (0 <= x + neighbor[0] < len(seat_map[0])):
                continue

            if seat_map[y + neighbor[1]][x + neighbor[0]] == "#":
                count_reserved += 1
        except:
            continue
    if count_reserved >= 4:
        return "L"
    return "#"


def unreserved_seat(y, x, seat_map):
    neighbors = [(0, -1), (1, -1), (1, 0), (1, 1),
                 (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    count_reserved = 0
    for neighbor in neighbors:
        try:
            if not (0 <= y + neighbor[1] < len(seat_map)):
                continue
            if not (0 <= x + neighbor[0] < len(seat_map[0])):
                continue
            if seat_map[y + neighbor[1]][x + neighbor[0]] == "#":
                count_reserved += 1
        except:
            continue
    if count_reserved > 0:
        return "L"
    return "#"


def unreserved_seat_2(y, x, seat_map):
    direction = [(0, -1), (1, -1), (1, 0), (1, 1),
                 (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    count_reserved = 0
    for dir in direction:
        reserved = False
        delta_x = dir[0]
        delta_y = dir[1]
        while True:
            try:
                if not (0 <= y + dir[1] < len(seat_map)):
                    break
                if not (0 <= x + dir[0] < len(seat_map[0])):
                    break
                if seat_map[y + dir[1]][x + dir[0]] == "#":
                    reserved = True
                    break
                if seat_map[y + dir[1]][x + dir[0]] == "L":
                    break
            except:
                break
            dir = (dir[0] + delta_x, dir[1] + delta_y)
        if reserved:
            count_reserved += 1
    if count_reserved > 0:
        return "L"
    return "#"


def reserved_seat_2(y, x, seat_map):
    direction = [(0, -1), (1, -1), (1, 0), (1, 1),
                 (0, 1), (-1, 1), (-1, 0), (-1, -1)]

    count_reserved = 0
    for dir in direction:
        reserved = False
        delta_x = dir[0]
        delta_y = dir[1]
        while True:
            try:
                if not (0 <= y + dir[1] < len(seat_map)):
                    break
                if not (0 <= x + dir[0] < len(seat_map[0])):
                    break
                if seat_map[y + dir[1]][x + dir[0]] == "#":
                    reserved = True
                    break
                if seat_map[y + dir[1]][x + dir[0]] == "L":
                    break
            except:
                break
            dir = (dir[0] + delta_x, dir[1] + delta_y)
        if reserved:
            count_reserved += 1
    if count_reserved >= 5:
        return "L"
    return "#"


def seat_state(y, x, seat, seat_map):
    if seat == ".":
        return seat
    if seat == "#":
        return reserved_seat(y, x, seat_map)
    if seat == "L":
        return unreserved_seat(y, x, seat_map)


def seat_state_2(y, x, seat, seat_map):
    if seat == ".":
        return seat
    if seat == "#":
        return reserved_seat_2(y, x, seat_map)
    if seat == "L":
        return unreserved_seat_2(y, x, seat_map)


def lambda_handler(event, _):
    """Advent of code day 11, excercise 1
    """
    seat_map = get_input(event)

    count = 0
    while True:
        count += 1
        seat_map_temp = copy.deepcopy(seat_map)
        for y, row in enumerate(seat_map):
            for x, seat in enumerate(row):
                seat_map_temp[y][x] = seat_state(y, x, seat, seat_map)
        if seat_map_temp == seat_map:
            break
        seat_map = seat_map_temp

    reserved = [seat for row in seat_map for seat in row].count("#")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": reserved
        }),
    }


def lambda_handler_2(event, _):
    """Advent of code day 10, excercise 2
    """
    seat_map = get_input(event)
    count = 0
    while True:
        count += 1
        seat_map_temp = copy.deepcopy(seat_map)
        for y, row in enumerate(seat_map):
            for x, seat in enumerate(row):
                seat_map_temp[y][x] = seat_state_2(y, x, seat, seat_map)
        if seat_map_temp == seat_map:
            break
        seat_map = seat_map_temp
        print(seat_map)

    reserved = [seat for row in seat_map for seat in row].count("#")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": reserved
        }),
    }
