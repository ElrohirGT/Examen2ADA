keypad = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"],
]


def addToMemo(memo, digit, n, value):
    if digit not in memo:
        memo[digit] = {}
    memo[digit][n] = value


def _findCombinations(x, y, n, memo):
    current = keypad[y][x]

    if current == "*" or current == "#" or n == 0:
        addToMemo(memo, current, n, 0)
        return 0
    if n == 1:
        addToMemo(memo, current, n, 1)
        return 1

    if current in memo and n in memo[current]:
        print("HIT!")
        return memo[current][n]

    center = (x, y)
    top = (x, y - 1)
    bottom = (x, y + 1)
    left = (x - 1, y)
    right = (x + 1, y)

    combinationCount = 0
    match current:
        case "1":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(right[0], right[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(bottom[0], bottom[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "2":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(right[0], right[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(left[0], left[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(bottom[0], bottom[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "3":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(left[0], left[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(bottom[0], bottom[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "4":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(top[0], top[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(right[0], right[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(bottom[0], bottom[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "5" | "8":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(top[0], top[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(left[0], left[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(right[0], right[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(bottom[0], bottom[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "6":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(top[0], top[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(left[0], left[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(bottom[0], bottom[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "7":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(top[0], top[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(right[0], right[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "9":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(top[0], top[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(left[0], left[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub
        case "0":
            sub = _findCombinations(center[0], center[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

            sub = _findCombinations(top[0], top[1], n - 1, memo)
            addToMemo(memo, current, n - 1, sub)
            combinationCount += sub

    return combinationCount


def findCombinations(n):
    out = 0
    memo = {}
    for y in range(4):
        for x in range(3):
            out += _findCombinations(x, y, n, memo)
    return out


print("combinations(2):", findCombinations(2))
print("combinations(10):", findCombinations(10))
