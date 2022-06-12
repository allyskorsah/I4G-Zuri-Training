import random


exit = False #for when player wants to exit

#loop
while(exit == False):
    game = ["R" , "P" , "S" ]
    CPU = random.choice(game)
    Player = input("Pick a choice R(rock), P(paper), S(scissors) E(exit): ")

    if Player == "R" or Player == "r":
        if CPU == "R" or CPU == "r":
            print("Player Rock : CPU Rock")
            print("It is a Tie") # create loop to go back to start
        
        elif CPU == "P" or CPU == "p":
            print("Player Rock : CPU Paper")
            print("CPU wins")

        elif CPU == "S" or CPU == "s":
            print("Player Rock : CPU Scissors")
            print("Player wins")

    elif Player == "P" or Player == "p":
        if CPU == "R" or CPU == "r":
            print("Player Paper : CPU Rock")
            print("Player wins") 
        
        elif CPU == "P" or CPU == "p":
            print("Player Paper : CPU Paper")
            print("It is a tie") # create loop to go back to start

        elif CPU == "S" or CPU == "s":
            print("Player Paper : CPU Scissors")
            print("CPU wins") 

    elif Player == "S" or Player == "s":
        if CPU == "R" or CPU == "r":
            print("Player Scissors : CPU Rock")
            print("CPU wins") 
        
        elif CPU == "P" or CPU == "p":
            print("Player scissors : CPU Paper")
            print("Player wins")

        elif CPU == "S" or CPU == "s":
            print("Player Scissors : CPU Scissors")
            print("It is a Tie") # create loop to go back to start

    elif Player == "exit" or Player == "E" or Player == "e":
        print("You are exiting game")
        exit = True

    elif Player != "R" or Player != "r" or Player != "P" or Player != "p" or Player != "S" or Player != "s" or Player != "E" or Player != "e" or Player != "exit":
        print("Invalid choice, try again")



