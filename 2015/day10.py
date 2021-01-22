import src  # My utility functions
import itertools


SEQUENCE = '3113322113'


def generate_next(sequence):
    new_seq = ''
    for ch, it in itertools.groupby(sequence):
        new_seq += str(len(list(it))) + ch
    return new_seq


def main(sequence=SEQUENCE, iterations=40):
    for i in range(iterations):
        sequence = generate_next(sequence)
    length = len(sequence)
    print(f"The final sequence has length {length}.")
    src.clip(length)


if __name__ == '__main__':
    print("Part One:")
    main()

    print("\nPart Two:")
    main(iterations=50)
