import random
#Imports the random integer generator

print("Enter the number of your selection, from the following:")
print("1.) Rock")
print("2.) Paper")
print("3.) Scissor")
print("4.) Lizard")
print("5.) Spock")
print("q to quit")
#Outputs the list of potential options

list = ["Bazinga!","Rock","Paper","Scissor","Lizard","Spock"]
#List used to identify the players choices
botwins = 0
playerwins = 0

while True:
  bot = random.randint(1,5)
  #randomly generate an integer for bot's selection.
  print()
  #print("Bot chooses: "+ list[bot]) #dev output test
  
  score = (str(botwins) + " - " + str(playerwins))
  print("Score: " + str(score))
  print()
  player = input("What is your selection? ")

  if player == "q" or player == "Q":
    if botwins > playerwins:
      print("I win! Bazinga")
    if botwins < playerwins:
      print("bortaS bIr jablu'DI' reH QaQqu' nay'!")
    break 

  choice = int(player)
  check = str(bot) + str(player)

  if int(check) == 11 or int(check) == 22 or int(check) == 33 or int(check) == 44 or int(check) == 55:
    print("Dang it! it's a draw.")

  if int(check) == 12 or int(check) == 21:
    print("Paper covers rock")
    if int(check) == 12:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 21:
      print("I win this round")
      botwins = botwins + 1
     
  if int(check) == 14 or int(check) == 41:
    print("Rock crushes lizard")
    if int(check) == 41:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 14:
      print("I win this round")
      botwins = botwins + 1
  
  if int(check) == 23 or int(check) == 32:
    print("Scissors cuts paper")
    if int(check) == 23:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 32:
      print("I win this round")
      botwins = botwins + 1
       
  if int(check) == 45 or int(check) == 54:
    print("Lizard poisons Spock")
    if int(check) == 54:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 45:
      print("I win this round")
      botwins = botwins + 1
  
  if int(check) == 35 or int(check) == 53:
    print("Spock smashes scissors")
    if int(check) == 35:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 53:
      print("I win this round")
      botwins = botwins + 1
  
  if int(check) == 34 or int(check) == 43:
    print("Scissors decapitates lizard")
    if int(check) == 43:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 34:
      print("I win this round")
      botwins = botwins + 1

  if int(check) == 24 or int(check) == 42:
    print("Lizard eats paper")
    if int(check) == 24:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 42:
      print("I win this round")
      botwins = botwins + 1
  
  if int(check) == 25 or int(check) == 52:
    print("Paper disproves Spock")
    if int(check) == 52:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 25:
      print("I win this round")
      botwins = botwins + 1
      
  if int(check) == 15 or int(check) == 51:
    print("Spock vapourizes rock")
    if int(check) == 15:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 51:
      print("I win this round")
      botwins = botwins + 1
  
  if int(check) == 13 or int(check) == 31:
    print("Rock crushes scissors")
    if int(check) == 31:
      print("You win this round")
      playerwins = playerwins + 1
    if int(check) == 13:
      print("I win this round")
      botwins = botwins + 1