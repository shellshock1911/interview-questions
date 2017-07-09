"""Given two strings s and t, determine whether some anagram of t is a substring of s. """

from collections import Counter

def anagram_substring(s, t):

    if not t or not s:
        return False
    
    t_len, s_len = len(t), len(s)
    
    if t_len > s_len:
        return False
    
    t_count = Counter(t)
    
    for i in range(len(t)):
        char = s[i]
        if char in t_count:
            t_count[char] -= 1
    
    diff = sum(t_count[char] for char in t_count if t_count[char] >= 0)
    
    for i in range(t_len, s_len):
        if diff == 0:
            return True
        else:
            char = s[i - t_len]
            if char in t_count:
                t_count[char] += 1
                if t_count[char] > 0:
                    diff += 1
                else:
                    diff -= 1
            char = s[i]
            if char in t_count:
                t_count[char] -= 1
                diff -= 1
    
    return diff == 0

########################################
# Test Cases
########################################

s, t = '', ''
print anagram_substring(s, t)
# Output == False
s, t = 'foo', ''
print anagram_substring(s, t)
# Output == False
s, t = None, 'bar'
print anagram_substring(s, t)
# Output == False
s, t = 'udacity', 'ad'
print anagram_substring(s, t)
# Output == True
s, t = 'dudacity', 'dad'
print anagram_substring(s, t)
# Output == False
s, t = 'leeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeepap', 'app'
print anagram_substring(s, t)
# Output == True
s, t = 'asdlfajsiojobhrgoiaeioeuweshojnnoasldkfjaasdlkvjjaiojoas', 'johnson'
print anagram_substring(s, t)
# Output == True