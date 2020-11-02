list1 = [1, 4, 6, 5, 7, 10]
def swap_list_elements(list1):
    l = 0
    r = len(list1)-1
    while l < r:
        while l != len(list1) and list1[l] % 2 == l % 2:
            l += 1
        while r != 0 and list1[r] % 2 == r % 2:
            r -= 1
        if l < r:
            list1[l], list1[r] = list1[r], list1[l]
    return list1


print(swap_list_elements(list1))