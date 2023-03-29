import pygame
import time
import random
import sys
print(sys.path)
pygame.init()
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()

pygame.display.set_caption('Snake game by Yaretzi')

blue = (0,0,255)
red = (255,0,0)
black = (0, 0, 0)
white = (255,255,255)
yellow = (255,255,102)
green = (0,255,0)
clock = pygame.time.Clock()
 
snake_block = 80
snake_speed = 10

font_style = pygame.font.Font(pygame.font.get_default_font(), 25)
score_font = pygame.font.Font(pygame.font.get_default_font(), 35)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def Your_score(score):
    #value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(3 , [0, 0])
    
#def message(msg, color):
   # mesg = font_style.render(msg, True, color)
    dis.blit(" x " , [dis_width / 6, dis_height / 3])
    
x1 = dis_width/2
y1 = dis_height/2
snake_block = 10
x1_change = 0
y1_change = 0

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Length_of_snake = 1
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    print(foodx, foody)
 
    while not game_over:
        while game_close == True:
               # dis.fill(white)
                #message("You Lost! Press Q-Quit or C-Play Again", red)
                pygame.display.update()
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
            
         
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            print("mhhm")
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)

       # message("You lose", red)
        pygame.display.update()
    time.sleep(1)
        
    pygame.quit()
    quit()
gameLoop()
