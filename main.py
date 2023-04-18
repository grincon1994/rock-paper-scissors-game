import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

# print player and computer choices, so we can see the choices displayed

#random.randint = chooses a random integer from a list/sequence

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
 

if player_choice >= 3 or player_choice < 0:
  print("Invalid choice, please choose a valid option.")
  
else: 

  print("player chose: ")
  print(options[player_choice])

  computer_choice = random.randint(0, 2)
  
  print("computer chose: ")
  print(options[computer_choice])
  
  if player_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and player_choice == 2:
    print("You Lose!")
  elif computer_choice > player_choice:
    print("You Lose!")
  elif player_choice > computer_choice:
    print("You Win!")
  elif computer_choice == player_choice:
    print("It's a draw")
  










