from itertools import permutations
def permute(nums):
    permutations_list = list(set(permutations(nums)))
    return permutations_list
print(permute([1,2,3]))
