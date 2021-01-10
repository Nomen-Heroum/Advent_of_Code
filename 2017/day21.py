import src
import numpy as np
import re
from collections import defaultdict

STRING = src.read('\n\n')[0]
TRANSLATION = str.maketrans('.#/', '01\n')
IMAGE = np.array([[0, 1, 0],
                  [0, 0, 1],
                  [1, 1, 1]])


def build_dict(string=STRING):
    dct = {}
    for tup in re.findall(r'(\S+) => (\S+)', string):
        square, enhancement = [np.genfromtxt(s.translate(TRANSLATION).splitlines(), int, delimiter=1)
                               for s in tup]
        dct[square.tobytes()] = enhancement  # Cast square to bytes to make it hashable
    return dct


ENHANCEMENTS = build_dict()  # Global dictionary for the input data


def iterate_once(image=IMAGE, enhancements=None):
    """Iterates an image once according to the dictionary of enhancements"""
    enhancements = enhancements or ENHANCEMENTS

    size = len(image)
    w = 2 if size % 2 == 0 else 3  # Width of one chunk -> replacements have width w+1
    chunks = size // w  # Number of chunks per axis
    if size == 6:  # In this case we can consider the result to be multiple 3x3 images; we count those
        new_image = defaultdict(int)
    else:  # Otherwise we just return the enhanced image
        new_size = (w + 1) * chunks
        new_image = np.zeros((new_size, new_size), int)  # Blank image to fill with enhancements

    for i in range(chunks):  # Scan the image top to bottom
        x = w * i
        new_x = (w + 1) * i
        for j in range(chunks):  # Left to right
            y = w * j
            new_y = (w + 1) * j
            square = image[x:x+w, y:y+w]
            for oriented in src.orientations(square):
                square_bytes = oriented.tobytes()
                if square_bytes in enhancements:
                    if size == 6:
                        new_image[enhancements[square_bytes].tobytes()] += 1
                    else:
                        new_image[new_x:new_x + w + 1, new_y:new_y + w + 1] = enhancements[square_bytes]
                    break
    return new_image


EXPANSIONS = {}  # Cache for expansions of 3x3 tiles to 9x9 images


def expand(img_bytes) -> dict:
    """Expands a 3x3 image to a 9x9 one and counts the frequency of each 3x3 subsection."""
    if img_bytes in EXPANSIONS:
        return EXPANSIONS[img_bytes]
    else:
        image = np.frombuffer(img_bytes, int).reshape(3, 3)
        expanded = src.repeat(iterate_once, image, 3)  # 3rd iteration returns a dictionary
        EXPANSIONS[img_bytes] = expanded
        return expanded


def iterate(steps, image=IMAGE):
    big_steps, small_steps = divmod(steps, 3)

    counts = {image.tobytes(): 1}
    for _ in range(big_steps):
        new_counts = defaultdict(int)

        for img_bytes, ct in counts.items():
            for sub_bytes, num in expand(img_bytes).items():
                new_counts[sub_bytes] += ct * num

        counts = new_counts

    total = 0
    for img_bytes, ct in counts.items():
        image = np.frombuffer(img_bytes, int).reshape(3, 3)
        total += ct * src.repeat(iterate_once, image, small_steps).sum()

    return total


def main():
    print("Part One:")
    ans1 = iterate(5)  # 136
    print(f"After 5 iterations, {ans1} pixels are on.")

    print("\nPart Two:")
    ans2 = iterate(18)  # 1911767
    print(f"After 18 iterations, it's {ans2}.")
    src.copy(ans2)


if __name__ == '__main__':
    main()
