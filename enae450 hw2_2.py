import random
import numpy

array1 = []
N = 101

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

def sortArray(array):
 
 sortedArray = array.sort()

 for i in range(len(array)):
    if i == 0:
     print('Sorted array = [',end='')
     print(array[i], ',', end='')
    elif i == len(array1)-1:
     print(array[i], end='')
     print(']')
     print('')
    else:
     print(array[i], ',', end='')


randArray(array1,N)        

sortArray(array1)

print('Enter an integer value in the range [0,1000] to search for: ', end='')
intValue = input()

try:
    intValue = int(intValue)
except ValueError:
    print('Please enter a valid integer value: ', end='')  
    intValue = input()
    intValue = int(intValue)

while intValue < 0 or intValue >1000:
    print('Please enter a valid integer value: ', end='')  
    intValue = input()
    intValue = int(intValue)

def binarySearch(array, integer):
   currentArray = []
   arrayLength = len(array)
   for i in range(arrayLength):
      currentArray.append(array[i])
   found = False
   while found == False:
      #if arrayLength == 0:
         #print('FALSE')
         #break
      #print('Length of current array is ', end='')
      #print(arrayLength)
      #print('')
      middleIndex = (arrayLength/2)
      #print('Middle index of current array is', middleIndex, ", rounded down to ", end='')
      middleIndex = int(middleIndex)
      #print(middleIndex)
      #print('')
      #print("Middle value is ", currentArray[middleIndex])
      #print('')
      middleElement = currentArray[middleIndex]

      if arrayLength < 2:
        if integer == middleElement:
         print('TRUE')
        else:
         print('FALSE')
        break

      if integer == middleElement:
        print('TRUE')
        found = True

      if integer < middleElement:
        for i in range(middleIndex): #Loop which removes the top half of currentArray including the middle element
           currentArray.pop() #Removes last element of the array
        #for i in range(middleIndex):
           #print(currentArray[i])
        arrayLength = len(currentArray)
       

      if integer > middleElement:
        tempArray = []
        for i in range(middleIndex):
           tempArray.append(currentArray[i]) #Fills the tempArray with bottom half of currentArray
        for i in range(middleIndex):
            currentArray.remove(tempArray[i]) #Removes the values from currentArray that were stored in tempArray
        #for i in range(middleIndex):
            #print(currentArray[i])
        arrayLength = len(currentArray)
        
binarySearch(array1,intValue)
