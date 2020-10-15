# 1
word = input('Enter number ')
list1 = []
while word != 'End':
    list1.append(int(word))
    word = input('Enter number ')
dictionary = {}
for number in list1:
    dictionary[number] = dictionary.get(number, 0) + 1
print(dictionary)

# 2
word = input()
if len(word) % 2 == 0:
    for i in range(len(word)):
        if word.count(word[i]) % 2 == 1:
            print('No')
            break            
    else:
        print('Yes')
else:
    count = 0
    for i in range(len(word)):
        if word.count(word[i]) % 2 == 1:
            count += 1
    if count == 1:
        print('Yes')
    else:
        print('No')