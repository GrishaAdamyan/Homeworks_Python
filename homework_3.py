# 1
#n = int(input())
#list1 = []
#for i in range(n):
    #list1.append([float(input("mark: ")), input("name: ")])
#list1.sort()
#low = [list1[j][0] for j in range(n)].count([list1[j][0] for j in range(n)][0])
#i = low
#while i <= len(list1)-1 and [list1[j][0] for j in range(n)][i] == [list1[j][0] for j in range(n)][low]:
    #print(list1[i][1])
    #i += 1

# 2
superString = input()
subString = list(input())
list1 = []
list2 = []
for i in range(len(superString)):
    if superString[i] in subString:
        list1.append(subString.pop(subString.index(superString[i])))
        k = i
        while k < len(superString):
            if superString[k] in subString:
                list1.append(subString.pop(subString.index(superString[k])))
            k += 1