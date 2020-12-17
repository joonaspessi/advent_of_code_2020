import json
import re


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open("day17/input.txt", 'r') as f:
            lines = f.read()
    return lines


def empty_plane(x_len, y_len):
    p = []
    for y in range(y_len):
        for x in range(x_len):
            p.append(".")
    return p


def lambda_handler(event, _):
    input = get_input(event)
    lines = input.splitlines()
    matrix = []

    for y, line in enumerate(lines):
        matrix.append([[cube] for cube in line])

    x_len = len(matrix[0])
    y_len = len(matrix)

    for round in range(6):
        for y in range(y_len):
            for x in range(x_len):
                matrix[y][x].append(".")

        z_len = len(matrix[0][0][0])

        activate = []
        for y, _ in range(y_len):
            for x, _ in range(x_len):
                for z, _ in range(z_len):
                    active_cubes = 0
                    for yy in [-1, 0, 1]:
                        for xx in [-1, 0, 1]:
                            for zz in [-1, 0, 1]:
                                if xx != 0 and yy != 0 and zz != 0:
                                    if matrix[y+yy][x+xx][z+zz] == "#":
                                        active_cubes += 1
                    if not(2 <= active_cubes <= 3) and matrix[y][x][z] == "#":
                        activate.append([y, x, z, "."])
                    elif matrix[y][x][z] == "." and active_cubes == 3:
                        activate.append([y, x, z, "#"])

        for a in activate:
            y = a[0]
            x = a[1]
            z = a[2]
            state = a[3]
            matrix[y][x][z] = state

    z_len = len(matrix[0][0][0])
    count = 0
    for y, _ in enumerate(y_len):
        for x, _ in enumerate(x_len):
            for z, _ in enumerate(z_len):
                if matrix[y][x][z] == "#":
                    count += 1

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }
