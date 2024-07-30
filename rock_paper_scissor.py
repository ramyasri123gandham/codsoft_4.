''' Rock-Paper-Scissors Game
 User Input: Prompt the user to choose rock, paper, or scissors.
 Computer Selection: Generate a random choice (rock, paper, or scissors) for
 the computer.
 Game Logic: Determine the winner based on the user's choice and the
 computer's choice.
 Rock beats scissors, scissors beat paper, and paper beats rock.
 Display Result: Show the user's choice and the computer's choice.
 Display the result, whether the user wins, loses, or it's a tie.
 Score Tracking (Optional): Keep track of the user's and computer's scores for
 multiple rounds.
 Play Again: Ask the user if they want to play another round.
 User Interface: Design a user-friendly interface with clear instructions and
 feedback'''

import random
import string

if __name__=="__main__":
   u_score=0
   c_score=0
   print('\nWelcome to rock-paper-scissors game!\n')
   while True: 
    u=input('Choose one from rock, paper, scissors: ').strip()
    if u not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
    st=['rock', 'paper', 'scissors']
    c=random.choice(st)
    #print(u)
    if u==c:
        print('Tie')
    elif (u== 'rock' and c== 'scissors') or \
        (u== 'scissors' and c== 'paper') or \
        (u== 'paper' and c== 'rock'):
        u_score+=1
        print('Nice! You won!')
    else:
        c_score+=1
        print('You lose!')

    print(f"Scores - You: {u_score}, Computer: {c_score}\n")
        
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Bye!\n")
        break    

