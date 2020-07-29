import os
import sys
import re
from numpy import random

def play(word,indeces):
    # temporary word
    temp = [word[i] if i in indeces else "_" for i in range(len(word))]
    temp = " ".join(temp)
    chances = round(0.6*len(word))*2
    print("\nTry to fill the blanks in atmost {} chances !".format(chances))
    print("\nYour challenge is : {} \t Chances : {}".format(temp,chances))
    while chances:
        if len(indeces) == len(word):
            return True
        letter = input("\nTake a guess on any letter : ")
        letter = re.sub("\n","",letter)
        if letter=="":
            print("\nThat's a wrong guess :(")
        else:
            if letter in word:
                index = word.find(letter)
                if index not in indeces:
                    print("\nThat's a correct guess :)")
                    indeces.append(index)
                    temp = [word[i] if i in indeces else "_" for i in range(len(word))]
                    temp = " ".join(temp)
                else:
                    prev = index+1
                    while index in indeces and index!=-1:
                        index = word.find(letter,prev,len(word))
                        print(index)
                        prev = index+1  
                    if index==-1:
                        print("\nThat's a wrong guess :(")
                    else:
                        print("\nThat's a correct guess :)")
                        indeces.append(index)
                        temp = [word[i] if i in indeces else "_" for i in range(len(word))]
                        temp = " ".join(temp)
            else:
                print("\nThat's a wrong guess :(")
            
        chances -= 1
        print("\n\nWord : {} \t Chances remaining : {}".format(temp,chances))
    if len(indeces) == len(word):
        return True
    return False
     
def main():
    # read the words
    words = open("words.txt","r").readlines()
    words = [re.sub("\n","",word.lower()) for word in words]
    # select a random word    
    word = words[random.randint(0,len(words)-1)]
    # indeces to reveal
    indeces = list(random.choice(len(word),size=round(0.4*len(word)),replace=False))
    # let's play the game
    name = input("\nEnter your name : ")
    print("\nLet's play a guessing game "+name)
    ret = play(word,indeces)
    print("\n\n******************** Result ********************")
    if ret:
        print("\nCongratulations "+name+"! You have won.\n")
    else:
        print("\nSorry "+name+", You have lost.\n")
        print("The word is "+word+"\n")

if __name__ == "__main__":
	main()