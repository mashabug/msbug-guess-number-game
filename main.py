#Number Guessing Game Objectives:
from art import logo
import random

EASY = 10
HARD = 5
#Function to check user's guess against actual answer.
def check_answer(guess, answer, tier):
  if guess > answer:
    print("Too high")
    return tier -1
  if guess < answer:
    print("Too low")
    return tier - 1
  else:
    print("You got it! The answer is {}".format(answer))

#Make function to set difficulty.
def difficulty():
  level = input("Choose your difficulty level. Type 'easy' or 'hard'.\n").lower()
  if level == 'easy':
    return EASY
  if level == 'hard':
    return HARD

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(answer)
  
  tier = difficulty()
 
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print("You have {} attempts to guess.".format(tier))
    guess = int(input("Make your guess: "))
    tier = check_answer(guess, answer, tier)
    if tier == 0:
      print("You are out of guess.")
      return
    elif guess != answer:
      print("Guess again.")
    
game()
