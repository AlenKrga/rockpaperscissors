import random, sys

print("kamen, papir, skare")

#ove varijable ce biljeziti pobjede, poraze i podjednako

wins = 0
losses = 0
ties = 0

while True: #glavna petlja igre
  print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
  while True: #ovo je petlja za igracev unos.
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    playerMove = input()
    if playerMove == "q":
      sys.exit() # Quit the program.
    if playerMove == "r" or playerMove == 'p' or playerMove == "s":
      break # izadji van od igraceve input petlje
    print("Type one of r, p, s or q.")
    # prikaz cega je igrac izabrao:
  if playerMove == 'r':
    print("Rock versus...")
  elif playerMove == "p":
     print("Paper versus...")
  elif playerMove == "s":
     print("Scissors versus...")
  #display random number
  randomNumber = random.randint(1, 3)
  if randomNumber == 1:
    computerMove = "r"
    print("ROCK")
  elif randomNumber == 2:
    computerMove = "p"
    print("PAPER")
  elif randomNumber == 3:
    computerMover = "s"
    print("SCISSORS")
  #display and record w/l/t
  if playerMove == computerMove:
    print("it is a tie!")
    ties = ties + 1
  elif playerMove == "r" and computerMove == "s":
    print("You win!")
    wins = wins + 1
  elif playerMove == "p" and computerMove == "r":
    print("You win!")
    wins = wins + 1
  elif playerMove == "s" and computerMove == "p":
    print("You win!")
    wins = wins + 1
  elif playerMove == "s" and computerMove == "r":
    print("You lose")
    losses = losses + 1
  elif playerMove == "r" and computerMove == "p":
    print("You lose")
    losses = losses + 1
  elif playerMove == "r" and computerMove == "s":
    print("You lose")
    losses = losses + 1
  
