list = [10,11,12,13,14,15,16,17,18,19,20]
target  = 25

left = list[0]
right = list[-1]

while left < right:
    cur_sum = left + right
    if cur_sum == target:
        print(f"found {left} and {right}")
        break
    elif cur_sum < target:
        left = left + 1
    else:
        right = right - 1