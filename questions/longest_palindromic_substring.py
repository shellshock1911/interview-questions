"""Given string a, find the longest palindromic substring contained in a.

   ** Taken from Udacity Machine Learning Nanodegree Program **
"""

def LPS(a):
    
    if not a:
        return None
    
    length = 1
    first = 0
    
    for i in xrange(1, len(a)):
        start = i - 1
        end = i
        while start >= 0 and end < len(a) and a[start] == a[end]:
            if end - start + 1 > length:
                first = start 
                length = end - start + 1
            start -= 1
            end += 1
        
        start = i - 1
        end = i + 1
        while start >= 0 and end < len(a) and a[start] == a[end]:
            if end - start + 1 > length:
                first = start
                length = end - start + 1
            start -= 1
            end += 1
    
    return a[first:first + length]

########################################
# Test Cases
########################################

a = ''
print LPS(a)
# Output == None
a = None
print LPS(a)
# Output == None
a = 'a'
print LPS(a) 
# Output == 'a'
a = 'xslhhlst' # Even length
print LPS(a)
# Output = 'slhhls'
a = 'marryhadalittlelamb' # Odd length
print LPS(a)
# Output = 'ada'
a = 'alsdfjalsdjflasjweofiuewoifjjadsjfasdjfosjafoijefioaoghaodhasdofasofdfaso\
asdlfjasdofjaracecarosifjioaejfkayakoiasjdfiosajdfiojeijwoejfaoejfoiawjefoiwjrahawo\
aifjiewjiwhgioaoasddnxncbmadamndbnaghaorgaorghoagdjlfasjiofawiohaoinkxlkjkbjf\
noonasldkjfkasdjldsnboarobhaoiergoargioawrigouarigargaprgupiasrgakgxgjlkl'
print LPS(a)
# Output = 'racecar'