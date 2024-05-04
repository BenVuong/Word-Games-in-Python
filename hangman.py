from random import randint

def checkLetter(insertChar, target):
    #takes in the character and check if it is in the target word
    #if it is return an array of all of the indexes of where the character is in the target word
        
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



end = False
win = 0
totalGames = 0

while(end == False):
    wordList = []
    turns = 8
    unknownWord = []
    listOfWords = []
    listOfLetterGuessed = []
    f = open("wordList.txt", "r")
    for x in f:
        listOfWords.append(x)
    f.close
    answerIndex = randint(0,len(listOfWords)-1)
    answer=listOfWords[answerIndex]
    answer = answer.strip()


    print("\nWelcome to Hangman")
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
                win+=1
                totalGames+=1
                print("You have won " + str(win) + " out of " + str(totalGames) + " Games")
                userInput = input("Would you like to play again y/n: ")[0]
                if (userInput == "n"):
                    end = True
            else:
                print("You lose")
                print("The word was: " + answer)
                totalGames+=1
                print("You have won " + str(win) + " out of " + str(totalGames) + " Games")
                
                userInput = input("Would you like to play again y/n: ")[0]
                if (userInput == "n"):
                    end = True
        else:
            print("Letters that you have already guessed: ", end=" ")
            for x in listOfLetterGuessed:
                print(x, end=" ")
            print("\n")
            
            userInput = input('Guess a letter that might be in the word:')[0]
            listOfLetterGuessed.append(userInput)
            checkLetter(userInput, answer)
            
            final = "".join(unknownWord)
            if(final == answer):
                print("\n You win" )
                win+=1
                totalGames+=1
                print("You have won " + str(win) + " out of " + str(totalGames) + " Games")
                userInput = input("Would you like to play again y/n: ")[0]
                if (userInput == "n"):
                    end = True
                
                break




