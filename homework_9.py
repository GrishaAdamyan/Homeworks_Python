def buildPalindrome(string):
    l = 0
    r = len(string) - 1
    flag = False
    while l < r:
        if string[l] != string[r]:
            flag = True
            break
        else:
            l += 1
            r -= 1
    if flag == False:
        return string
    list1 = list(string)
    for i in range(len(string)):
        if i != 0 and string[i] == string[-1]:
            while i - 1 > -1:
                list1.append(string[i - 1])
                i -= 1
            break
    return ''.join(list1)


print(buildPalindrome('aa'))
