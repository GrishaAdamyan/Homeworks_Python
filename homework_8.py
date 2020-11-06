# 1
def answer_queries(k, *query_counts):
    count = 1
    list1 = list(query_counts)
    for i in range(len(list1)):
        if i != len(list1) - 1:
            if k >= list1[i]:
                return count
            elif k < list1[i]:
                list1[i + 1] += list1[i] - k
            count += 1
        else:
            if k >= list1[i]:
                return count
            elif k < list1[i]:
                count += (list1[i]) // k
                return count


print(answer_queries(5, 5, 5))

# 2
def non_decreasing_sequence(*nums):
    list1 = list(nums)
    for i in range(len(list1)):
        list1[i] = 0 - list1[i]
        if list1 == sorted(list1):
            return 'Yes', list1
        else:
            list1[i] = 0 - list1[i]
    for i in range(len(list1)):
        for j in range(len(list1)):
            list1[i] = 0 - list1[i]
            list1[j] = 0 - list1[j]
            if list1 == sorted(list1):
                return 'Yes', list1
            else:
                list1[i] = 0 - list1[i]
                list1[j] = 0 - list1[j]
    return 'No'


print(non_decreasing_sequence(1, 1, 0))