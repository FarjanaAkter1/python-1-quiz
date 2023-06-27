def max_values(nums):
    value = sorted(range(len(nums)), key=lambda i: nums[i])[-2:]
    
    
    return value

pass #TODO:






# print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
# print(max_values([-5, -2, -1, -11])) # -> [1, 2]