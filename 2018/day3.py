import src
import numpy as np
import parse

STRINGS = src.read()


def count_overlap(strings, size=1000):
    fabric = np.zeros((size, size), int)
    pattern = parse.compile('#{:d} @ {:d},{:d}: {:d}x{:d}')
    valid_claims = set()
    for s in strings:
        claim_id, left, top, width, height = pattern.parse(s)
        claim = fabric[top:top+height, left:left+width]
        ids = np.unique(claim)
        if ids.any():
            valid_claims -= set(ids)
        else:
            valid_claims.add(claim_id)
        claim[:] = claim_id
    assert len(valid_claims) == 1, f"{len(valid_claims)} valid claims found, 1 expected."
    return (fabric > 1).sum(), valid_claims.pop()


def main(strings=STRINGS):
    ans1, ans2 = count_overlap(strings)
    print("Part One:")
    print(f"There are {ans1} square inches of overlapping instructions.")  # 116489

    print("\nPart Two:")
    print(f"The only non-overlapping claim is #{ans2}.")  # 1260
    src.copy(ans2)


if __name__ == '__main__':
    main()
