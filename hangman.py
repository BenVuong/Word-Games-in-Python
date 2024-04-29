answer = "hello"
unknownWord = []
for i in range(len(answer)):
    unknownWord.append("-")

for i in range(len(unknownWord)):
    print(unknownWord[i], end=" ")


insertChar = "l"
locatArray = []
while(answer.find(insertChar)!=-1):
    locatArray.append(answer.find(insertChar))
    answer=answer.replace(insertChar,"*"*len(insertChar),1)

for i in range(len(locatArray)):
    unknownWord[locatArray[i]]=insertChar
print("\n")
for i in range(len(unknownWord)):
    print(unknownWord[i], end=" ")

