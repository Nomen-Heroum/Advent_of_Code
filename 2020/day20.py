import src
import numpy as np
import re
from collections import defaultdict
import inspect
import matplotlib.pyplot as plt

BLOCKS = src.read(split='\n\n')  # List with one separate string for each block of text
SNEK_STRING = inspect.cleandoc("""
                                    # 
                  #    ##    ##    ###
                   #  #  #  #  #  #   """).translate(str.maketrans(' #', '01'))
SNEK = np.genfromtxt(SNEK_STRING.splitlines(), delimiter=1) == 1  # Boolean array containing the snek


def tile_dict(blocks: list):
    """Builds a dictionary with entries of the form <ID: tile array> out of the block strings"""
    tiles = {}
    for block in blocks:
        tile_id = int(re.search(r'\d+', block)[0])
        block = block.translate(str.maketrans('.#', '01'))  # Turn the image pieces into 0s and 1s
        tile_array = np.genfromtxt(block.splitlines()[1:], int, delimiter=1)  # Cast it into an array
        tiles[tile_id] = tile_array
    return tiles


def orientations(tile: np.ndarray):
    """Yields all different orientations of a tile"""
    for direction in (1, -1):  # Tile is not flipped/flipped
        for rotation in range(4):  # CCW quarter turns
            yield np.rot90(tile, k=rotation)[:, ::direction]


def edge_dict(tiles: dict):
    """Builds a dictionary counting how often each edge occurs"""
    edges = defaultdict(int)
    for tile in tiles.values():
        for oriented_tile in orientations(tile):
            edge = tuple(oriented_tile[0])  # Top edge of the current orientation
            edges[edge] += 1
    return edges


# Global dicts for the input data
TILES = tile_dict(BLOCKS)
EDGES = edge_dict(TILES)


def find_corners(tiles: dict, edges: dict):
    """Makes a list of IDs of the corner pieces"""
    corners = []
    for tile_id, tile in tiles.items():
        if sum(edges[tuple(o[0])] == 1 for o in orientations(tile)) == 4:  # 4 out of 8 possible edges are unique
            corners.append(tile_id)
    return corners


# Part 2 functions
def build_image(tiles: dict, edges: dict):
    """Builds the total image out of the grids"""
    print("Building image...\r", end='')

    n = len(tiles)
    tiles_wide = int(n**.5)
    assert tiles_wide**2 == n, "Unable to find square dimensions."

    remaining = dict(tiles)  # Dictionary of all tiles that haven't been fit in yet
    corner = find_corners(tiles, edges)[0]  # One of the corner tile IDs
    current_tile = remaining.pop(corner)
    while not edges[tuple(current_tile[0])] == edges[tuple(current_tile[:, 0])] == 1:
        current_tile = np.rot90(current_tile)  # Ensuring the corner is rotated right; no need to flip

    tile_width = current_tile.shape[0] - 2  # Width of each tile in the final image (8)
    total_size = tiles_wide * tile_width  # Size of the final picture
    picture = np.zeros((total_size, total_size), dtype=int)  # Empty array to build the picture in

    def find_fit(edge):
        """Finds the oriented tile that has a certain top edge."""
        for tile_id, tile in remaining.items():
            for oriented_tile in orientations(tile):
                if np.array(oriented_tile[0] == edge).all():
                    remaining.pop(tile_id)  # Remove the fitting tile from the remaining pieces
                    return oriented_tile

    for x in range(0, total_size, tile_width):      # Scanning where the tiles need to go from top to bottom
        for y in range(0, total_size, tile_width):  # Left to right on each line of tiles
            if y == 0:  # First tile in each line
                if x > 0:  # We already have a current_tile for x=0, y=0
                    current_tile = find_fit(bottom_edge)
                bottom_edge = current_tile[-1]
            else:
                current_tile = find_fit(right_edge).T  # Transpose since we need the left edge, not the top
            picture[x:x+tile_width, y:y+tile_width] = current_tile[1:-1, 1:-1]  # Edit the current region
            right_edge = current_tile[:, -1]

    return picture


def roughness(picture: np.ndarray, snek=SNEK):
    """Calculates the roughness of the water"""
    print("Trying to find sneks...\r", end='')

    snek_count = 0
    pic_x, pic_y = picture.shape
    snek_x, snek_y = snek.shape
    max_x = pic_x - snek_x + 1  # Maximum x and y where the top left corner of a snek may be
    max_y = pic_y - snek_y + 1

    for pic in orientations(picture):
        # Identify indices in pic with a 1 below them, so that they may be the top left corner of a snek
        options = np.argwhere(pic[1:max_x + 1, :max_y] == 1)
        for place in options:
            snek_here = True
            for piece in np.argwhere(snek):  # Pieces of the monster
                if pic[tuple(place + piece)] == 0:
                    snek_here = False  # Stop if any piece is missing
                    break
            if snek_here:
                for piece in np.argwhere(snek):
                    pic[tuple(place + piece)] = 2  # Make the snek stand out in the picture
                snek_count += 1
        if snek_count:
            print(f"{snek_count} sneks were counted.")
            plt.imshow(pic)
            return (pic == 1).sum()  # Sneks have a value of 2

    raise EOFError("No orientation found with sneks.")


def main():
    print("Part One:")
    ans1 = np.prod(find_corners(TILES, EDGES))  # 5966506063747
    print(f"The product of corner IDs is {ans1}.")

    print("\nPart Two:")
    picture = build_image(TILES, EDGES)
    ans2 = roughness(picture)  # 1714
    print(f"The roughness of water in this image is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
