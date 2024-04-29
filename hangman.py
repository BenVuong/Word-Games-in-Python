answer = "hello"
unknownWord = []
for i in range(len(answer)):
    unknownWord.append("-")

for i in range(len(unknownWord)):
    print(unknownWord[i], end=" ")

def checkLetter(insertChar, target):
    
    if(target.find(insertChar)!=-1):
        locatArray = []
    
        while(target.find(insertChar)!=-1):
            locatArray.append(target.find(insertChar))
            target=target.replace(insertChar,"*"*len(insertChar),1)    

        for i in range(len(locatArray)):  
            unknownWord[locatArray[i]]=insertChar
        print("\n")
        for i in range(len(unknownWord)):
            print(unknownWord[i], end=" ")
    else:
        print("Letter not in word")    
   
print("\n")
input = input('Guess a letter that might be in the word:')[0]
checkLetter(input, answer)


