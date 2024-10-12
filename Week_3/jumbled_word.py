from random import choice,sample
def picked_word():
    words = [
    "apple", "balloon", "journey", "mountain", "rhythm", 
    "galaxy", "breeze", "guitar", "candle", "forest", 
    "ocean", "whisper", "butterfly", "crystal", "eclipse", 
    "shadow", "horizon", "melody", "thunder", "flame", 
    "treasure", "harmony", "puzzle", "spark", "velvet", 
    "lantern", "echo", "fountain", "sunrise", "twilight", 
    "sapphire", "blossom", "storm", "rainbow", "feather", 
    "glacier", "comet", "dragonfly", "island", "oasis", 
    "canyon", "meadow", "phoenix", "coral", "emerald", 
    "waterfall", "snowfall", "desert", "ember", "canyon"
]
    return choice(words)

def jumble(word:str):
    return ''.join(sample(word,len(word)))

def play():
    c1,c2=1,1
    p1=input("Enter your name(Player1): ")
    p2=input("Enter your name(Player2): ")
    p1_score,p2_score,turn =0,0,0

    pkw = picked_word()
    jumbled_word=jumble(pkw)
    print(jumbled_word)
    while(True):
        #player 1
        if turn == 0:
            print("Player1 Turn",p1)
            ans=input("Your Answer: ")
            if ans == pkw:
                p1_score += 1
                print("Correct Answer :)! Your Score:",p1_score)
            else:
                print("Wrong Answer :(! Your Score is:",p1_score)
                print("Correct Answer is:",pkw)
            c1=input("Press 1 to continue and 0 to Quit: ")
            turn = 1
        #player 2
        else:
            print("Player2 Turn",p2)
            ans=input("Your Answer: ")
            if ans == pkw:
                p2_score += 1
                print("Correct Answer :)! Your Score:",p2_score)
            else:
                print("Wrong Answer :(! Your Score is:",p2_score)
            c2=input("Press 1 to continue and 0 to Quit: ")
            turn = 0
        if((c1 == '0' or c2 == '0') and turn == 0): break
    print(f"{p1} score is {p1_score}")
    print(f"{p2} score is {p2_score}")
    print("Thanks for Playing")

if __name__ == "__main__":
    play()