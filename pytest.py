# Simple pygame program
# Import and initialize the pygame library
import pygame
import ticktacktoe
pygame.init()
y = 1
empty_game = [[" "," "," "],[" "," "," "],[" "," "," "]]
# Set up the drawing window
screen = pygame.display.set_mode([800, 800])

pygame.Surface([500, 500])
start_pos = (266, 100)
end_pos = (266, 700)
start_pos2 = (533, 100)
end_pos2 = (533, 700)
start_pos3 = (100, 266)
end_pos3 = (700, 266)
start_pos4 = (100, 533)
end_pos4 = (700, 533)

def draw_ticktactoe(board):
    print(board)
    X, Y = 100, 100
    for row in board:
        X = 100
        for column in row:
            if column == "O":
                pygame.draw.circle(screen, (0, 0, 255), (X, Y), 50, width = 1)
            if column == "X":
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(X, Y, 100, 100), width = 1)
            print(row)
            print(column)
            #pygame.draw.circle(screen, (0 ,0 ,255), (X, Y), 50, width = 1)
            #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(X, Y, 100, 100), width = 1)
            X += 266
        Y += 266
        
        
def check_game2(empty_game):
    if empty_game[0] == ["X","X","X"] or empty_game[1] == ["X","X","X"] or empty_game[2] == ["X","X","X"] :
        print("X WINS!")
        return True
    if empty_game[0] == ["O","O","O"] or empty_game[1] == ["O","O","O"] or empty_game[2] == ["O","O","O"]:
        print("O WINS!")
        return True
    if empty_game[0][0] == "X" and empty_game[1][0] == "X" and empty_game[2][0] == "X":
        print("X WINS!")
        return True
    if empty_game[0][1] == "X" and empty_game[1][1] == "X" and empty_game[2][1] == "X":
        print("X WINS!")
        return True
    if empty_game[0][2] == "X" and empty_game[1][2] == "X" and empty_game[2][2] == "X":
        print("X WINS!")
        return True
    if empty_game[0][0] == "O" and empty_game[1][0] == "O" and empty_game[2][0] =="O":
        print("O WINS!")
        return True
    if empty_game[0][1] == "O" and empty_game[1][1] == "O" and empty_game[2][1] == "O":
        print("O WINS!")
        return True
    if empty_game[0][2] == "O" and empty_game[1][2] == "O" and empty_game[2][2] == "O":
        print("O WINS!")
        return True
    if empty_game[0][0] == "X" and empty_game[1][1] == "X" and empty_game[2][2] == "X":
        print("X WINS!")
        return True
    if empty_game[0][0] == "O" and empty_game[1][1] == "O" and empty_game[2][2] == "O":
        print("O WINS!")
        return True
    if empty_game[0][2] == "X" and empty_game[1][1] == "X" and empty_game[2][0] == "X":
        print("X WINS!Congrats")
        return True
    if empty_game[0][2] == "O" and empty_game[1][1] == "O" and empty_game[2][0] == "O":
        print("O WINS!Congrats")
        return True
    return False
    
game_over = False
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
# Did the user click the window close button?

    # Fill the background with white
    screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
           #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
         # Flip the display
    pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos)
    pygame.draw.line(screen, (0, 0, 0), start_pos2, end_pos2)
    pygame.draw.line(screen, (0, 0, 0), start_pos3, end_pos3)
    pygame.draw.line(screen, (0, 0, 0), start_pos4, end_pos4)
    

    counter = 0
    result = False
    if game_over == False:
        for counter in range(counter < 10):
            draw_ticktactoe(empty_game)
            pygame.display.flip()
            ticktacktoe.ticktac_toe(empty_game, y + 1)
            y += 1
            pygame.display.flip()
            # Done! Time to quit.
            result = check_game2(empty_game)
            if result is True:
                ticktacktoe.draw_game(empty_game)
                draw_ticktactoe(empty_game)
                pygame.display.flip()
                game_over = True
                break
            
pygame.quit()




