import json


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open("day17/input.txt", 'r') as f:
            lines = f.read()
    return lines


def lambda_handler(event, _):
    input = get_input(event)
    lines = input.splitlines()

    matrix = set()

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "#":
                matrix.add((y, x, 0))

    max_range = 15  # len(lines) + 6 + 1
    for _ in range(6):
        new_matrix = set()
        for y in range(-max_range, max_range):
            for x in range(-max_range, max_range):
                for z in range(-max_range, max_range):
                    cube_on = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                if dy != 0 or dx != 0 or dz != 0:
                                    if (y + dy, x + dx, z + dz) in matrix:
                                        cube_on += 1
                    if cube_on == 3 and (y, x, z) not in matrix:
                        new_matrix.add((y, x, z))
                    if cube_on in [2, 3] and (y, x, z) in matrix:
                        new_matrix.add((y, x, z))
        matrix = new_matrix

    result = len(matrix)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)
    lines = input.splitlines()

    matrix = set()

    for y, row in enumerate(lines):
        for x, char in enumerate(row):
            if char == "#":
                matrix.add((y, x, 0, 0))

    max_range = len(lines) + 6 + 1
    for _ in range(6):
        new_matrix = set()
        for y in range(-max_range, max_range):
            for x in range(-max_range, max_range):
                for z in range(-max_range, max_range):
                    for w in range(-max_range, max_range):
                        cube_on = 0
                        for dy in [-1, 0, 1]:
                            for dx in [-1, 0, 1]:
                                for dz in [-1, 0, 1]:
                                    for dw in [-1, 0, 1]:
                                        if dy != 0 or dx != 0 or dz != 0 or dw != 0:
                                            if (y + dy, x + dx, z + dz, w + dw) in matrix:
                                                cube_on += 1
                        if cube_on == 3 and (y, x, z, w) not in matrix:
                            new_matrix.add((y, x, z, w))
                        if cube_on in [2, 3] and (y, x, z, w) in matrix:
                            new_matrix.add((y, x, z, w))
        matrix = new_matrix

    result = len(matrix)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }
