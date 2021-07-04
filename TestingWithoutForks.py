
from random import randint
from random import choice
from time import sleep 


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
        newRow.append("O") #if 1, add an O - for the random
        
      elif Col == 2:
        newRow.append("X") #if 2, add an X - for the AI
    
    newGrid.append(newRow) #add the newRow to newGrid
    
  #print the tic tac toe board, as shown below  
  print(f" {newGrid[0][0]} | {newGrid[0][1]} | {newGrid[0][2]} ")
  print("---+---+---")    
  print(f" {newGrid[1][0]} | {newGrid[1][1]} | {newGrid[1][2]} ")  
  print("---+---+---")    
  print(f" {newGrid[2][0]} | {newGrid[2][1]} | {newGrid[2][2]} ")
      
  


def Is_A_Winning_Move(Value, Row, Col, Grid): #check winning move
  temp = copy.deepcopy(Grid) #make a copy of Grid
  
  temp[Row][Col] = Value #set temp's position as value
  
  return Check_Win(temp, Value) #check for wins, either return True or False
      
  
  
  
def Computer_Turn(Grid): #random computer
  while True:
    Row = randint(0, 2) #randomly pick a row, 0, 1, or 2
    Col = randint(0, 2) #randomly pick a col, 0, 1, or 2
    
    if Grid[Row][Col] == 0: #if no value is in the position:
      Grid[Row][Col] += 1 #then have the computer possess it
      break #break from the loop
  
  
  
def AI_Turn(Grid): #AI computer (smart)
  
  for i in range(len(Grid)):
    for j in range(len(Grid[0])):
      if Grid[i][j] == 0: #if the position is empty:
        Computer = Is_A_Winning_Move(1, i, j, Grid)
        AI = Is_A_Winning_Move(2, i, j, Grid)
        #call Is_A_Winning_Move for both Computer and AI to see if either one of them have a winning move
        
        if Computer == True or AI == True: #if they do:
          Grid[i][j] += 2 #immediately block/possess it to prevent losing, or win
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
  Grid = Create_Grid() #create the Grid
  turns = 0 #variable to keep track of turns
  
  Flip = CoinFlip() #call CoinFlip() and store it into Flip
  
  if Flip == 1: #if Flip is 1, then it's the AI's turn
    turns += 1 #add 1 to turns to signal it's the AI's turn
  
  
  while True:
    print("\n")
    Print_Grid(Grid) #print the Grid
    
    if turns % 2 == 0: #if turns is divisible by 2, computer
      Computer_Turn(Grid)
    
    else: #if it's not divisible by 2, AI's turn
      AI_Turn(Grid)
     
    Win = Check_Win(Grid) #call Check_Win, store it into Win
    
    if Win == 1: #if Win is 1, then the computer won
      print("\n")
      Print_Grid(Grid)
      return 1
    
    elif Win == 2: #if Win is 2, then the AI won
      print("\n")
      Print_Grid(Grid)
      return 2
  
  
    Tie = Check_Tie(Grid)
    
    if Tie == True: #if it's a Tie, return 3 to signal difference
      print("\n")
      Print_Grid(Grid)
      return 3
    
    turns += 1 #add 1 to switch turns
    
   
   
    
def Official():
  computer = 0 #keeping track of computer wins
  AI = 0 #keeping track of AI wins
  tie = 0 #keeping track of ties
  
  for i in range(1000): #call Play() 1000 times
    print("\n")
    Value = Play() #store the returning value into Value
    
    if Value == 1: #if it's 1, computer won, so add 1 to computer
      computer += 1
    
    elif Value == 2: #if it's 2, AI won, so add 1 to AI
      AI += 1 
    
    elif Value == 3: #if it's 3, it's a tie, so add 1 to tie
      tie += 1
      
  print(f"\n\nTies: {tie}") #print everything at the end
  print(f"RANDOM wins: {computer}")
  print(f"AI wins: {AI}")
  
  

Official()
  
  
  
