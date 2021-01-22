import src  # My utility functions
import numpy as np
import matplotlib.pyplot as plt

DIGITS = [int(n) for n in src.read()[0]]


def find_layer(digits, width=25, height=6):
    n = width * height
    min_zeros = n
    best_layer = None
    for layer in (digits[i:i+n] for i in range(0, len(digits), n)):
        zeros = layer.count(0)
        if zeros < min_zeros:
            min_zeros = zeros
            best_layer = layer
    return best_layer.count(1) * best_layer.count(2)


def decode_image(digits, width=25, height=6):
    layers = np.reshape(digits, (-1, height, width))
    image = np.full_like(layers[0], 2)
    for layer in layers:
        undetermined = image == 2
        image[undetermined] = layer[undetermined]
    plt.imshow(image)


def main(digits=None):
    digits = digits or DIGITS

    print("Part One:")
    ans1 = find_layer(digits)  # 2975
    print(f"The checksum of the layer with least zeros is {ans1}.")
    src.clip(ans1)

    print("\nPart Two:")
    decode_image(digits)  # EHRUE
    print("Plotted the image.")


if __name__ == '__main__':
    main()
