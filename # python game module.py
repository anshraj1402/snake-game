# python game module
import pygame
# python random module to randomise the aapreance of food
import random
import os

#The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.
pygame.init()

# Definig colors to use as per need
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# Creating window screen
screen_width = 1100
screen_height = 700
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



# defining a text screen to write messages on window screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# plotting snake on the window screen
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# welcome page and adding key to play game and replay the game
def welcome() :
    exit_game = False
    while not exit_game:
        gameWindow.fill((0, 255, 0))
        text_screen("Welcome to Snakes", black, 330, 300)
        text_screen("Press Spacebar to start the game", black, 250, 360)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()




        pygame.display.update()
        clock.tick(60)



# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    #snake coordinates
    snake_x = 45
    snake_y = 55
    #snake velocity
    velocity_x = 0
    velocity_y = 0
    #snake length
    snk_list = []
    snk_length = 1
    # Check if highscore file exsits
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()
    #food
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    #score
    score = 0
    # snake movement speed
    init_velocity = 4
    # starting snake size
    snake_size = 20
    #FPS of the game for smoothness
    fps = 60
    # printing message on screen if the game is over
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(green)
            text_screen("Game Over! Press Enter To Try Again", black, 100, 250)

# to quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
# to restart the game

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
# telling what to do on what button is pressed
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
# changing the coordinates as per the buttons are clicked
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
#defining the range when the food and snake will collide and score will be updated and snake size will increase
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(highscore):
                    highscore = score

#printing the Score in multiples of 10
            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "Highscore: "+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

# describing how the snake size will increase when he eats food using list
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
# describing the game over conditions
            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
            # updating the game window
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
