# read the input from a file called 8.in
txt = open(__file__.split(".")[0] + ".in").read()

# txt = """30373
# 25512
# 65332
# 33549
# 35390"""

# Turn txt into a grid of integers
g = [[int(c) for c in ln] for ln in txt.strip().split("\n")]

# A visible item in a grid is a item
# if all the items between it and the edge of the grid
# are smaller than it
def vis(g, x, y):
    # return True if the item is on the edge of the grid
    if x == 0 or y == 0 or x == len(g[y]) - 1 or y == len(g) - 1:
        return True

    # Check up
    for y2 in range(y):
        if g[y2][x] >= g[y][x]:
            break
    else:
        return True

    # Check down
    for y2 in range(y + 1, len(g)):
        if g[y2][x] >= g[y][x]:
            break
    else:
        return True

    # Check left
    for x2 in range(x):
        if g[y][x2] >= g[y][x]:
            break
    else:
        return True

    # Check right
    for x2 in range(x + 1, len(g[y])):
        if g[y][x2] >= g[y][x]:
            break
    else:
        return True

    return False


# A visible item from a point in the grid
# is an item that is smaller than the point
# and is on the same row, column
# count the number of visible items in each direction from a point
def vis2(g, x, y):
    uc = 0
    for y2 in range(y - 1, -1, -1):
        if g[y2][x] >= g[y][x]:
            uc += 1
            break
        uc += 1

    dc = 0
    # Check down
    for y2 in range(y + 1, len(g)):
        if g[y2][x] >= g[y][x]:
            dc += 1
            break
        dc += 1

    lc = 0
    # Check left
    for x2 in range(x - 1, -1, -1):
        if g[y][x2] >= g[y][x]:
            lc += 1
            break
        lc += 1

    rc = 0
    # Check right
    for x2 in range(x + 1, len(g[y])):
        if g[y][x2] >= g[y][x]:
            rc += 1
            break
        rc += 1

    print(
        f"({x}, {y} => {g[y][x]}) -> u:{uc} d:{dc} l:{lc} r:{rc} = {uc * dc * lc * rc}"
    )

    return uc * dc * lc * rc


# Count the number of visible items in a grid
def count_vis(g):
    c = 0
    for y in range(len(g)):
        for x in range(len(g[y])):
            if vis(g, x, y):
                print(f"Visiable: {g[y][x]} ({x}, {y})")
                c += 1
    return c


# Count the number of visible items from a point in a grid
# Return the result as dictionary
# with the point x, y as the key
# and the number of visible items as the value
def count_vis2(g):
    d = {}
    for y in range(len(g)):
        for x in range(len(g[y])):
            d[(g[y][x], y, x)] = vis2(g, x, y)
    return d


print(max(count_vis2(g).values()))
