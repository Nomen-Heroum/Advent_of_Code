import src

strings = src.read()
data = [int(s) for s in strings]

if data.count(1010) > 1:
    print(f"1010 occurs at least twice; 1010^2 = {1010**2}")

small_nums = [x for x in data if x < 1010]

for x in small_nums:
    if 2020 - x in data:
        print(f"Found {x} and {2020-x}; their product is {x * (2020-x)}.")

print("No more matches found.")

# Part Two
print("\n--- Part Two ---")

for x in small_nums:
    for y in small_nums:
        if 2020 - x - y in data and x <= y:
            print(f"Found {x}, {y} and {2020-x-y}; their product is {x * y * (2020-x-y)}.")

print("No more matches found.")
