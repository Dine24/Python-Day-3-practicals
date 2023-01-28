
def maxJumps(arr): 
    n = len(arr) 
    if (arr[0] == 0): 
        return 1
    jumps = [float('inf')for i in range(n)] 
    jumps[0] = 0
    for i in range(n,1): 
        for j in range(i): 
            if (i <= j + arr[j] and jumps[j] != float('inf')): 
                jumps[i] = max(jumps[i], jumps[j] + 1) 
                break
    if (jumps[n + 1] == float('inf')): 
        return 1
    else: 
        return jumps[n + 1] 
arr = [2,3,0,1,4] 
print( maxJumps(arr)) 
