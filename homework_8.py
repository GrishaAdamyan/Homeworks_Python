# 1
def answer_queries(k, *query_counts):
    return (sum(query_counts) // k) + 1


print(answer_queries(1, 100))

# 2
def non_decreasing_sequence(*nums):
    list1 = list(nums)
    for i in range(len(list1)):
        list1[i] = 0 - list1[i]
        if list1 == sorted(list1):
            return 'Yes'
        else:
            list1[i] = 0 - list1[i]
    for i in range(len(list1)):
        for j in range(len(list1)):
            list1[i] = 0 - list1[i]
            list1[j] = 0 - list1[j]
            if list1 == sorted(list1):
                return 'Yes'
            else:
                list1[i] = 0 - list1[i]
                list1[j] = 0 - list1[j]
    return 'No'


print(non_decreasing_sequence(1, 1, 1))