import random
"""
rock-paper-scissor game
"""
total_input_left=10
no_of_computer_win=0
no_of_human_win=0


print("\t \t \t  r  =  Rock  :   p  =  Paper  :  s =  Scissor (....Enter Q to stop)  \n")

while (total_input_left>0):
    print(f"\n[ Your chance left {total_input_left} ]")
    total_input_left-=1
    player_input = input("Enter Your Choice.......  \n")
    player_input=player_input.lower()
    pc_input = (random.choice(["s","p","k"]))

    if player_input=="q":
        print(".........GAME END.........")
        break

    elif player_input == pc_input:
        print("Both are same !!!!!")

    elif player_input == 'r' and pc_input == 'p':
        print("Computer won.....You lose....!!")
        no_of_computer_win+=1

    elif player_input == 'p' and pc_input == 'r':
        print("You Won !!")
        no_of_human_win+=1

    elif player_input == 'r' and pc_input == 's':
        print("You Won !!")
        no_of_human_win+=1

    elif player_input == 's' and pc_input == 'r':
        print("Computer won.....You lose....!!")
        no_of_computer_win+=1

    elif player_input == 's' and pc_input == 'p':
        print("You Won !!")
        no_of_human_win+=1

    elif player_input == 'p' and pc_input == 's':
        print("Computer won.....You lose....!!")
        no_of_computer_win+=1

    else:
        print("You Entered Wrong input....try again")


print(f"\nComputer score {no_of_computer_win}\n Your score {no_of_human_win}")
