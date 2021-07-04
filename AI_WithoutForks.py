
from random import randint
from random import choice
from time import sleep
import copy 


def CoinFlip(): #Flip a coin
  return randint(0,1)


def Create_Grid(): #create the grid
  Grid = [] #list of lists
  
  for i in range(3):
    row = [] #Row major
    
    for j in range(3):
      element = 0
      row.append(element) #add a bunch of zeros to each row
      
    Grid.append(row) #add the rows to the Grid
    
  return Grid #return the Grid
  


def Print_Grid(Grid): #print the grid
  newGrid = [] #variable to convert to O's and X's
  
  for Row in Grid:
    newRow = []
    for Col in Row:
      if Col == 0:
        newRow.append(" ") #if 0, then just add an empty space
        
      elif Col == 1:
        newRow.append("O") #if 1, add an O - for the player
        
      elif Col == 2:
        newRow.append("X") #if 2, add an X - for the AI
    
    newGrid.append(newRow) #add the newRow to newGrid
    
  #print the tic tac toe board, as shown below  
  print(f" {newGrid[0][0]} | {newGrid[0][1]} | {newGrid[0][2]} ")
  print("---+---+---")    
  print(f" {newGrid[1][0]} | {newGrid[1][1]} | {newGrid[1][2]} ")  
  print("---+---+---")    
  print(f" {newGrid[2][0]} | {newGrid[2][1]} | {newGrid[2][2]} ")

  
  
def User_Turn(Grid): #User's Turn
  while True:
    Row = int(input(f"\n\nPlease pick a row (0, 1, or 2): "))
    Col = int(input(f"Please pick a column (0, 1, or 2): "))
    
    if Row in range(0, 3) and Col in range(0, 3): #Row and Column must both be 0,1,or 2 so use range(0,3)
      
      if Grid[Row][Col] == 0: #if the element is empty:
        Grid[Row][Col] += 1 #then let the user possess it
        break
      
      else: #otherwise, try again
        print(f"\nCell is already full, pick again.")
    
    else: #if not in range(0,3), have the user pick again
      print(f"\nInvalid row and column, pick again.")
      
  

def Is_A_Winning_Move(Value, Row, Col, Grid): #check winning move
  temp = copy.deepcopy(Grid) #make a copy of Grid
  
  temp[Row][Col] = Value #set temp's position as value
  
  return Check_Win(temp, Value) #check for wins, either return True or False
      
  
  
  
def Computer_Turn(Grid):
  print(f"\n\nThe AI uses logic...")
  sleep(0.5)
  
  for i in range(len(Grid)):
    for j in range(len(Grid[0])):
      if Grid[i][j] == 0: #if the position is empty:
        Player = Is_A_Winning_Move(1, i, j, Grid)
        AI = Is_A_Winning_Move(2, i, j, Grid)
        #call Is_A_Winning_Move for both Computer and AI to see if either one of them have a winning move
        
        if AI == True: #check if AI can win:
          Grid[i][j] += 2 #immediately possess it to win
          return
         
        if Player == True: #next, check if player can win:
          Grid[i][j] += 2 #if so, immediately block it to prevent losing
          return
          
          
  if Grid[1][1] == 0: #first thing to check afterwards is center
    Grid[1][1] += 2 #if the center is empty, immediately hold it
    return
  
  
  Corners = [] #next, check the corners
  
  if Grid[0][0] == 0:
    Corners.append("TL") #top left corner
  
  elif Grid[0][2] == 0:
    Corners.append("TR") #top right corner
    
  elif Grid[2][0] == 0:
    Corners.append("BL") #bottom left corner
    
  elif Grid[2][2] == 0:
    Corners.append("BR") #bottom right corner
  
  
  if len(Corners) > 0: #if at least one element was appended:
    random = choice(Corners) #randomly choose a corner
    
    #then, add 2 to the correct corner, respectively:
    if random == "TL":
      Grid[0][0] += 2 
    
    elif random == "TR":
      Grid[0][2] += 2 
      
    elif random == "BL":
      Grid[2][0] += 2 
    
    elif random == "BR":
      Grid[2][2] += 2
    
    return
    

  else: #if the center and the corners are already full:
    while True: #just randomly choose a possible item
      Row = randint(0, 2)
      Col = randint(0, 2)
      
      if Grid[Row][Col] == 0:
        Grid[Row][Col] += 2
        break
  
  return
  
      
    
    
def Check_Win(Grid): #function to check wins
  if Grid[0][0] != 0 and Grid[0][0] == Grid[0][1] and Grid[0][0] == Grid[0][2]: #top row
    return Grid[0][0] 
    
  if Grid[1][0] != 0 and Grid[1][0] == Grid[1][1] and Grid[1][0] == Grid[1][2]: #middle row
    return Grid[1][0]
    
  if Grid[2][0] != 0 and Grid[2][0] == Grid[2][1] and Grid[2][0] == Grid[2][2]: #bottom row
    return Grid[2][0]
  
  
  if Grid[0][0] != 0 and Grid[0][0] == Grid[1][0] and Grid[0][0] == Grid[2][0]: #left column
    return Grid[0][0]
  
  if Grid[0][1] != 0 and Grid[0][1] == Grid[1][1] and Grid[0][1] == Grid[2][1]: #middle column
    return Grid[0][1]
  
  if Grid[0][2] != 0 and Grid[0][2] == Grid[1][2] and Grid[0][2] == Grid[2][2]: #right column
    return Grid[0][2]
  
  
  if Grid[0][0] != 0 and Grid[0][0] == Grid[1][1] and Grid[0][0] == Grid[2][2]: #diagonal from left to right
    return Grid[0][0] 
  
  if Grid[0][2] != 0 and Grid[0][2] == Grid[1][1] and Grid[0][2] == Grid[2][0]: #diagonal from right to left
    return Grid[0][2]
  
  else:
    return 0 #none of these methods, then return 0



def Check_Tie(Grid): #function to check ties
  for Row in Grid:
    for Col in Row:
      if Col == 0: #check every element, if at least one of them are empty (aka 0), then return False
        return False 
  
  return True #otherwise, return True
  
  



#--------------------------------------------------------------

def Play():
  Grid = Create_Grid() #create the grid first
  turns = 0 #variable to keep track of turns
  
  sleep(0.5)
  Flip = CoinFlip() #store the result of the coinFlip into Flip
  
  if Flip == 0: #if Flip is 0, user begins
    print(f"The coin flip has decided that you go first! (you are O) ")
  
  else: #else, meaning FLip is 1, then computer begins
    print(f"The coin flip has decided that the AI goes first. (X) ")
    turns += 1 #add 1 to signal the computer begins
  
  
  while True:
    sleep(1)
    print("\n")
    
    Print_Grid(Grid) #print the Grid
    
    if turns % 2 == 0: #if turns is divisible by 2, user's turn
      User_Turn(Grid)
    
    else: #otherwise, it's the computer's turn
      sleep(1)
      Computer_Turn(Grid)
     
     
    Win = Check_Win(Grid) #call check_win and store it into Win
    
    if Win == 1: #if Win is 1, then the user wins
      sleep(1)
      print("\n")
      Print_Grid(Grid) #print the Grid to show the winning board
      sleep(1)
      print(f"\nPlayer O (you) wins! Game over.")
      break
    
    
    elif Win == 2: #if Win is 2, then the computer wins
      sleep(1)
      print("\n")
      Print_Grid(Grid) #print the Grid to show the winning board
      print(f"\nPlayer X (the AI) wins. Game over.")
      break 
  
  
    Tie = Check_Tie(Grid) #next, call Check_Tie, store into Tie
    
    if Tie == True: #if it is a tie, then print "Tie!"
      sleep(1)
      print("\n")
      Print_Grid(Grid)
      sleep(1)
      print(f"\nAll cells are full. Tie!")
      break 
    
    turns += 1 #add 1 to switch turns
  
  Play_Again() #once game is over, ask the user Play Again?

  
  
def Play_Again():
  sleep(2.5)
  choice = input("\n\nWould you like to play again? Y/N ") #ask
  
  if choice.upper() == "Y": #if yes, then play again
    sleep(2.5)
    print("\n\n")
    Play()
    
  else: #otherwise, exit
    sleep(1)
    print("\nThank you for playing!")
    sleep(1)
    exit(1) 
  
  
Play()  
  
  
  
 
