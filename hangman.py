from random import randint
wordList = []
turns = 8
unknownWord = []
listOfWords = []



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
        for i in range(len(unknownWord)):
            print(unknownWord[i], end=" ")
        print("\n")


f = open("wordList.txt", "r")
for x in f:
    listOfWords.append(x)
f.close
answerIndex = randint(0,len(listOfWords)-1)
answer=listOfWords[answerIndex]


print("Welcome to Hangman")
print("A random word will be choosen and you will have 8 turns to guess a letter that belongs in that word")
print("On the 8th turn you will have to type in the entire word")
for i in range(len(answer)):
    unknownWord.append("-")
for i in range(len(unknownWord)):
    print(unknownWord[i], end=" ")
for i in range(turns):   
    print("\n Turn: " + str(i+1) + "\n")
    if(i == turns-1):
        userInput = input("Guess the word:")
        if(userInput == answer):
            print("You win")
        else:
            print("You lose")
            print("The word was: " + answer)
    else:
        userInput = input('Guess a letter that might be in the word:')[0]
        checkLetter(userInput, answer)
        final = "".join(unknownWord)
        if(final == answer):
            print("\n You win" )
            break
    



