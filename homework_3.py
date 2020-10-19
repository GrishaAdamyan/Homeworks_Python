# 1
#n = int(input())
#list1 = []
#for i in range(n):
    #name = input("name: ")
    #mark = float(input("mark: "))
    #list1.append([mark,name])
#list1.sort()
#list2 = [list1[j][0] for j in range(n)]
#low = list2.count(list2[0])
#i = low
#while i <= len(list1)-1 and list2[i] == list2[low]:
    #print(list1[i][1])
    #i += 1

# 2
count = 0
superString = input()
subString = input()
list1 = []
string = ''
for i in range(len(superString)):
    if superString[i] in subString and len(subString) - count == 1:
        string += superString[i]
        count = 0
        list1.append(string)
    elif superString[i] in subString:
        string += superString[i]
        count += 1
    else:
        string += superString[i]
list1.sort()
print(list1[0])