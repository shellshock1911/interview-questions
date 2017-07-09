"""Given a string a, find the longest palindromic substring contained in a."""

def LPS(a):
    
    if not a:
        return None
    
    max_length = 1
    
    start = 0
    length = len(a)
    
    low = 0
    high = 0
    
    for i in xrange(1, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and a[low] == a[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
        
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and a[low] == a[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
    
    return a[start:start + max_length]

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