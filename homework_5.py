# 1
xmbak = input().split(', ')
list1 = []
for i in range(len(xmbak)):
    list1.append([])
    list1[i].append(input())
i = 0
t = 0
while i < len(list1):
    if int(xmbak[t][-1]) != len(list[i]):
        i += 1
    else:
        i = 0
        t += 1
names = input()










# 2
check_number = 1
list1 = []
list2 = []
def add_item(itemName, itemCost):
    global list1
    global list2
    list1.append(itemName)
    list2.append(itemCost)
    return


def print_receipt():
    global check_number
    if len(list1) == 0:
        return
    print('Check {}. Number of items: {}'.format(check_number, len(list1)))
    for i in range(len(list1)):
        print(list1[i], '-', list2[i])
    print('Total:', sum(list2))
    print('-----')
    check_number += 1
    list1.clear()
    list2.clear()
    return


add_item('Keyboard', 100)
print_receipt()

add_item('Mouse', 70)
print_receipt()
print_receipt()

add_item('Screen', 15)
add_item('Screen', 15)
add_item('Pen', 5)
print_receipt()

add_item('Screen', 15)
add_item('Screen', 15)
# Cancel