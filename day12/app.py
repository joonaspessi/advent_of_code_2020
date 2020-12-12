import json
import math


def get_input(event):
    if "body" in event:
        lines = event["body"].splitlines()
    else:
        with open("day10/input.txt", 'r') as f:
            lines = f.readlines()
    return [(line[:1], int(line[1:])) for line in lines]


def lambda_handler(event, _):
    instructions = get_input(event)
    dir_to_angle = {"N": 0, "E": 90, "S": 180, "W": 270}
    angle_to_dir = {0: "N", 90: "E", 180: "S", 270: "W"}
    cur_dir = "E"
    movements = {"N": 0, "E": 0, "S": 0, "W": 0}
    for x in instructions:
        if x[0] == "E" or x[0] == "S" or x[0] == "W" or x[0] == "N":
            movements[x[0]] += x[1]
        elif x[0] == "F":
            movements[cur_dir] += x[1]
        elif x[0] == "R":
            new_degree = (dir_to_angle[cur_dir] + x[1]) % 360
            cur_dir = angle_to_dir[new_degree]
        elif x[0] == "L":
            new_degree = (dir_to_angle[cur_dir] - x[1]) % 360
            cur_dir = angle_to_dir[new_degree]

    mov = abs(movements["N"] - movements["S"]) + \
        abs(movements["E"] - movements["W"])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": mov
        }),
    }


def lambda_handler_2(event, _):
    instructions = get_input(event)
    waypoint = [10, 1]
    ship = [0, 0]
    for x in instructions:
        if x[0] == "E":
            waypoint[0] += x[1]
        elif x[0] == "S":
            waypoint[1] -= x[1]
        elif x[0] == "W":
            waypoint[0] -= x[1]
        elif x[0] == "N":
            waypoint[1] += x[1]
        elif x[0] == "F":
            move = list(map(lambda n: n * x[1], waypoint))
            ship = [i + y for i, y in zip(move, ship)]
        elif x[0] == "R" or "L":
            angle = math.radians(
                x[1]) if x[0] == "L" else -1 * math.radians(x[1])
            new_x = round(waypoint[0] * math.cos(angle) -
                          waypoint[1] * math.sin(angle))
            new_y = round(waypoint[0] * math.sin(angle) +
                          waypoint[1] * math.cos(angle))
            waypoint = [new_x, new_y]
        print(f"move={x}, waypoint={waypoint}, ship={ship}")

    manhattan = abs(ship[0]) + abs(ship[1])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": manhattan
        }),
    }
