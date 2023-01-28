def isMatch(s, p):
  if not p:
    return not s
  first_match = bool(s) and p[0] in {s[0], '.'}
  if len(p) >=2 and p[1] == '*':
    return (isMatch(s, p[2:]) or (first_match and isMatch(s[1:], p)))
  else:
    return first_match and isMatch(s[1:], p[1:])
print(isMatch("aa", "a"))  
print(isMatch("aa", "a*"))  
print(isMatch("ab", ".*"))  
print(isMatch(" aaa", "aa"))  
print(isMatch("aab", "c*a*b"))  
