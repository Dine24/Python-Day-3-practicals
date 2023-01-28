from collections import defaultdict
def groupAnagrams(strs):
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())
strs = "banana"
print(groupAnagrams(strs)) 
strs =["a"]
print(groupAnagrams(strs)) 
strs = [""]
print(groupAnagrams(strs)) 
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs)) 
strs = 12345
print(groupAnagrams(strs)) 
