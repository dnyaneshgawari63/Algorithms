def find_sum(list, target):
    left  = 0
    right = len(list) - 1

    while left < right:
        current_sum = list[left] + list[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left = left +1
        else:
            right = right -1
    
    return False

list = [1,2,2,3,4,4,5,5,6,20]
target = 10

if find_sum(list,target):
    print("found")
else:
    print("not found")

