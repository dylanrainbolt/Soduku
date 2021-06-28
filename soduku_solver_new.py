import math
import random
def initialize():
    game=[]
    for i in range(3):
        game.append('||=====================================||')
        game.append('||   |   |   ||   |   |   ||   |   |   ||')
        game.append('||   |   |   ||   |   |   ||   |   |   ||')
        game.append('||   |   |   ||   |   |   ||   |   |   ||')
    game.append('||=====================================||')
    return game

def row_val_changer(row, col, val):
    curr_row= list(row)
    curr_row[int(col[0])]= val[0]
    curr_row[int(col[1])]= val[1]
    curr_row[int(col[2])]= val[2]
    curr_row= "".join(curr_row)
    return curr_row

def add_vals(game):
    new= []
    for row in range(12):
        if row == 0 or row==4 or row==8 or row==12:
            new.append('||=====================================||')
        else:
            col1= str(random.randint(1,9))
            col2= str(random.randint(1,9))
            col3= str(random.randint(1,9))
            while col1 == col2 or col1 == col3 or col2==col3:
                col1= str(random.randint(1,9))
                col2= str(random.randint(1,9))
                col3= str(random.randint(1,9))
            col_vals= [col1, col2, col3]
            #print(col_vals)
            #print('-----')
            for i in range(3):
                if 3 >= int(col_vals[i]) >= 1:
                    col_vals[i]= str(int(col_vals[i])*4-1)
                if 6 >= int(col_vals[i]) > 3:
                    col_vals[i]= str(int(col_vals[i])*4)
                if 9 >= int(col_vals[i]) > 6:
                    col_vals[i]= str(int(col_vals[i])*4+1)

            #print(col_vals)
            
            curr_row= list(game[row])

            val= str(random.randint(1,9))
            val2= str(random.randint(1,9))
            val3= str(random.randint(1,9))

            while val== val2 or val == val3 or val2== val3:
                val2= str(random.randint(1,9))
                val3= str(random.randint(1,9))
            
            vals= [val,val2,val3]
            temp= row_val_changer(curr_row,col_vals,vals)
            new.append(temp)
    new.append('||=====================================||')
    print_game(new)
    return new

def print_game(board):
    for i in board:
        print(i)

def check_row(search_val, col): #variable row is actually the columns within the row
    for row in range(9):
        if 3 >= row >= 1:
            row= row*4-1
        if 6 >= row > 3:
            row= row*4
        if 9 >= row > 6:
            row= row*4+1
        col= list(col)
        while search_val == col[row]:
            print('value: ', col[row])
            

def master_check(game):
    row= game[0]
    row_vals= []
    for char in range(1,10):
        if 3 >= char >= 1:
            char= char*4-1
        if 6 >= char > 3:
            char= char*4
        if 9 >= char > 6:
            char= char*4+1
        search_val= row[char]
        check_row(search_val,char)

def main():
    game= initialize()
    game= add_vals(game)
    master_check(game)

main()
