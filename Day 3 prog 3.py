def num_good_pairs(nums): 
  count = 0
  for i in range(len(nums)): 
    for j in range(i + 1, len(nums)): 
      if nums[i] == nums[j]: 
        count += 1
  return count

print(num_good_pairs([1,2,3,1,1,3]))
print(num_good_pairs([1,1,1,1]))
print(num_good_pairs([1,2,3]))
print(num_good_pairs([4,5,1,3,7]))
print(num_good_pairs([1,2,2,3]))
