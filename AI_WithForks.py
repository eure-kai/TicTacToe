# main.py
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
    Row = int(input(f"\n\nPlease pick a row (1, 2, or 3): "))
    
    if Grid[Row-1][0] != 0 and Grid[Row-1][1] != 0 and Grid[Row-1][2] != 0: #if the elements in the row are already full, have the user try again
      print(f"\nRow is already full, pick again.")
    
    
    else:
      Col = int(input(f"Please pick a column (1, 2, or 3): "))
  
      
      if Row-1 in range(0, 3) and Col-1 in range(0, 3): #Row and Column must both be 0,1,or 2 so use range(0,3)
        
        if Grid[Row-1][Col-1] == 0: #if the element is empty:
          Grid[Row-1][Col-1] = 1 #then let the user possess it
          break
        
        else: #otherwise, try again
          print(f"\nCell is already full, pick again.")
      
      else: #if not in range(0,3), have the user pick again
        print(f"\nInvalid row and column, pick again.")
      
  

def Is_A_Winning_Move(Value, Row, Col, Grid): #check if the position is a win move
  temp = copy.deepcopy(Grid) #make a copy of Grid
  
  temp[Row][Col] = Value #set temp's position as value
  
  return Check_Win(temp, Value) #check for wins, either return True or False




def Check_for_Forks(Value, Row, Col, Grid): #check if the position is a fork
  temp = copy.deepcopy(Grid) #make a copy of Grid
  
  temp[Row][Col] = Value #set temp's position as value
  
  wins = 0 #keep track of how many win moves there are
  
  for i in range(0, len(temp)): #for every row:
    for j in range(0, len(temp[0])): #for every col in row:
      check = Is_A_Winning_Move(Value, i, j, temp) #check if each position is a potential winning move for temp
        
      if check == True and temp[i][j] == 0: #if so, and the position is empty:
        wins += 1 #mark it as a winning move by adding 1 to wins
  
  if wins >= 2: #if you have 2 or more wins possible, then it's a fork:
    return True 
  
  else: #otherwise, return False
    return False
      
  
  
  
def AI_Turn(Grid):
  print(f"\n\nThe AI uses logic...")
  sleep(0.5)
  
  for i in range(len(Grid)): #first, check for AI winning moves
    for j in range(len(Grid[0])):
      
      if Grid[i][j] == 0 and Is_A_Winning_Move(2, i, j, Grid) == True: #if the position is empty, and it is a winning move:
        Grid[i][j] = 2 #immediately possess it to win
        return
        
        
  for k in range(len(Grid)): #then, check for player winning moves
    for l in range(len(Grid[0])):
      
      if Grid[k][l] == 0 and Is_A_Winning_Move(1, k, l, Grid) == True: #if the position is empty, and it is a winning move:
        Grid[k][l] = 2 #immediately block it to prevent losing
        return
  
  
  for m in range(len(Grid)): #next, check for AI fork moves
    for n in range(len(Grid[0])):
      
      if Grid[m][n] == 0 and Check_for_Forks(2, m, n, Grid) == True: #if the position is empty, and it is a fork move:
        Grid[m][n] = 2 #immediately possess it
        return
        
  
  for o in range(len(Grid)): #finally, check for player fork moves
    for p in range(len(Grid[0])):
      
      if Grid[o][p] == 0 and Check_for_Forks(1, o, p, Grid) == True: #if the position is empty, and it is a winning move:
        Grid[o][p] = 2 
        return
          
       
       
  if Grid[1][1] == 0: #first thing to check afterwards is center
    Grid[1][1] = 2 #if the center is empty, immediately hold it
    return
  
  
  Corners = ["TL", "TR", "BL", "BR"] #next, check the corners
  
  random = choice(Corners) #randomly choose a corner
    
  #then, add 2 to the correct corner, respectively:
  if random == "TL" and Grid[0][0] == 0:
    Grid[0][0] = 2 
  
  elif random == "TR" and Grid[0][2] == 0:
    Grid[0][2] = 2 
    
  elif random == "BL" and Grid[2][0] == 0:
    Grid[2][0] = 2 
  
  elif random == "BR" and Grid[2][2] == 0:
    Grid[2][2] = 2
    

  else: #if the center and the corners are already full:
    while True: #just randomly choose a possible item
      Row = randint(0, 2)
      Col = randint(0, 2)
      
      if Grid[Row][Col] == 0:
        Grid[Row][Col] = 2
        break
  
  return
  
      
    
    
def Check_Win(Grid, Value): #function to check wins
  for i in range(len(Grid)): #check rows
    check = 0 #temporary variable to keep track
    
    for j in range(len(Grid[0])): #for each col in row
      if Grid[i][j] == Value: #When checking rows, the column changes, so j is the column (since j changes in this nested loop)
        check += 1
    
    if check == 3: #if check is 3, that means Grid[i][0] == Grid[i][1] == Grid[i][2], meaning the row was equal. So, return True
      return True 
      
      
  for i in range(len(Grid)): #check columns
    check = 0 #temporary variable to keep track
    
    for j in range(len(Grid[0])):
      if Grid[j][i] == Value: #this time, j and i are reversed, since the row changes
        check += 1
    
    if check == 3: #if check is 3, that means Grid[0][i] == Grid[1][i] == Grid[2][i], meaning the column was equal. So, return True
      return True
  
  
  if Grid[0][0] == Value and Grid[0][0] == Grid[1][1] and Grid[0][0] == Grid[2][2]: #then, check diagonal from left to right
    return True
  
  if Grid[0][2] == Value and Grid[0][2] == Grid[1][1] and Grid[0][2] == Grid[2][0]: #finally, check diagonal from right to left
    return True
      
      
  else: #nothing works, return False
    return False



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
    
    else: #otherwise, it's the AI's turn
      sleep(1)
      AI_Turn(Grid)
     
     
    Win_Play = Check_Win(Grid, 1) #call check_win for the player's values (1)
    Win_AI = Check_Win(Grid, 2) #call check_win for the AI's values (2)
    
    if Win_Play == True: #if Win_Play is True, then the user wins
      sleep(1)
      print("\n")
      Print_Grid(Grid) #print the Grid to show the winning board
      sleep(1)
      print(f"\nPlayer O (you) wins! Game over.")
      break
    
    
    elif Win_AI == True: #if Win_AI is True, then the AI wins
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

  
  
def Play_Again(): #function to play again
  sleep(2.5)
  choice = input("\n\nWould you like to play again? (Y for Yes) ") #ask
  
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
  
  
  
  
