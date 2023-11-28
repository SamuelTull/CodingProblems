from collections import defaultdict

# https://www.youtube.com/watch?v=JvbnQMzOHhI
# fill 4x4 grid with digits 1-9
# each row and column and 2x2 sums to x
# each row and column has unique set of 4 numbers


def printing(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=" ")
        print()


def checkSets(arr, x):
    sets = []
    for row in range(4):
        this_sum = 0
        this_set = 0
        complete = True
        for col in range(4):
            if arr[row][col] == 0:
                complete = False
                break
            this_sum += arr[row][col]
            this_set |= 1 << arr[row][col] - 1
        if complete:
            if this_sum != x:
                return False
            if this_set in sets:
                return False
        sets.append(this_set)
    for col in range(4):
        this_sum = 0
        this_set = 0
        complete = True
        for row in range(4):
            if arr[row][col] == 0:
                complete = False
                break
            this_sum += arr[row][col]
            this_set |= 1 << arr[row][col] - 1
        if complete:
            if this_sum != x:
                return False
            if this_set in sets:
                return False
        sets.append(this_set)
    return True


def checkRow(arr, row, num):
    for c in range(4):
        if arr[row][c] == num:
            return False
    return True


def checkCol(arr, col, num):
    for r in range(4):
        if arr[r][col] == num:
            return False
    return True


def checkSquare(arr, row, col, num):
    start_row = row - row % 2
    start_col = col - col % 2
    s = num
    complete = True
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if i == row and j == col:
                continue
            s += arr[i][j]
            if arr[i][j] == 0:
                complete = False
            elif arr[i][j] == num:
                return False
    if complete and s != x:
        return False
    return True


def isSafe(arr, row, col, num, x):
    return (
        checkRow(arr, row, num)
        and checkCol(arr, col, num)
        and checkSquare(arr, row, col, num)
    )


def solveSudoku(arr, row, col, x):
    if row == 3 and col == 4:
        return True

    if col == 4:
        row += 1
        col = 0

    if arr[row][col] > 0:
        return solveSudoku(arr, row, col + 1, x)

    for num in range(1, 10):
        if isSafe(arr, row, col, num, x):
            arr[row][col] = num
            if checkSets(arr, x) and solveSudoku(arr, row, col + 1, x):
                return True
        arr[row][col] = 0

    return False


def find_poss_x():
    x_combinations = defaultdict(list)

    for i1 in range(1, 10):
        for i2 in range(i1 + 1, 10):
            for i3 in range(i2 + 1, 10):
                for i4 in range(i3 + 1, 10):
                    x = i1 + i2 + i3 + i4
                    x_bit = 1 << i1 - 1 | 1 << i2 - 1 | 1 << i3 - 1 | 1 << i4 - 1
                    x_combinations[x].append(x_bit)

    poss_x = []
    for x in x_combinations:
        if len(x_combinations[x]) >= 8:
            poss_x.append(x)
    return poss_x


def custom_iterable():
    for v1 in range(1, 5):
        for v2 in range(1, 5):
            for x1 in range(1, 10):
                for x2 in range(1, 10):
                    for x in find_poss_x():
                        grid = [[0 for x in range(4)] for y in range(4)]
                        grid[0][0] = v1
                        grid[0][1] = 5 - v1
                        grid[1][2] = v2
                        grid[2][2] = 5 - v2
                        grid[1][1] = 10 - v2
                        grid[0][3] = x1
                        grid[1][3] = 10 - x1
                        grid[2][1] = x2
                        grid[3][1] = 10 - x2
                        yield grid, x


iterable = custom_iterable()
for grid, x in iterable:
    if solveSudoku(grid, 0, 0, x):
        print("Solved")
        printing(grid)
        # assert False
