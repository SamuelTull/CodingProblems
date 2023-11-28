# given an array and target
# return the indices of the two numbers that add up to the target
# or return None


def sol_for_loops(arr, target):
    # 2 for loops
    # quadratic time
    # constant space
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None


def sol_pointers(arr, target):
    arr = sorted([(arr[i], i) for i in range(len(arr))], key=lambda x: x[0])
    # nlogn time
    # linear space
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left][0] + arr[right][0] == target:
            return [arr[left][1], arr[right][1]]
        elif arr[left][0] + arr[right][0] > target:
            right -= 1
        else:
            left += 1
    return None


def sol_hash(arr, target):
    # linear time as we only loop through the array once
    # with constant look up time
    S = {}
    for i in range(len(arr)):
        if target - arr[i] in S:
            return [S[target - arr[i]], i]
        else:
            S[arr[i]] = i
    return None


tests = [[[2, 7, 11, 15], 9], [[3, 2, 4], 6], [[3, 3], 6]]


for arr, val in tests:
    print("arr: ", arr, " val: ", val)
    print(sol_for_loops(arr, val))
    print(sol_pointers(arr, val))
    print(sol_hash(arr, val))
    print()
