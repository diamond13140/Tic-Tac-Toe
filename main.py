#       ------ <|Global Variables|> -------

checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# count = 0
i = '|'
change = [
" "," "," ",
" "," "," ",
" "," "," "
]


# display bash of Tic Tac Toe game   :
def display():
    bash = f'''                                                |            |     |         
         {i}     {i}                                |         7  |  8  |  9
      {change[6]}  {i}  {change[7]}  {i}  {change[8]}                             |       _____|_____|_____ 
    _____{i}_____{i}_____                           |            |     |  
         {i}     {i}                                |         4  |  5  |  6
      {change[3]}  {i}  {change[4]}  {i}  {change[5]}                             |       _____|_____|_____ 
    _____{i}_____{i}_____                           |            |     |  
         {i}     {i}                                |         1  |  2  |  3
      {change[0]}  {i}  {change[1]}  {i}  {change[2]}                             |            |     |        
         {i}     {i}                                |        

    '''
    print(bash)
  # return bash


# player's turn -->
def player(count):

    #player1 turn :     
    if count%2 == 0:   
        change[num-1] = "x"
        display()

    #player2 turn :
    else:
        change[num-1] = "o"
        display()


# check row winners
def checkRow():
    
    if change[0] == change[1] == change[2] != " ":
        checkR = 1

    elif change[3] == change[4] == change[5] != " ":
        checkR = 1

    elif change[6] == change[7] == change[8] != " ":
        checkR = 1
    
    else:
        checkR = 0

    return checkR


# check column winners
def checkColumn():

    if change[0] == change[3] == change[6] != " ":
        checkC = 1
    
    elif change[1] == change[4] == change[7] != " ":
        checkC = 1
    
    elif change[2] == change[5] == change[8] != " ":
        checkC = 1
    
    else:
        checkC = 0
        
    return checkC


# check diagonal winners
def checkdiagonals():

    if change[0] == change[4] == change[8] != " ":
        checkD = 1

    elif change[2] == change[4] == change[6] != " ":
        checkD = 1

    else:
        checkD = 0

    return checkD

# check winners
def gameWinner():

    if checkRow() == 1 or checkColumn() == 1 or checkdiagonals() == 1:
        result = 1
    else:
        result = 0
    
    return result

# Main Code 
if __name__ == "__main__":

    count = 0
    
    # display function will show game-board
    display()


    while len(checkList) > 0:
        num = int(input("Please select one no. (1-9) : "))
        
        # condition for avoiding overlap
        if num in checkList:
            player(count)
            count += 1
            checkList.remove(num)
        else:
            print("\nInvalid Input!\n")

        # function call gameWinnner

        if gameWinner() == 1:
            if count % 2 == 0:
                print("\n************************** Player 'o' Wins ************************")
            
            else:
                print("\n************************** Player 'x' Wins ************************")
            
            break
        
# All boxes are filled no space remains for next turn 
    else:
        print("Match Draw !")
8