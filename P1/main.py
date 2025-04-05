keypad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"],
]


def _findCombinations(x, y, n):
    current = keypad[y][x]

    if current == "*" or current == "#" or n == 0:
        return 0
    if n == 1:
        return 1

    center = (x, y)
    top = (x, y - 1)
    bottom = (x, y + 1)
    left = (x - 1, y)
    right = (x + 1, y)

    combinationCount = 0
    match current:
        case "1":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(right[0], right[1], n - 1)
            combinationCount += _findCombinations(bottom[0], bottom[1], n - 1)
        case "2":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(right[0], right[1], n - 1)
            combinationCount += _findCombinations(left[0], left[1], n - 1)
            combinationCount += _findCombinations(bottom[0], bottom[1], n - 1)
        case "3":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(left[0], left[1], n - 1)
            combinationCount += _findCombinations(bottom[0], bottom[1], n - 1)
        case "4":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(top[0], top[1], n - 1)
            combinationCount += _findCombinations(right[0], right[1], n - 1)
            combinationCount += _findCombinations(bottom[0], bottom[1], n - 1)
        case "5" | "8":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(top[0], top[1], n - 1)
            combinationCount += _findCombinations(left[0], left[1], n - 1)
            combinationCount += _findCombinations(right[0], right[1], n - 1)
            combinationCount += _findCombinations(bottom[0], bottom[1], n - 1)
        case "6":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(top[0], top[1], n - 1)
            combinationCount += _findCombinations(left[0], left[1], n - 1)
            combinationCount += _findCombinations(bottom[0], bottom[1], n - 1)
        case "7":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(top[0], top[1], n - 1)
            combinationCount += _findCombinations(right[0], right[1], n - 1)
        case "9":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(top[0], top[1], n - 1)
            combinationCount += _findCombinations(left[0], left[1], n - 1)
        case "0":
            combinationCount += _findCombinations(center[0], center[1], n - 1)
            combinationCount += _findCombinations(top[0], top[1], n - 1)

    return combinationCount


def findCombinations(n):
    out = 0
    for y in range(4):
        for x in range(3):
            out += _findCombinations(x, y, n)
    return out


print(findCombinations(2))
