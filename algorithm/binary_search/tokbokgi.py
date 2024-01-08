def cuting(array, x):
    sum = 0
    for i in range(n):
        if x < array[i]:
            sum += (array[i] - x)
    return sum

result = 0
def binary_search(array, target, start, end):
    global result
    if start > end:
        return None
    mid = (start + end) // 2
    if cuting(array, mid) == target:
        result = mid
        return mid
    elif cuting(array, mid) > target:
        result = mid
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid -1)

n, m = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)

binary_search(h, m, 0, h[0])
print(result)
