#Python imports
from random import *
from colorama import Fore as F
from colorama import Style as S
from colorama import Back as B
from time import *
import sys
import os

#Text effect
def char_delay(text, delay):
  for letter in text:
    print(letter, end="")
    sleep(delay)
    sys.stdout.flush()

#Blackjack Functions <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
#Deal the cards
def dealCard(turn):
  card = choice(deck)
  turn.append(card) #Takes the card away that was choosen
  deck.remove(card) #Simply moving a card from one deck to another!

#Calculate the total of each hand
def total(turn):
  total = 0
  face = ['J', 'K', 'Q']
  for card in turn:
    if card in range(1, 11): #Range(1, 11) means 10
      total += card
    elif card in face: #Refer list below
      total += 10
    else: 
      if total > 11:
        total += 1
      else:
        total += 11

  return total

#Check for winner
def revealDealerHand():
  if len(dealerHand) == 2:
    return dealerHand[0]
  elif len(dealerHand) > 2:
    return dealerHand [0], dealerHand[1]
#END OF BLACKJACK FUNCTIONS <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


#War Functions <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
def gameDeck():
  #Nested loop from w3 schools (https://www.w3schools.com/python/python_for_loops.asp)
  Suits = "Hearts", "Diamonds", "Clubs", "Spades" #Suits variable containing each separate string of suits. Separate strings w/ the use of commos.
  for suit in Suits: #Refer above ↖
    for rank in range(2, 15):
      deck.append((rank, suit)) #Store the integer number + string suit in deck using [append()] function. The use of TWO (2) parenthesis are because we want to assign each suit with a number similar to coordinates on a graph.

def displayCard(card):
  #Efficent coding --> minimize lines of code by simply writing the code if a conditional is [true] on the same line followed by the collon [:]
  if card[0] <= 10: cardType = card[0] #If the number is between 1 and 10, then we are simply reassigning the integer to another variable.
  if card[0] == 11: cardType = 'Jack'
  if card[0] == 12: cardType = 'Queen'
  if card[0] == 13: cardType = 'King'
  if card[0] == 14: cardType = 'Ace'
  cardName = str(cardType) + " of " + card[1] #Card[1] refers the the card's suit
  return cardName
  

def drawCard(playerName):
  card = deck[0] #First card from the deck
  deck.remove(deck[0]) #Removes this card from the overall deck so that the next player will not get the same exact card
  if playerName == "CPU":
     print(F.CYAN + "CPU drew the " + displayCard(card) + ".") #Uses the functions first parameter [playerName] to print the user's name when it assigns a card. The 'displayCard(card)' is from the function above and allows for the user to see their card in a more 'prettier' format.
  else: print(F.BLUE + p1Name + " drew the " + displayCard(card) + ".")
  return card #This now returns the variable [card] b/c it is not a global variable
#END OF WAR FUNCTIONS <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

#Tic Tac Toe 👀 Functions <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
'''
Function: Printing the Tic Tac Toe gameGrid every player turn
Paramter: gameGrid in terms of a list
Output --> string text on terminal
'''
def displayBoard(gameGrid):
  print(gameGrid[0] + " | " + gameGrid[1] + " | " + gameGrid[2])
  print("---------")
  print(gameGrid[3] + " | " + gameGrid[4] + " | " + gameGrid[5])
  print("---------")
  print(gameGrid[6] + " | " + gameGrid[7] + " | " + gameGrid[8])

'''
Function: Player input for location of [X] / [O]
Parameters: gameGrid in terms of a list
Output --> string one the terminal depicting where you put the [X] or [Y]
'''
def XorO(gameGrid):
  print(B.RED + S.DIM + "\n<><><>" + B.RESET + S.RESET_ALL)
  inp = int(input("Select a spot 1-9: "))
  print()
  if gameGrid[inp-1] == "-": #[-1] is b/c use of index values for list. The [and] operator serves the function of checking that no player has already inputted a [X] or [O] at the spot in the tic tac toe gameGrid
      gameGrid[inp-1] = turn
  else:
      print("Oops player is already at that spot.")


'''
Function: These will check if there is a winner present. It is broken down into three components: the horizontal, vertical, and diagonal.
Parameters: gameGrid in terms of a string
Output --> boolean True if winner is present
Global variable reference to winner 
'''
def horizontalWinner(gameGrid):
  global gameWinner #[golabl] variable: simple idea that will allow to make changes to the winner variable and if we edit the [gameWinner] variable, then it will also edit/change anywhere else that variable is each time a change occurs! Basically, the variables SCOPE has changed
  if gameGrid[0] == gameGrid[1] == gameGrid[2] and gameGrid[0] != "-":
      gameWinner = gameGrid[0]
      return True #can assign the function to [True]
  elif gameGrid[3] == gameGrid[4] == gameGrid[5] and gameGrid[3] != "-":
      gameWinner = gameGrid[3]
      return True
  elif gameGrid[6] == gameGrid[7] == gameGrid[8] and gameGrid[6] != "-":
      gameWinner = gameGrid[6]
      return True

def verticalWinner(gameGrid):
  global winner
  if gameGrid[0] == gameGrid[3] == gameGrid[6] and gameGrid[0] != "-":
      gameWinner = gameGrid[0]
      return True
  elif gameGrid[1] == gameGrid[4] == gameGrid[7] and gameGrid[1] != "-":
      gameWinner = gameGrid[1]
      return True
  elif gameGrid[2] == gameGrid[5] == gameGrid[8] and gameGrid[2] != "-":
      gameWinner = gameGrid[3]
      return True


def diagonalWinner(gameGrid):
  global winner
  if gameGrid[0] == gameGrid[4] == gameGrid[8] and gameGrid[0] != "-":
      gameWinner = gameGrid[0]
      return True
  elif gameGrid[2] == gameGrid[4] == gameGrid[6] and gameGrid[4] != "-":
      gameWinner = gameGrid[2]
      return True

'''
Function: checks the previous winner functions and their returned boolean values and rules it through conditionals in the function below.
Parameters: gameGrid in terms of a list
Output --> string of '____ is winner'
Global variable reference to gameOn
'''
def winner(gameGrid):
  global gameOn #references variable outside this scoope
  global gameWinner
  if horizontalWinner(gameGrid):
    displayBoard(gameGrid)
    if gameWinner == None:
      gameWinner = "O"
    print(f"The winner is {gameWinner}!")
    os.system('clear')
    gameOn = False
    
    sleep(3)

  elif verticalWinner(gameGrid):
    displayBoard(gameGrid)
    if gameWinner == None:
      gameWinner = "O"
    print(f"The winner is {gameWinner}!")
    os.system('clear')
    gameOn = False
    
    sleep(3)

  elif diagonalWinner(gameGrid):
    displayBoard(gameGrid)
    if gameWinner == None:
      gameWinner = "O"
    print(f"The winner is {gameWinner}!")
    os.system('clear')
    gameOn = False
    
    sleep(3)

'''
Function: Checks the Tic Tac Toe gameGrid if there is a winner present
Parameter: gameGrid in terms of a list
Output --> string 'It's a tie' + end of gameOn loop
Global variable reference to gameOn
'''
def tie(gameGrid):
  global gameOn #references variable outside this scoope
  if "-" not in gameGrid: #if "-" is NOT in the list gameGrid, then ... [https://www.tutorialspoint.com/list-methods-in-python-in-not-in-len-min-max]
      displayBoard(gameGrid)
      print("It is a tie!")
      gameOn = False


'''
Function: Switches player after each round of an [X] being placed onto the Tic Tac Toe  gameGrid
Paramters: N/A
Output --> string assinged to a variable that will used outside of the function therefore...
Global variable [turn] referenced
'''
def pTurn():
  global turn #references variable [turn] that is outside the scope of this function
  if turn == "X":
      turn = "O"
  else:
      turn = "X"

'''
Function: This allows the user to play against the computer. The game is not semiautomated.
Parameters: gameGrid in terms of a list
Output --> the computer player a [X] or [O] on the game gameGrid
'''
def CPUplay(gameGrid):
  while turn == "O":
      position = randint(0, 8)
      if gameGrid[position] == "-":
          gameGrid[position] = "O"
          pTurn()

#END OF MYSTERY GAME FUNCTIONS <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
print(S.BRIGHT)
char_delay("Programmed by Krish Patel & Samuel Dires.", 0.05)
sleep(2) #Time function. Sleeps for 2 seconds

text = True
playAgain = True

while playAgain == True: #Over arching While loop... More on this later
  os.system('clear') #This will clear the terminal every time a new Game is started.
  Blackjack = False
  War = False
  mysteryGame = False
  
  print("--------------------------------------------")
  if text != False:
    text = "New game!"
  else:
    text = "Let's Begin!"
  print(F.WHITE + B.MAGENTA + text + B.RESET)
  print(S.RESET_ALL + B.RESET)
  
  #Introduction to game
  print(F.LIGHTBLUE_EX + "\n")
  char_delay("Welcome to the card simulation game!\n", 0.03)
  sleep(1)
  print(F.RESET)
  p1Name = input("What is your name? ").upper()
  print(f"\nHey {p1Name}. This is a card game simulator that allows you play one of two card games:")
  sleep(1)
  print(S.BRIGHT + B.RESET+ "\n⚫🖤⬛ Blackjack (1) OR\n" + F.MAGENTA + B.RESET + "\n🤜👊🤛 War! (2)\n" + F.RED + "\nAdditionally, you can also select our new MYSTERY GAME 👀👀👀👀\n" + F.WHITE + S.RESET_ALL)
  sleep(2)
  
  gameType = input(B.BLUE +F.WHITE+ "Would you like to play " + p1Name + "? BLACKJACK [1], War [2], OR the MYSTERY GAME 👀 [3]?" + B.RESET + " ").lower()
  print(F.RESET + B.RESET)
  os.system('clear')
  sleep(.2)
  
  gameTypeInput = True
  while gameTypeInput == True:
    if gameType == "blackjack" or gameType == "1":
      char_delay("Excellent. Blackjack it is!", .1)
      sleep(2)
      Blackjack = True
      gameTypeInput = False
    elif gameType == 'war' or gameType == '2':
      char_delay("WAR TIMEEE!!\n", .1)
      sleep(2)
      War = True
      gameTypeInput = False
    elif gameType == "mystery" or gameType == "mystery game" or gameType == "3":
      print(S.BRIGHT)
      char_delay("Let's play the mystery game 💥", .1)
      print(S.RESET_ALL)
      sleep(2)
      mysteryGame = True
      gameTypeInput = False
    elif gameType != ('blackjack' or 'war' or '1' or '2' or 1 or 2): 
      gameType = input('This is not an acceptable response. Try entering a [1] for Blackjack or [2] for War. ')
      os.system('clear')
      continue

  #Start of Code
  
#⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛ BLACKJACK GAME CODE ⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛
  if Blackjack == True:
    sleep(.02)
    print(f"\n\nBLACKJACK GAME SPECIFICCATIONS:\n" + F.BLUE + S.BRIGHT + "To beat the dealer...\n" + F.RESET + S.RESET_ALL + "🟨 Draw a hand value that is higher than the dealer's hand value.\n🟥 By the dealer drawing a hand value that goes over 21\n🟦 By drawing a hand value of 21 on your first two cards, when the dealer does not\n\n" + F.RED + S.BRIGHT + "To lose to the dealer...\n" + F.RESET + S.RESET_ALL + "⬜ Your hand value exceeds 21\n🟪 The dealers hand has a greater value than yours at the end of the round\n\n" + F.CYAN + "🟧 Remember, cards 1-10 are worth their face value, Jack's, Queen's and King's are worth 10, and Aces are worth 11 or 1.\n" + F.MAGENTA + "For more on the rules, visit: https://www.blackjackapprenticeship.com/how-to-play-blackjack/"  + F.RESET + "\n")
    sleep(2.5)

    pScore_blackjack = 0
    CPUscore_blackjack = 0
    
    playerIn = True
    dealerIn = True

    #Initial points + points variable introduction
    playerPoints = 0
    dealerPoints = 0
    
    print(f"Note: X represents a unrevealed card from the dealer's collection.\n")
    sleep(.2)
    print("\nHere we go!")
    blackjackRounds = int(input(B.BLUE+"How many rounds of blackjack would you like to play? Please enter only a numerical value!" + B.RESET + " "))
    sleep(0.24)
    #Deck of Cards / Player dealer hand
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
    playerHand = [] #Empty initial list
    dealerHand = []
    playerHand.clear() and dealerHand.clear() #clears anything and everything from the list above
    
    
    while blackjackRounds > 0:  
      #Game loop
      for tommy in range(2):
        dealCard(dealerHand)
        dealCard(playerHand)
      
      while playerIn or dealerIn:
        print(F.BLUE)
        print(f"➭ Dealer has {revealDealerHand()} and X") #X is because we do not want to reveal EVERYTHING.
        print(F.CYAN)
        print(f"➭ You have {playerHand} for a total of {total(playerHand)}\n")
        if playerIn: #Makes sure playerIn = True
          stayOrHit = input(F.GREEN + '1: Stay\n' + F.RED + '2: Hit\n' + F.RESET) #User can input, or ENTER, '1' to stay or '2' to hit!
        if total(dealerHand) > 16:
          dealerIn = False
        else:
          dealCard(dealerHand) #uses the function dealerCard and then shuffles, adds, and then removes a card to the dealerHand, or the dealer's collection
        if stayOrHit == '1' or stayOrHit == 'stay' or stayOrHit == 'Stay': #from user input
          playerIn = False #Use of boolean based on the input
        else: #Hit
          dealCard(playerHand) #transfer
        #Conditional for winner; breaks, or ends, the while loop
        if total(playerHand) >= 21: 
          break
        elif total(dealerHand) >= 21:
          break
  
      print(F.RESET + S.RESET_ALL + B.RESET)
      End_of_game_output = "You have " + str(playerHand) + " for a total of " + str(total(playerHand)) + " and the dealer has " + str(dealerHand) + " for a total of " + str(total(dealerHand))
      
      
      if total(playerHand) == 21:
        print(End_of_game_output, "\nBlackjack! You win this round!")
        sleep(2)
        blackjackRounds -= 1
        pScore_blackjack += 1
        playerHand.clear()
        dealerHand.clear()
        playerIn = True
        
        
      elif total(dealerHand) == 21:
        print(End_of_game_output)
        print(f"Blackjack! Dealer wins this round!")
        sleep(2)
        blackjackRounds -= 1
        CPUscore_blackjack += 1
        playerHand.clear()
        dealerHand.clear()
        playerIn = True
        
      
      elif total(dealerHand) and total(playerHand) == 0:
        print(End_of_game_output)
        print(f"Blackjack! Dealer wins this round because ties provide the upper hand to the dealer.")
        sleep(2)
        blackjackRounds -= 1
        CPUscore_blackjack += 1   
        playerHand.clear()
        dealerHand.clear()
        playerIn = True
        
        
      elif total(playerHand) > 21:
        print(End_of_game_output)
        print(f"You bust! Dealer wins this round!")
        sleep(2)
        blackjackRounds -= 1
        CPUscore_blackjack += 1
        playerHand.clear()
        dealerHand.clear()
        playerIn = True
        
        
      elif total(dealerHand) > 21:
        print(End_of_game_output)
        print(f"Dealer busts! You win this round!")
        sleep(2)
        blackjackRounds -= 1
        pScore_blackjack += 1
        playerHand.clear()
        dealerHand.clear()
        playerIn = True
        
      
      elif 21 - total(dealerHand) < 21 - total(playerHand):
        print(End_of_game_output)
        print(f"Dealer wins this round!")
        sleep(2)
        blackjackRounds -= 1
        CPUscore_blackjack += 1
        playerHand.clear()
        dealerHand.clear()
        playerIn = True
        
      
      elif 21 - total(dealerHand) > 21 - total(playerHand):
        print(End_of_game_output)
        print(f"You win this round!")
        sleep(2)
        blackjackRounds -= 1
        pScore_blackjack += 1
        playerHand.clear()
        dealerHand.clear()
        playerIn = True

    if blackjackRounds == 0:
      print(F.MAGENTA + S.DIM + "\n----------------------\n" + F.RESET + S.RESET_ALL)
      if pScore_blackjack > 1: points = "points"
      else: points = "point"
      endOfGameScoreOutput = p1Name + ", you have " + str(pScore_blackjack) + " " + points + " while the dealer has " + str(CPUscore_blackjack) + " " + points + "."
      if pScore_blackjack > CPUscore_blackjack:
        print(endOfGameScoreOutput)
        print(f"\nCongrulations {p1Name}!! You have won this game of blackjack!!")
      else:
        print(endOfGameScoreOutput)
        print(f"\nYou lose.🙁🙁 Dealer wins this game of blackjack!")
      playAgain_q = input(F.RED + S.BRIGHT + "\nWould you like to play again? Possibily another game? [Yes] or [No]?" + F.RESET + " ").lower()
      if playAgain_q == 'yes' or playAgain_q == 'sure' or playAgain_q == 'why not' or playAgain_q == 'ig' or playAgain_q == 'of course' or playAgain_q == 'ofc' or playAgain_q == 'yess' or playAgain_q == 'ye': 
        print("Yay!! Let's play again!!! 🙃🙃")
        playAgain = True
      else:
        print(f"No worries! 😊 We're glad you tried out our game {p1Name}")
        print(f"Thanks!\n-- iCards")
        playAgain = False
          
  
#⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛ BLACKJACK ⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛⚫🖤⬛

#😡​😠​👊​⚔️​🛡️​😠​😡​😠​👊​⚔️​🛡️​😠 WAR 😡​😠​👊​⚔️​🛡️​😠​😡​😠​👊​⚔️​🛡️​😠
  if War == True: 
    winner = False
    #Intial code
    deck = [] #Empty list
    p1Score, p2Score, p1Cookies, p2Cookies = 0, 0, 0, 0
    #Introduction
    print("\nWar card game rules: Both players place the top card of their deck onto the center of the table. The player whose card is higher in value takes both cards and places them in a separate pile next to their deck. Once a player runs out of cards in their deck, they shuffle all of the cards in their win pile and continue to play.\n" +F.MAGENTA + "Need more help, visit: https://playingcarddecks.com/blogs/how-to-play/war-game-rules\n")
    print(F.RESET + "In this game of war, you will enter the number of rounds you want to play. At the end of each round, the CPU player or you will recive +50 cookies if you win!!! At the end of all the rounds, you will get a total cookie amount and the player with the greatest wins!")
    warRounds = input(F.RED + "\n\nHow many rounds would you like to play?" + F.RESET + " ")
    os.system('clear')
    warRounds = int(warRounds)
    while warRounds > 0:

        
      #Making the deck
      gameDeck()
      
      #Shuffle deck
      shuffle(deck) #From imported random module, use shuffle function to mix cards.
      
      #every turn loop
      while len(deck) != 0:
        #Drawing cards for each player
        p1_card = drawCard(p1Name) #Player 1's card. Uses [drawCard] function with the string parameter ["Krish"].
        p2_card = drawCard("CPU")
        #Winner
        if p1_card[0] > p2_card[0]: #We must us the index value [0] to check the first item from the card, which is an integer that can be compared.
          winner = p1Name
          p1Score += 2
        elif p1_card[0] < p2_card[0]:
          winner = "CPU"
          p2Score += 2
        else:
          winner = "No one"
        print(F.RESET + winner + " wins.\n\n")
        #Tiebreaker
        
        #Conditional for empty deck
        if len(deck) == 0:
          print("Game over. Deck is empty.")
          print(f"{p1Name}: {p1Score} points.")
          print(f"CPU: {p2Score} points.")
          if p1Score > p2Score:
            print(f"The winner is... {p1Name}❗")
            print("Because " + p1Name + " won, they recieve 50 cookie points as a reward for this round!")
            p1Cookies += 50
            warRounds = warRounds - 1
          else: 
            print(f"The winner is... CPU❗")
            print("Because the CPU won this round, they recieve 50 cookie points as a reward")
            p2Cookies += 50
            warRounds = warRounds - 1

          if warRounds == 0:
            if p1Cookies > p2Cookies:
              print(p1Name + " you win b/c you have more cookie points than the CPU player.")
              break
              playAgain = False
            else:
              print("CPU wins b/c it had more cookie points than you.")
      if warRounds == 0:
        end = input("Would you like to play again? Another game? [Yes] or [No]? ").lower()
        if end == 'yes':
          playAgain = True
        if end == 'no':
          print('No worries! See ya next time!')
          os.system('clear')
          playAgain = False
          break
          
            



#😡​😠​👊​⚔️​🛡️​😠​😡​😠​👊​⚔️​🛡️​😠 WAR 😡​😠​👊​⚔️​🛡️​😠​😡​😠​👊​⚔️​🛡️​😠

#👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀 MYSTERY GAME 👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀
  if mysteryGame == True: 
    #<><><><><><><><><><><><><><><><><><> MAIN CODE <><><><><><><><><><><><><><><><><><>
    char_delay("AND NOW FOR THE MYSTERY GAME... (drumroll please!!) TIC TAC TOE❗", .15)
    print(S.DIM + "\n\nIn addition to iCards card game's, the company has decided to test other products out... starting with Tic Tac Toe!" + S.RESET_ALL)
    sleep(2)
    print(S.BRIGHT + "Here are the rules: " + S.DIM + "\n1. The game is played on a grid that's 3 squares by 3 squares.\n2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie." + S.BRIGHT + "\n\nStill confused? Check out: " + S.DIM + F.BLUE + "https://www.exploratorium.edu/brain_explorer/tictactoe.html" + S.RESET_ALL + "\n")
    print(F.RESET)
    sleep(7)
    os.system('clear')
    print(S.BRIGHT)
    char_delay("Here we go!", .02)
    print(S.RESET_ALL)
    '''
    Purpose: Create a list and assign it to a variable called [gameGrid].
    This list will help us check for which spots are avialable and which spots have a X/O in them.
    '''
    gameGrid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    
    turn = "X" #We will reference who's turn it is in terms of [X] and [O]
    
    gameWinner = None
    gameOn = True
    
    while gameOn: #game loop;
      displayBoard(gameGrid) #Argument/Parameter is the list [gameGrid]
      XorO(gameGrid) #Player inputs where they want to put there play
      winner(gameGrid)
      if winner(gameGrid) != True:
        tie(gameGrid)
        if tie(gameGrid) != True:
          pTurn()
          CPUplay(gameGrid)
          winner(gameGrid)
          if winner(gameGrid) != True:
            tie(gameGrid)
          else: 
            print(f"The winner is {gameWinner}!\n\n")
            onemore = input("Would you like to play again? [Yes] or [No]? ").lower()
            if onemore == "yes" or onemore == "ye" or onemore == "sure":
              playAgain = True
            else:
              char_delay("No worries! We hope you enjoyed!", .01)
              playAgain = False
            
        else: 
          print(f"The winner is {gameWinner}!\n\n")
          onemore = input("Would you like to play again? [Yes] or [No]? ").lower()
          if onemore == "yes" or onemore == "ye" or onemore == "sure":
            playAgain = True
          else:
            char_delay("No worries! We hope you enjoyed!", .01)
            playAgain = False
      else: 
        print(f"The winner is {gameWinner}!\n\n")
        onemore = input("Would you like to play again? [Yes] or [No]? ").lower()
        if onemore == "yes" or onemore == "ye" or onemore == "sure":
          playAgain = True
        else:
          char_delay("No worries! We hope you enjoyed!", .01)
          playAgain = False
    if winner(gameGrid):
      print(f"The winner is {gameWinner}")