import random
player=["virat","rohit","dhoni","gill","rajat"]
def A(word):
    return random.choice(word)
def B(word,guess):
    return ' '.join([let if let in guess else '_' for let in word])
def C(guess):
    while True:
        g=input("GUESS THE LETTER: ").lower()
        if(len(g)!=1 or not g.isalpha()):
            print("ENTER VALID LETTER.")
        elif g in guess:
            print("YOU HAVE ALREADY GUESSES THAT LETTER.")
        else:
            return g
def D(word,guess):
    return all(let in guess for let in word)
def play():
    word=A(player)
    guess=[]
    chances=len(word)+3
    print("WELCOME TO HANGMAN!!")
    print(f"THE WORD HAS {len(word)} LETTERS.")
    while chances>0:
        print(f"\n YOU HAVE {chances} CHANCES LEFT!!")
        print(B(word,guess))
        g=C(guess)
        guess.append(g)
        if g not in word:
            chances=chances-1
            print(f"WRONG GUESS!! YOU HAVE {chances} CHANCES LEFT.")
        else:
            print("CORRECT GUESS!!")
        if(D(word,guess)):
            print(f"\nCONGRATULATIONS!! YOU HAVE GUESSED THE WORD:{word} ")
            break
    else:
        print(f"\nGAME OVER!! THE WORD IS:{word}:")
if __name__=="__main__":
    play()