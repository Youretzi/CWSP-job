# X | X | O
# O | X | O
# X | O | O

#game = [["X","O","O"],["O","X","X"],["O","O","X"]]
#game2 = [1,2,3,4,5,6,7,8,9]
#empty_game = [[" "," "," "],[" "," "," "],[" "," "," "]]
def take_input():
    row = input("enter row: ")
    column = input("enter column: ")
    return row,column
    
def check_value(row,column,empty_game):
    if empty_game[row-1][column-1] == " ":
        return False
    if empty_game[row-1][column-1] == "X":
        return True
    if empty_game[row-1][column-1] == "O":
        return True

def number_input():
    x = input()
    if x.isdigit():
        print("Number")
    else:
        print("not a number")
def draw_game(game_board):
    board = ""
    counter = 1
    for row in game_board:
        each_row = ""
        each_row += "|"
        if row[0] == "X":
            each_row += " X "
        elif row[0] == "O":
            each_row += " O "
        elif row[0] == " ":
            each_row += "   "
            
    
        each_row += "|"
        if row[1] == "X":
            each_row += " X "
        elif row[1] == "O":
            each_row += " O "
        elif row[1] == " ":
            each_row += "   "
        
        
        each_row += "|"
        if row[2] == "X":
            each_row += " X "
        elif row[2] == "O":
            each_row += " O "
        elif row[2] == " ":
            each_row += "   "
        print(each_row+"|" , str(counter))
        print("|-----------|")
        counter += 1
    print("  1   2   3")
        
def check_game(game_board):
    if game_board[0] == ["X","X","X"] or game_board[1] == ["X","X","X"] or game_board[2] == ["X","X","X"] :
        print("X WINS!")
        return True
    if game_board[0] == ["O","O","O"] or game_board[1] == ["O","O","O"]or game_board[2] == ["O","O","O"]:
        print("O WINS!")
        return True
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("X WINS!")
        return True
    if game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("X WINS!")
        return True
    if game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("X WINS!")
        return True
    if game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] =="O":
        print("O WINS!")
        return True
    if game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("O WINS!")
        return True
    if game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("O WINS!")
        return True
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("X WINS!")
        return True
    if game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("O WINS!")
        return True
    if game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("X WINS!Congrats")
        return True
    if game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("O WINS!Congrats")
        return True
    return False
    
def ticktac_toe(empty_game, x):
    draw_game(empty_game)
    if (int(x) %2) == 0:
        print ("Player X turn")
        row,column = take_input()
        if (int(row) > 3 or int(column) > 3 or int(row) < 1 or int(column) < 1) or check_value(int(row),int(column),empty_game):
            print("Number is not in range")
            row,column = take_input()
            empty_game[int(row)-1][int(column)-1]= "X"
    
        else:
            empty_game[int(row)-1][int(column)-1]= "X"
        
    else:
        print ("Player O turn")
        row,column = take_input()
        if (int(row) > 3 or int(column) > 3 or int(row) < 1 or int(column) < 1) or check_value(int(row),int(column),empty_game):
            print("Number is not in range")
            row,column = take_input()
            empty_game[int(row)-1][int(column)-1]= "O"
        else:
            empty_game[int(row)-1][int(column)-1]= "O"
        print("game")
            
      
   


