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
        self.connections = [False, False, False, False]
        self.permutation_index = 0

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

    def add_connection(self, tile, index):
        self.connections[index] = tile
        return self

    def get_connections(self):
        return self.connections

    def get_connections_len(self):
        l = 0
        for con in self.connections:
            if con != False:
                l += 1
        return l

    def have_connections_for(self, con):
        connections = [bool(c) for c in self.get_connections()]
        return connections == con

    def rotate(self):
        self.tiles = rotateMatrix(self.tiles)
        return self

    def mirror(self):
        self.tiles = mirror(self.tiles)
        return self

    def permutate(self):
        if self.permutation_index % 4 == 0:
            self.mirror()
        else:
            self.rotate()
        self.permutation_index = (self.permutation_index + 1) % 5
        return self

    def print(self):
        print(self.id)
        print(20 * "=")
        for row in self.tiles:
            print(row)
        # for i, border in enumerate(self.get_borders()):
            # print(i, border)


def strip_tile_borders(tile):
    new_tile = []
    for i, row in enumerate(tile):
        if i == 0:
            continue
        if i == len(tile) - 1:
            continue
        new_tile.append(row[1:-1])
    return new_tile


class Image:
    def __init__(self, tiles):

        for row in tiles:
            print([r.id for r in row])
        image = []
        for i, tile_row in enumerate(tiles):
            tiles = [tile.tiles for tile in tile_row]
            t = strip_tile_borders(tiles[0])
            for tile in tiles[1:]:
                t = combine_tiles(t, strip_tile_borders(tile))
            for row in t:
                image.append(row)
        self.image = image
        print("image", len(image), len(image[0]))
        self.permutation_index = 0

    def rotate(self):
        self.image = rotateMatrix(self.image)
        return self

    def mirror(self):
        self.image = mirror(self.image)
        return self

    def mirror_x(self):
        self.image = mirror(self.image)
        return self

    def mirror_y(self):
        self.image = [mirror(im) for im in self.image]
        return self

    def permutate(self):
        if self.permutation_index % 4 == 0:
            self.mirror()
        else:
            self.rotate()
        self.permutation_index = (self.permutation_index + 1) % 5
        return self

    def find_sea_monster(self):
        size = len(self.image)
        found = 0
        for y in range(0, size - 2):
            for x in range(0, size - 19):
                if self.image[y][x+18] == "#" and \
                        self.image[y+1][x+0] == "#" and \
                        self.image[y+1][x+5] == "#" and \
                        self.image[y+1][x+6] == "#" and \
                        self.image[y+1][x+11] == "#" and \
                        self.image[y+1][x+12] == "#" and \
                        self.image[y+1][x+17] == "#" and \
                        self.image[y+1][x+18] == "#" and \
                        self.image[y+1][x+19] == "#" and \
                        self.image[y+2][x+1] == "#" and \
                        self.image[y+2][x+4] == "#" and \
                        self.image[y+2][x+7] == "#" and \
                        self.image[y+2][x+10] == "#" and \
                        self.image[y+2][x+13] == "#" and \
                        self.image[y+2][x+16] == "#":
                    found += 1
        return found

    def print(self):
        print("image")
        for i in self.image:
            print(i)

    def count_hash(self):
        count = 0
        for y in self.image:
            for x in y:
                if x == "#":
                    count += 1
        return count


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


def rotateMatrix(mat):
    N = len(mat)
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N-1-x]
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
            mat[N-1-y][x] = temp
    return mat


def generate_permutations(images):
    permutations = []
    for image in images:
        image_id = image["id"]
        original = image["tile"]
        mirrored = [mirror(row) for row in original]
        flipped = mirror(original)
        flipped_mirrored = [mirror(row) for row in flipped]
        # image["permutations"] = [original, mirrored, flipped, flipped_mirrored]
        for p in [original, mirrored, flipped, flipped_mirrored]:
            permutations.append({"id": image_id, "tile": p})
    return permutations


def lambda_handler(event, _):
    input = get_input(event)
    tiles = parse_tiles(input)

    for tile in tiles:
        tile_borders = tile.get_borders()
        for i, border in enumerate(tile_borders):
            for tile2 in tiles:
                if tile != tile2:
                    if border in tile2.get_all_border_permutations():
                        tile.add_connection(tile2, i)

    result = 1
    for tile in tiles:
        connections = tile.get_connections_len()
        if connections == 2:
            result *= tile.id

    print("sum", result)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }


def combine_tiles(tile, tile2):
    res = []
    for i, row in enumerate(tile):
        new_row = row + tile2[i]
        res.append(new_row)
    return res


def get_top_left_tile(tiles):
    for tile in tiles:
        print(tile.id, tile.get_connections_len(), [
              bool(x) for x in tile.get_connections()])
        top_left = [False, True, True, False]
        if tile.have_connections_for(top_left):
            return tile


def create_image(top_left_tile):
    left_tiles = []

    t = top_left_tile
    while True:
        left_tiles.append(t)
        if bool(t.get_connections()[2]) == False:
            break
        t = t.get_connections()[2]

    image_tiles = []
    for i, tile in enumerate(left_tiles):
        row = []
        while True:
            row.append(tile)
            if bool(tile.get_connections()[1]) == False:
                break
            tile = tile.get_connections()[1]
        image_tiles.append(row)

    return Image(image_tiles)


def lambda_handler_2(event, _):
    input = get_input(event)
    tiles = parse_tiles(input)
    tile = tiles[0]

    tile_locked = set()
    tiles_to_process = [tiles[0]]
    tiles_processed = []
    processed = 0
    while len(tiles_to_process) > 0:
        print(len(tiles_to_process))
        tile = tiles_to_process.pop(0)
        print(len(tiles_to_process))
        tile_borders = tile.get_borders()
        for i, border in enumerate(tile_borders):
            for tile2 in tiles:
                if tile != tile2:
                    if border in tile2.get_all_border_permutations():
                        while True and tile2.get_connections_len() == 0:
                            tile2.permutate()
                            if border == tile2.get_borders()[(i+2) % 4]:
                                break
                        assert border == tile2.get_borders()[(i+2) % 4]
                        tile.add_connection(tile2, i)
                        if tile2 not in tiles_processed and tile2 not in tiles_to_process:
                            tiles_to_process.append(tile2)
        tiles_processed.append(tile)
        print(processed)
        processed += 1

    top_left_tile = get_top_left_tile(tiles)
    image = create_image(top_left_tile)
    image.print()

    result = 0
    while True:
        image.mirror_x()
        found = image.find_sea_monster()
        if found > 0:
            break
        image.mirror_y()
        found = image.find_sea_monster()
        if found > 0:
            break
        image.mirror_x()
        found = image.find_sea_monster()
        if found > 0:
            break
        image.mirror_y()
        found = image.find_sea_monster()
        if found > 0:
            break
        image.rotate()
        found = image.find_sea_monster()
        if found > 0:
            break

    print("Found", found)

    result = image.count_hash() - found*15
    print("result", result)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": 0
        })
    }


if __name__ == "__main__":
    lambda_handler_2({"fileName": sys.argv[1]}, {})
