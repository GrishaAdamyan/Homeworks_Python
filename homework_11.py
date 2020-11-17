# 1
def rotateImage(a):
    b = []
    for i in range(len(a)):
        b.append([])
        for j in range(len(a[i]) - 1, -1, -1):
            b[i].append(a[j][i])
    return b


print(rotateImage([[10,9,6,3,7], 
                   [6,10,2,9,7], 
                   [7,6,3,8,2], 
                   [8,9,7,9,9], 
                   [6,8,6,8,2]]))

# 2
def digitsProduct(product):
    if 0 <= product < 10 and type(product) == int:
        return '1' + str(product)
    else:
        str1 = ''
        tiv = 9
        while product >= 2 and tiv >= 2:
            if product % tiv == 0:
                product /= tiv
                str1 += str(tiv)
            else:
                tiv -= 1
        if product != 1:
            return -1
        return ''.join(reversed(list(str1)))


print(digitsProduct(10))