
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
print(number)

score = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
if score == 'easy':
  score = 10
else:
  score = 5

end_of_game = False
while not end_of_game:
  print(f"You have {score} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  
  if guess != number:
    if guess > number:
      print("Too high.")
    elif guess < number:
      print("Too low.")
    score -= 1
  else:
    if guess == number:
      end_of_game = True
      print("You got it! The answer was {}.".format(number))
  
  if score != 0 and guess != number:
    print("Guess again.")  
  elif score == 0:
    end_of_game = True
    print("You lost. The number was {}.".format(number))
