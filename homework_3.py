# 1
n = int(input())
list1 = []
for i in range(n):
    name = input("name: ")
    mark = float(input("mark: "))
    list1.append([mark,name])
list2 = []
for j in range(n):
    list2.append(list1[j][0])
list2.sort()
low = list2.count(list2[0])
i = low
while i <= len(list1)-1 and list2[i] == list2[low]:
    print(list1[i][1])
    i += 1