import pygame
import pygame.freetype
pygame.init()


board = [
   [0, 5, 2, 4, 8, 9, 3, 7, 6],
   [7, 3, 9, 2, 5, 6, 8, 4, 1],
   [4, 6, 8, 3, 7, 1, 2, 9, 5],
   [3, 8, 7, 1, 2, 4, 6, 5, 9],
   [5, 9, 1, 7, 6, 3, 4, 2, 8],
   [2, 4, 6, 8, 9, 5, 7, 1, 3],
   [9, 1, 4, 6, 3, 7, 5, 8, 2],
   [6, 2, 5, 9, 4, 8, 1, 3, 7],
   [8, 7, 3, 5, 1, 2, 9, 6, 4]
]

def draw_board(): 
    screen = pygame.display.set_mode((900, 900))
    pygame.Surface([500,500])
    screen.fill((255,255,255))
    start_pos13 =(15, 775)
    end_pos13 = (870, 775)
    start_pos16 = (15, 100)
    end_pos16 = (15, 775)
    start_pos19 = (15, 100)
    end_pos19 = (870, 100)
    start_pos20 = (870,100)
    end_pos20 = (870, 775)

    pygame.draw.line(screen, (0,0,0), start_pos19, end_pos19, width = 2)
    pygame.draw.line(screen, (0,0,0), start_pos20, end_pos20, width = 2)
    pygame.draw.line(screen, (0,0,0), start_pos16, end_pos16, width = 2)
    pygame.draw.line(screen, (0,0,0), start_pos13, end_pos13, width = 2)
    for x in range(9):
        height = 75 * (x + 1) + 100 
        pygame.draw.line(screen, (0,0,0), (15,height), (870, height))
        width = 95 * (x + 1) + 15
        pygame.draw.line(screen, (0,0,0), (width, 100), (width, 775))
        if x == 2:
            pygame.draw.line(screen, (0,0,0), (15,height), (870, height), width = 2)
            pygame.draw.line(screen, (0,0,0), (width, 100), (width, 775), width = 2)
        elif x == 5: 
            pygame.draw.line(screen, (0,0,0), (15,height), (870, height), width = 2)
            pygame.draw.line(screen, (0,0,0), (width, 100), (width, 775), width = 2)
    a = 50 
    b = 120
    FONT = pygame.freetype.Font(None, 50)
    text_surface, rect = FONT.render(str(x), (0, 0, 0))
    for i in range(9):
        a = 50
        for j in range(9):
            text_surface, rect = FONT.render(str(board[i][j]), (0, 0, 0))
            screen.blit(text_surface, (a ,b)) 
            a += 95    
        b += 75

draw_board()

def cell_location(pos):
    u = pos[0] - 15 
    y = u // 95
    r = pos[1] - 100 
    x = r // 75
    print(x, y) 
    e = input("New number: ")
    while True:
        if e.isnumeric() is False:
            e = input("Invalid input1, try again: ")
        elif int(e) > 9:
            e = input("Invalid input2, try again: ")
        elif int(e) < 1:
           e = input("Invalid input3, try again: ")
        else:
            break 
    print(e)  
    board[x][y] = int(e)
    print(board)
    draw_board()
    print(board)
    pygame.display.flip()

def row_solver():
    counter = 0 
    for x in range(9):
        board2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        set1 = set(board[x])
        set2 = set(board2)
        if set2.intersection(set1):
            if set2.intersection(set1) == set2:
                counter += 1
                print("True")
        else:
                print("False")
        if counter == 9:
            print("ROWS SOLVED!")
    return counter == 9 

def column_solver():
    #this for loop is for checking the column 
    counter = 0 
    for x in range(9):
        board3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        set3 = set([])
        set4 = set(board3)
        #this for loop is for gathering colum values
        for y in range(9): 
            column = board[y][x]
            set3.add(column)
        if set4.intersection(set3):
            if set4.intersection(set3) == set4:
                counter += 1
                print("CONGRATS")
        else:
                print("False")
        if counter == 9:
            print("COLUMNS SOLVED!")
    return counter == 9 
#3x3 grid checking(for look is ruuning 9x?)Getting mixed result???
def begin_3x3():
    counter = 0 
    grid = set([1,2,3,4,5,6,7,8,9])
    set2 = set()
    set1 = set(grid)
    set3 = set()
    set4 = set()
    set5 = set()
    set6 = set()
    set7 = set()
    set8 = set()
    set9 = set()
    set10 = set()
    
    for x in range(3): 
        for y in range(1):
            set2.add(board[x][0])
            set2.add(board[x][1])
            set2.add(board[x][2])
            if set2 == grid:
                counter += 1
                print("Completed")
    print(set2)
    for i in range(3):
        set3.add(board[i][3])
        set3.add(board[i][4])
        set3.add(board[i][5])
        if set3 == grid:
            counter += 1 
            print("Completed")
    print(set3)
    
    for h in range(3):
        set4.add(board[h][6])
        set4.add(board[h][7])
        set4.add(board[h][8])
        if set4 == grid:
            counter += 1 
            print("Completed")
    print(set4)
    
    for c in range(3):
        p = c + 3 
        set5.add(board[p][0])
        set5.add(board[p][1])
        set5.add(board[p][2])
        if set5 == grid:
            counter += 1 
            print("Completed")
    print(set5)
    for y in range(3):
        t = y + 3
        set6.add(board[t][3])
        set6.add(board[t][4])
        set6.add(board[t][5])
        if set6 == grid:
            counter += 1 
            print("Completed")
    print(set6)
    
    for m in range(3):
        y = m + 3
        set7.add(board[y][6])
        set7.add(board[y][7])
        set7.add(board[y][8])
        if set7 == grid:
            counter += 1 
            print("Completed")
    print(set7)

    for r in range(3):
        k = r + 6
        set8.add(board[k][0])
        set8.add(board[k][1])
        set8.add(board[k][2])
        if set8 == grid:
            counter += 1 
            print("Completed")
    print(set8)
        
    for g in range(3):
        r = g + 6
        set9.add(board[r][3])
        set9.add(board[r][4])
        set9.add(board[r][5])
        if set9 == grid:
            counter += 1 
            print("Completed")
    print(set9)

    for w in range(3):
        t = w + 6
        set10.add(board[t][6])
        set10.add(board[t][7])
        set10.add(board[t][8])
        if set10 == grid:
            counter += 1 
            print("Completed")
    print(set10)
    print(counter)
    if counter == 9:
        print("3X3 SOLVED")
    return counter == 9 
pygame.display.flip()
pygame.event.get()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            if 15 <= pos[0] <= 870 and 100 <= pos[1] <= 775:
                cell_location(pos) 
                if row_solver() == True:
                    if column_solver() == True:
                        if begin_3x3() == True:
                            print("YOU WON CONGRATS!!")
                            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
print(board)