import src  # My utility functions
import re

FILE = src.read()[0]


def decompress(file: str, version=1):
    mo = re.search(r'\((\d+)x(\d+)\)', file)
    if mo:
        chars, reps = int(mo[1]), int(mo[2])
        a = mo.start()
        b = mo.end()
        c = b + chars
        if version == 1:
            return a + chars * reps + decompress(file[c:])
        else:
            return a + decompress(file[b:c], 2) * reps + decompress(file[c:], 2)
    else:
        return len(file)


def main(file=FILE):
    print("Part One:")
    ans1 = decompress(file)
    print(f"The decompressed file length is {ans1}.")

    print("\nPart Two:")
    ans2 = decompress(file, version=2)
    print(f"The fully decompressed length is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
