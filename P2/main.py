def copyWith0s(grid):
    return [[0 for _ in r] for r in grid]


def getOrDefault(grid, i, j, default):
    if i < 0 or i >= len(grid):
        return default

    row = grid[i]
    if j < 0 or j >= len(row):
        return default

    return grid[i][j]


def sumCruxOfSize(cruxSize):
    return 4 * cruxSize + 1


def maxCrux(grid):
    left = copyWith0s(grid)
    right = copyWith0s(grid)
    top = copyWith0s(grid)
    bottom = copyWith0s(grid)

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 1:
                left[i][j] = getOrDefault(left, i, j - 1, 0) + 1
                top[i][j] = getOrDefault(top, i - 1, j, 0) + 1

    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        for j in range(len(row) - 1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = getOrDefault(right, i, j + 1, 0) + 1
                bottom[i][j] = getOrDefault(bottom, i + 1, j, 0) + 1

    max = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            # Skip all 0 cells
            if left[i][j] < 1:
                continue

            currentCruxLength = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
            if currentCruxLength > max:
                max = currentCruxLength

    if max == 1:
        return 0
    else:
        return sumCruxOfSize(max - 1)


print(
    maxCrux(
        [
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        ]
    )
)

print(
    maxCrux(
        [
            [1, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1],
            [0, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 0],
        ]
    )
)
