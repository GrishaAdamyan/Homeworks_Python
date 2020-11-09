# 1
def buildPalindrome(string):
    if string == string[::-1]: # henc skzbic stugum enq polindrom e te che
        return string
    i = 0
    while string[i:] != string[i:][::-1]: # stugum enq te vortexic minchev verj e gtnvum stringi substring polindrom@
        i += 1
    return string + string[i - 1::-1] # entarkum enq konkatenaciayi string@ ev stringi ayn mas@ vor@ chi nerarum substring polindrom@

    #l = 0
    #r = len(string) - 1
    #flag = False
    #while l < r:
        #if string[l] != string[r]:
            #flag = True
            #break
        #else:
            #l += 1
            #r -= 1
    #if flag == False:
        #return string
    #list1 = list(string)
    #for i in range(len(string)):
        #if i != 0 and string[i] == string[-1]:
            #while i - 1 > -1:
                #list1.append(string[i - 1])
                #i -= 1
            #break
    #return ''.join(list1)  


print(buildPalindrome('abaa'))