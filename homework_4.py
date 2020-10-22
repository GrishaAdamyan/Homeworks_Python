# 1
matrix = [['True', 'False', 'False'], 
          ['False', 'True', 'False'],
          ['False', 'False', 'False']]
minesweeper_matrix = [[],[],[]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        count = 0
        if i == 0 and j == 0:
            if matrix[i+1][j] == 'True':
                count += 1
            if matrix[i][j+1] == 'True':
                count += 1
            if matrix[i+1][j+1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i == 0 and j != 0 and j != len(matrix[i])-1:
            if matrix[i][j-1] == 'True':
                count += 1
            if matrix[i+1][j] == 'True':
                count += 1
            if matrix[i+1][j-1] == 'True':
                count += 1
            if matrix[i][j+1] == 'True':
                count += 1
            if matrix[i+1][j+1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i == 0 and j == len(matrix[i])-1:
            if matrix[i][j-1] == 'True':
                count += 1
            if matrix[i+1][j] == 'True':
                count += 1
            if matrix[i+1][j-1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i != 0 and i != len(matrix)-1 and j == 0:
            if matrix[i-1][j] == 'True':
                count += 1
            if matrix[i-1][j+1] == 'True':
                count += 1
            if matrix[i][j+1] == 'True':
                count += 1
            if matrix[i+1][j] == 'True':
                count += 1
            if matrix[i+1][j+1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i != 0 and i != len(matrix)-1 and j != 0 and j != len(matrix[i])-1:
            if matrix[i-1][j] == 'True':
                count += 1
            if matrix[i+1][j] == 'True':
                count += 1
            if matrix[i][j-1] == 'True':
                count += 1
            if matrix[i][j+1] == 'True':
                count += 1
            if matrix[i-1][j-1] == 'True':
                count += 1
            if matrix[i+1][j+1] == 'True':
                count += 1
            if matrix[i-1][j+1] == 'True':
                count += 1
            if matrix[i+1][j-1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i != 0 and i != len(matrix)-1 and j == len(matrix[i])-1:
            if matrix[i-1][j] == 'True':
                count += 1
            if matrix[i-1][j-1] == 'True':
                count += 1
            if matrix[i][j-1] == 'True':
                count += 1
            if matrix[i+1][j] == 'True':
                count += 1
            if matrix[i+1][j-1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i == len(matrix)-1 and j == 0:
            if matrix[i-1][j] == 'True':
                count += 1
            if matrix[i-1][j+1] == 'True':
                count += 1
            if matrix[i][j+1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i == len(matrix)-1 and j != 0 and j != len(matrix)-1:
            if matrix[i][j-1] == 'True':
                count += 1
            if matrix[i-1][j] == 'True':
                count += 1
            if matrix[i-1][j-1] == 'True':
                count += 1
            if matrix[i][j+1] == 'True':
                count += 1
            if matrix[i-1][j+1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
        elif i == len(matrix)-1 and j == len(matrix)-1:
            if matrix[i-1][j] == 'True':
                count += 1
            if matrix[i-1][j-1] == 'True':
                count += 1
            if matrix[i][j-1] == 'True':
                count += 1
            minesweeper_matrix[i].append(count)
print(minesweeper_matrix)


# 2
word = input()
t = 1
start, end = 0, 0 + t
vowels = {}
consonants = {}
while t < len(word):
    if word[start] in 'aeyuio':
        vowels[word[start:end]] = vowels.get(word[start:end], 0) + 1
        start += 1
        end += 1
    elif word[start] not in 'aeyuio':
        consonants[word[start:end]] = consonants.get(word[start:end], 0) + 1
        start += 1
        end += 1
    if end == len(word) + 1:
        t += 1
        start = 0
        end = 0 + t
print(vowels, consonants, sep='\n')