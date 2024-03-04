import numpy

long_string = ('''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
                aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat!
                Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur?
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.''')
#String is modified to include periods, exclamation marks, and question marks

stringLength = len(long_string)
emptyArray = []
marker = 0
sentenceNumber = 0
for i in range(stringLength):
    if long_string[i] == '.':
        sentenceNumber = sentenceNumber + 1
        emptyArray.append(sentenceNumber)
        emptyArray.append(long_string[marker:i+1])
        marker = i+1
    if long_string[i] == '!':
        sentenceNumber = sentenceNumber + 1
        emptyArray.append(sentenceNumber)
        emptyArray.append(long_string[marker:i+1])
        marker = i+1
    if long_string[i] == '?':
        sentenceNumber = sentenceNumber + 1
        emptyArray.append(sentenceNumber)
        emptyArray.append(long_string[marker:i+1])
        marker = i+1
    

lenEmpty = len(emptyArray)

for i in range(stringLength):
    if i == 0:
        print('Original string: "', end='')
        print(long_string[i], end='')
    elif i == stringLength-1:
        print(long_string[i], '"')
        print('')
    elif i > 0 and i < stringLength-1:
        print(long_string[i], end='')

for i in range(lenEmpty):
    if i == 0:
        print('List of sentences: [ | ' ,end='')
    if i == lenEmpty - 1:
        print(emptyArray[i], "]")
    else:
        print(emptyArray[i], "| ", end='')
        


