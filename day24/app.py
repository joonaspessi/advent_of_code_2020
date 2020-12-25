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

    tiles = set()

    for path in cmds:
        tile = (0, 0, 0)
        for x, y, z in path:
            tile = (tile[0]+x, tile[1] + y, tile[2] + z)
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)

    for i in range(100):
        tiles_to_check = set()
        new_tiles = set()
        for (x, y, z) in tiles:
            tiles_to_check.add((x, y, z))
            for (dx, dy, dz) in cmd_map.values():
                tiles_to_check.add((x+dx, y + dy, z + dz))
        for x, y, z in tiles_to_check:
            black_count = 0
            for (dx, dy, dz) in cmd_map.values():
                if (x+dx, y + dy, z + dz) in tiles:
                    black_count += 1
            if black_count == 2 and (x, y, z) not in tiles:
                new_tiles.add((x, y, z))
            if black_count in [1, 2] and (x, y, z) in tiles:
                new_tiles.add((x, y, z))
        tiles = new_tiles

    print(len(tiles))
    result = len(tiles)

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
