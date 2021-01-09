import src
import numpy as np
import re

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


def iterate(steps=5, image=IMAGE, enhancements=None):
    enhancements = enhancements or ENHANCEMENTS

    def orientations(sq: np.ndarray):
        """Yields all different orientations of a square"""
        for direction in (1, -1):  # Square is not flipped/flipped
            for rotation in range(4):  # CCW quarter turns
                yield np.rot90(sq, k=rotation)[:, ::direction]

    size = len(image)
    for _ in range(steps):
        w = 2 if size % 2 == 0 else 3  # Width of one chunk -> replacements have width w+1
        chunks = size // w  # Number of chunks per axis
        new_size = (w + 1) * chunks
        new_image = np.zeros((new_size, new_size), int)  # Blank image to fill with enhancements

        for i in range(chunks):  # Scan the image top to bottom
            x = w * i
            new_x = (w + 1) * i
            for j in range(chunks):  # Left to right
                y = w * j
                new_y = (w + 1) * j
                square = image[x:x+w, y:y+w]
                for oriented in orientations(square):
                    square_bytes = oriented.tobytes()
                    if square_bytes in enhancements:
                        new_image[new_x:new_x+w+1, new_y:new_y+w+1] = enhancements[square_bytes]
                        break

        image = new_image
        size = new_size
    return image.sum()


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
