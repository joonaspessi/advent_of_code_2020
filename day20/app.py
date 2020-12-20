import sys
import re
import json
import fileinput


def get_input(event):
    if "body" in event:
        lines = event["body"]
    else:
        with open(event["fileName"], 'r') as f:
            return f.read()
    return lines


class Tile:
    def __init__(self, id, tiles):
        self.tiles = tiles
        self.id = id
        self.connections = []

    def get_tiles(self):
        return self.tiles

    def get_borders(self):
        top = self.tiles[0]
        right = [row[-1] for row in self.tiles]
        bottom = self.tiles[-1]
        left = [row[0] for row in self.tiles]

        return [top, right, bottom, left]

    def get_all_border_permutations(self):
        borders = self.get_borders()
        permutations = [mirror(b) for b in borders]
        return borders + permutations

    def add_connection(self, tile):
        self.connections.append(tile)
        return self

    def get_connections(self):
        return self.connections

    def rotate(self):
        pass

    def mirror(self):
        pass

    def print(self):
        print(self.id)
        print(20 * "=")
        for row in self.tiles:
            print(row)
        for i, border in enumerate(self.get_borders()):
            print(i, border)


def parse_tiles(input):
    tiles = []
    for tile in input.split("\n\n"):
        tile_array = []
        for i, line in enumerate(tile.splitlines()):
            if i == 0:
                id = int(line.strip()[5:-1])
            else:
                tile_array.append([c for c in line.strip()])

        tiles.append(Tile(id, tile_array))
    return tiles


def print_image(image):
    print(image["id"])
    print(len(image["tile"]) * "=")
    for per in image["permutations"]:
        print("permutation")
        for row in per:
            print(row)


def mirror(row):
    output = list(row[::-1])
    return output


def generate_permutations(images):
    permutations = []
    for image in images:
        image_id = image["id"]
        original = image["tile"]
        mirrored = [mirror(row) for row in original]
        flipped = mirror(original)
        flipped_mirrored = [mirror(row) for row in flipped]
        #image["permutations"] = [original, mirrored, flipped, flipped_mirrored]
        for p in [original, mirrored, flipped, flipped_mirrored]:
            permutations.append({"id": image_id, "tile": p})
    return permutations


def lambda_handler(event, _):
    input = get_input(event)
    tiles = parse_tiles(input)
    print(tiles)
    for tile in tiles:
        tile_borders = tile.get_borders()
        for border in tile_borders:
            for tile2 in tiles:
                if tile != tile2:
                    if border in tile2.get_all_border_permutations():
                        print(tile.id, tile2.id)
                        tile.add_connection(tile2)

    result = 1
    for tile in tiles:
        connections = tile.get_connections()
        print(len(connections))
        if len(connections) == 2:
            result *= tile.id

    print("sum", result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
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


if __name__ == "__main__":
    lambda_handler({"fileName": sys.argv[1]}, {})
