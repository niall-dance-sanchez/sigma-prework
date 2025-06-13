def maxmin(ints):
    max, min = float('-inf'), float('inf')
    for i in range(len(ints)):
        if ints[i] > max:
            max = ints[i]
        if ints[i] < min:
            min = ints[i]
    return [min, max]

print(maxmin([-100, 100]))