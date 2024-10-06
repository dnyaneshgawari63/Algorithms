def two_sum_dict(nums, target):
    seen = {}  # Create a dictionary to store seen numbers
    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement needed
        if complement in seen:
            return [seen[complement], i]  # Found a pair
        seen[num] = i  # Store the number and its index
    return None  # No pair found

nums = [1, 2, 3, 4]
target = 5
result = two_sum_dict(nums, target)
print(result)
