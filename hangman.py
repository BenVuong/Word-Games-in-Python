answer = "hello"
turns = 8
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
        print("\n")
    else:
        print("Letter not in word")    
        print("\n")


for i in range(turns):   
    print("\n Turn: " + str(i) + "\n")
    userInput = input('Guess a letter that might be in the word:')[0]
    checkLetter(userInput, answer)
    final = "".join(unknownWord)
    if(final == answer):
        print("\n You win" )
        break
    if i == turns-1:
        print("You lose")
        print("The word was: " + answer)



