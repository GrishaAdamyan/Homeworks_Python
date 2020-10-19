# 1
n = int(input())
lst = []
for i in range(n):
    name = input("name: ")
    mark = float(input("mark: "))
    lst.append([mark,name])
lst.sort()


i = 0
low = lst[i][0]
while i <= len(lst)-1 and lst[i][0] == low:
    i += 1
    print(lst[i])


need = lst[i][0] 
while i <= len(lst)-1 and lst[i][0] == need:
    print(lst[i][1]) 
    i += 1