def twosum(numbers, target):
    pair = {}

    for x, num in enumerate(numbers):
        diff = target - num
        if diff in pair:
            return [pair[diff], x]
        pair[num] = x

numbers = 12,43,45,5,3,2,43,223,54,23
target = 14
print(twosum(numbers, target))

try:
