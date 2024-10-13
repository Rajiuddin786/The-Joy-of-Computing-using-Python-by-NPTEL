from random import choice,sample

movies = [
    "Inception",
    "The Shawshank Redemption",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "The Matrix",
    "Parasite",
    "The Godfather",
    "Fight Club",
    "Interstellar",
    "The Lion King",
    "Gladiator",
    "The Prestige",
    "Avengers: Endgame",
    "Jurassic Park",
    "Schindler's List",
    "Titanic",
    "The Silence of the Lambs",
    "The Lord of the Rings: The Fellowship of the Ring",
    "Star Wars: A New Hope"
]

def generate_question(movie):
    qn=""
    for ch in movie:
        if ch == " ":
            qn += " "
        else:
            qn += "*"
    return qn

def is_present(ch,moive):
    if ch in moive:
        return True
    else:
        return False

def unlock(qn,movie,ch):
    n=len(movie)
    qn=list(qn)
    for i in range(n):
        if movie[i] == ch:
            qn[i] = ch
    return ''.join(x for x in qn)


def play():
    p1name=input("Enter your name Player 1: ")
    p2name=input("Enter your name Player 2: ")

    p1score,p2score=0,0

    turn=0
    while True:
        #Player 1
        if turn == 0:
            print(p1name,"your Turn")
            picked_moive=choice(movies)
            qn=generate_question(picked_moive)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter=input("Your Letter: ")[0]
                if(is_present(letter,picked_moive)):
                    modified_qn=unlock(modified_qn,picked_moive,letter)
                    print(modified_qn)
                    decision = input("Press 1 to Guess the Moive or 2 to Unlock another letter")
                    if decision == 1:
                        movie_name=input("Enter the Movie Name: ")
                        if(movie_name == picked_moive):
                            p1score += 1
                            print("Correct :)\nYour Score is",p1score)
                            not_said = False
                            
                        else:
                            print("Wrong :(\nYour Score",p1score,"\nMovie Name was",picked_moive)    
                            not_said = False
                else:
                    print(letter,"not found\nTry Again")
                    ran_out_of_letter = modified_qn.count('*') == len(modified_qn)
                    if ran_out_of_letter:
                        print("The Movie Name is",picked_moive)
                        not_said=False
            turn = 1
            c1=input("Press 1 to Continue and 0 to Quit")
        #Player 2
        else:
            print(p2name,"your Turn")
            picked_moive=choice(movies)
            qn=generate_question(picked_moive)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter=input("Your Letter: ")[0]
                if(is_present(letter,picked_moive)):
                    modified_qn=unlock(modified_qn,picked_moive,letter)
                    print(modified_qn)
                    decision = input("Press 1 to Guess the Moive or 2 to Unlock another letter")
                    if decision == 1:
                        movie_name=input("Enter the Movie Name: ")
                        if(movie_name == picked_moive):
                            p2score += 1
                            print("Correct :)\nYour Score is",p1score)
                            not_said = False
                            
                        else:
                            print("Wrong :(\nYour Score",p1score,"\nMovie Name was",picked_moive)    
                            not_said = False
                else:
                    print(letter,"not found\nTry Again")
                    ran_out_of_letter = modified_qn.count('*') == len(modified_qn)
                    if ran_out_of_letter:
                        print("The Movie Name is",picked_moive)
                        not_said=False
            turn = 0
            c2=input("Press 1 to Continue and 0 to Quit")
        if (c1 == 0 or c2 == 0) and turn == 0:
            break
    print(p1name,"Score=",p1score)
    print(p2name,"Score=",p2score)
    print("Thanks For Playing")


if __name__ == "__main__":
    play()