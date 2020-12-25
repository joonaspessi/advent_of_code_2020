import json
import sys
from collections import defaultdict
from copy import deepcopy


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


# se, sw, nw, ne, e, w

cmd_map = {
    "e":  (1, -1, 0),
    "se": (0, -1, 1),
    "sw": (-1, 0, 1),
    "w":  (-1, 1, 0),
    "nw": (0, 1, -1),
    "ne": (1, 0, -1),
}


def lambda_handler(event, _):
    input = get_input(event)

    cmds = []
    for line in input.splitlines():
        cmd = []
        print(line)
        while len(line) > 0:
            if line[:2] in {"se", "sw", "nw", "ne"}:
                print(line[:2], cmd_map[line[:2]])
                cmd.append(cmd_map[line[:2]])
                line = line[2:]
            elif line[:1] in {"e", "w"}:
                cmd.append(cmd_map[line[:1]])
                line = line[1:]
            else:
                assert False
        cmds.append(cmd)

    tiles = defaultdict(bool)

    for path in cmds:
        tile = (0, 0, 0)
        for x, y, z in path:
            tile = (tile[0]+x, tile[1] + y, tile[2] + z)
        print(tile)
        tiles[tile] = not tiles[tile]

    result = len(list(filter(lambda n: n == True, tiles.values())))
    print(result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def lambda_handler_2(event, _):
    input = get_input(event)

    cmds = []
    for line in input.splitlines():
        cmd = []
        while len(line) > 0:
            if line[:2] in {"se", "sw", "nw", "ne"}:
                cmd.append(cmd_map[line[:2]])
                line = line[2:]
            elif line[:1] in {"e", "w"}:
                cmd.append(cmd_map[line[:1]])
                line = line[1:]
            else:
                assert False
        cmds.append(cmd)

    tiles = defaultdict(bool)

    for path in cmds:
        tile = (0, 0, 0)
        for x, y, z in path:
            tile = (tile[0]+x, tile[1] + y, tile[2] + z)
        tiles[tile] = not tiles[tile]

    result = len(list(filter(lambda n: n == True, tiles.values())))
    print(f"{result}")
    
    

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


if __name__ == "__main__":
    if len(sys.argv) == 2:
        lambda_handler({"fileName": sys.argv[1]}, {})
    else:
        lambda_handler_2({"fileName": sys.argv[1]}, {})
