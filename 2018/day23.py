import src  # My utility functions
import parse

STRING = src.read('\n\n')[0]


def bots_in_range(nanobots, bot):
    x, y, z, r = bot
    return sum(abs(b[0]-x) + abs(b[1]-y) + abs(b[2]-z) <= r for b in nanobots)


def find_coordinate(nanobots):
    bot_ranges = [((x+y+z-r, x+y+z+r),  # Representations of all 8 planes bordering the range as a number
                   (-x+y+z-r, -x+y+z+r),  # One tuple for each pair of parallel planes
                   (x-y+z-r, x-y+z+r),
                   (-x-y+z-r, -x-y+z+r))
                  for x, y, z, r in nanobots]

    def intersect(region1, region2):
        result = ()
        for (p1, q1), (p2, q2) in zip(region1, region2):
            p_max = max(p1, p2)
            q_min = min(q1, q2)
            if p_max > q_min:
                return None
            result += ((p_max, q_min),)
        return result

    max_overlap = 0
    max_regions = {}
    for n, region in enumerate(bot_ranges):
        if n + 1 > len(nanobots) - max_overlap:
            break
        overlap = 0
        for scan in bot_ranges:
            new_region = intersect(region, scan)
            if new_region:
                region = new_region
                overlap += 1
                if overlap > max_overlap:
                    max_overlap += 1
                    max_regions = {region}
                elif overlap == max_overlap:
                    max_regions.add(region)

    min_distance = None
    for region in max_regions:
        furthest_plane = 0
        for p, q in region:
            if p * q > 0:  # Both parallel planes have the same sign
                furthest_plane = max(furthest_plane, min(abs(p), abs(q)))
        if not min_distance:
            min_distance = furthest_plane
        else:
            min_distance = min(min_distance, furthest_plane)
    return min_distance


def main(string=STRING):
    pattern = parse.compile('pos=<{:d},{:d},{:d}>, r={:d}')
    nanobots = [result.fixed for result in pattern.findall(string)]

    print("Part One:")
    strongest_bot = max(nanobots, key=lambda tup: tup[-1])
    ans1 = bots_in_range(nanobots, strongest_bot)  # 326
    print(f"{ans1} nanobots are in range of the strongest one.")

    print("\nPart Two:")
    ans2 = find_coordinate(nanobots)  # 142473501
    print(f"The shortest Manhattan distance with maximum coverage is {ans2}.")
    src.clip(ans2)


if __name__ == '__main__':
    main()
