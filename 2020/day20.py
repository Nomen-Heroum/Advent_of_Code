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
SNEK = np.genfromtxt(' '.join(SNEK_STRING).splitlines()) == 1  # Boolean array containing the snek


def tile_dict(blocks: list):
    """Builds a dictionary with entries of the form <ID: tile array> out of the block strings"""
    dct = {}
    for block in blocks:
        key = int(re.search(r'\d+', block)[0])  # Extract the tile ID
        strings = block.split('\n')[1:]
        value = np.array([np.fromstring(','.join(s.translate(str.maketrans('.#', '01'))), dtype=int, sep=',')
                          for s in strings])
        dct[key] = value
    return dct


def orientations(tile: np.ndarray):
    """Yields all different orientations of a tile"""
    for d in (1, -1):  # Tile is not flipped/flipped
        for rot in range(4):  # CCW quarter turns
            yield np.rot90(tile, k=rot)[:, ::d]


def edge_dict(tls: dict):
    """Builds a dictionary counting how often each edge occurs"""
    dct = defaultdict(int)
    for tile in tls.values():
        for ori in orientations(tile):
            edge = tuple(ori[0])
            dct[edge] += 1
    return dct


# Global dicts for the input data
TILES = tile_dict(BLOCKS)
EDGES = edge_dict(TILES)


def find_corners(tls: dict, edg: dict):
    """Makes a list of IDs of the corner pieces"""
    corners = []
    for tile_id, tile in tls.items():
        if sum(edg[tuple(o[0])] for o in orientations(tile)) == 12:  # 8 orientations, 4 have non-unique edges
            corners.append(tile_id)
    return corners


# Part 2 functions
def build_image(tls: dict, edg: dict):
    """Builds the total image out of the grids"""
    print("Building image...")

    n = len(tls)
    size = int(n**.5)
    assert size**2 == n, "Unable to find square dimensions."

    remaining = dict(tls)  # Dictionary of all tiles that haven't been fit in yet
    first = find_corners(tls, edg)[0]  # One of the corner tile IDs
    current_tile = tls[first]
    remaining.pop(first)

    d = current_tile.shape[0] - 2  # Width of each tile in the final image (8)
    total_size = size * d  # Size of the final picture
    picture = np.zeros((total_size, total_size), dtype=int)  # Empty array to build the picture in
    while not edg[tuple(current_tile[0])] == edg[tuple(current_tile[:, 0])] == 1:
        current_tile = np.rot90(current_tile)  # Ensuring the corner is rotated right; no need to flip

    # Function for finding the tile that has a certain top edge
    def find_fit(e):
        for tile_id, tile in remaining.items():
            for ori in orientations(tile):
                if np.array(ori[0] == e).all():
                    remaining.pop(tile_id)  # Remove the fitting tile from the remaining pieces
                    return ori

    for x in range(0, total_size, d):      # Scanning where the tiles need to go from top to bottom
        for y in range(0, total_size, d):  # Left to right on each line of tiles
            if y == 0:  # First tile in each line
                if x > 0:  # We already have a current_tile for x=0, y=0
                    current_tile = find_fit(x_edge)
                x_edge = current_tile[-1]
            else:
                current_tile = find_fit(y_edge).T  # Transpose since we need the left edge, not the top
            picture[x:x+d, y:y+d] = current_tile[1:-1, 1:-1]  # Edit the current region
            y_edge = current_tile[:, -1]

    return picture


def roughness(picture: np.ndarray, snek=SNEK):
    """Calculates the roughness of the water"""
    print("Trying to find sneks...")

    snek_count = 0
    pic_x, pic_y = picture.shape
    snek_x, snek_y = snek.shape

    for pic in orientations(picture):
        options = np.argwhere(pic[1:pic_x - snek_x + 2, :pic_y - snek_y + 1] == 1)  # Indices in pic where a monster
        for place in options:                                                       # might be (have a 1 below them)
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
    assert snek_count, "No orientation found with sneks."


def main():
    print("Part One:")
    ans1 = np.prod(find_corners(TILES, EDGES))
    print(f"The product of corner IDs is {ans1}.")

    print("\nPart Two:")
    picture = build_image(TILES, EDGES)
    ans2 = roughness(picture)
    print(f"The roughness of water in this image is {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
