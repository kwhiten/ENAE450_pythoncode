import random


array1 = []
array2 = []
N = 50

def randArray(array, n):
        print("array = [", end='')
        for i in range(n):
            randInt = random.randint(0,1000)
            array.append(randInt)
            if i == n - 1:
                for i in range(n):
                    if i == n - 1:
                        print(array[i], end='')
                    else:
                        print(array[i],',', end='')
            
        print("]")
        print('')

print('First Random Array:')
randArray(array1, N)
print('Second Random Array:')
randArray(array2, N)

arrayMerge = array1 + array2
addedLength = (len(array1) + len(array2))

for i in range(addedLength):
    if i == 0:
     print('Merged array = [',end='')
     print(arrayMerge[i], ',', end='')
    elif i == addedLength-1:
     print(arrayMerge[i], end='')
     print(']')
     print('')
    else:
     print(arrayMerge[i], ',', end='')

sortedArray = arrayMerge.sort()

for i in range(addedLength):
    if i == 0:
     print('Sorted array = [',end='')
     print(arrayMerge[i], ',', end='')
    elif i == addedLength-1:
     print(arrayMerge[i], end='')
     print(']')
     print('')
    else:
     print(arrayMerge[i], ',', end='')
