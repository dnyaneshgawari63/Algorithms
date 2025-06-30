# def two pointer for sum of any given list 

def find_pair():
    list = [1,2,3,4,5]
    target = 6
    # print(list)
    left = 0
    right = len(list) - 1
    while left < right:
        cur_sum = list[left] + list[right]
        if cur_sum == target:
            print(f"found {list[left]} and {list[right]}")
            break
        elif cur_sum < target:
            left = left + 1
        else:
            right = right - 1

find_pair()


# above problem using class

class Pair:
    def __init__(self):
        self.left = left
        self.right = right
