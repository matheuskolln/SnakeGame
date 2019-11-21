# Imports the library Pygame
import pygame
# Imports a function that will be random for objects(directions and positions)
import randomized as random
# Imports a function that will be define when a object collide with another
import collision
# Imports components to load images in Pygame
from pygame.locals import *
# Sets numbers for directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
# Creates a list to set initial random direction
directions = [UP, RIGHT, DOWN, LEFT]


# Function that will run the game
def run():
    # This is the body of snake, and the 3 initial parts and the respective positions
    snake = [(200, 200), (210, 210), (220, 220)]
    # Run the window
    pygame.init()
    # Sets the properties of window(Geometry, Title, Icon)
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Snake Game')
    icon = pygame.image.load("assets/snakeicon.png")
    pygame.display.set_icon(icon)
    # Sets the style for the skin of the snake
    snake_skin = pygame.image.load("assets/snakeskin.png")
    # Sets the initial position randomly of the apple
    apple_pos = (random.pos())
    # Sets the style for the apple
    apple = pygame.image.load("assets/apple.png")
    # Sets the initial position randomly of the skull
    skullpos = (random.pos())
    # Sets the style for the skull
    skull = pygame.image.load("assets/skull.png")
    # Sets the initial position randomly of the storm
    stormpos = (random.pos())
    # Sets the style for the storm
    storm = pygame.image.load("assets/storm.png")
    # Load the background image
    bg = pygame.image.load("assets/bg.png")
    # list with the blocks of the edge
    edgeblock_pos = list()
    # add the blocks of the edge in the list
    for i in range(0, 60):
        edgeblock_pos.append((i*10, -10))
        edgeblock_pos.append((-10, i*10))
        edgeblock_pos.append((600, i*10))
        edgeblock_pos.append((i*10, 600))
    # Sets a randomly initial direction for the snake
    randomdirection = random.direction()
    my_direction = directions[randomdirection]
    # Sets the speed of the snake
    clockrate = 10
    clock = pygame.time.Clock()
    while True:
        clock.tick(clockrate)
        # Puts the background image in window
        screen.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            # Relations of the input(keyboard) to the output(snake moving)
            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT
                if event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT
        # Defines what happens if the snake collides with the apple(when the size is smaller than 10)
        if collision.collide(snake[0], apple_pos) and len(snake) < 10:
            # Sets a new randomly position for the apple
            apple_pos = random.pos()
            # The snake will be up your size by 1
            snake.append((0, 0))
            # The speed will up 2
            clockrate += 2
        # Defines what happens if the snake collides with the apple(when the size is larger or equal than 10)
        if len(snake) >= 10:
            # Puts the skull in the game
            screen.blit(skull, skullpos)
            # Defines what happens if the snake collides with the apple
            if collision.collide(snake[0], apple_pos):
                # Sets a new randomly position for the apple
                apple_pos = random.pos()
                # The snake will be up your size by 1
                snake.append((0, 0))
                # The speed will up 2
                clockrate += 2
                # Sets a new randomly position for the skull
                skullpos = random.pos()
            # Defines what happens if the snake collides with the skull
            if collision.collide(snake[0], skullpos):
                # Sets a new randomly position for the skull
                skullpos = random.pos()
                # Snake will be lose your last 2 parts of the body
                snake.remove(snake[-1])
                snake.remove(snake[-2])
        # Puts the storm if the size of snake is larger or equal than 14 and is divisible by 7
        if len(snake) >= 14 and len(snake) % 7 == 0:
            screen.blit(storm, stormpos)
            # Defines what happens if the snake collides with the storm
            if collision.collide(snake[0], stormpos):
                # The snake will be up your size in 3
                for c in range(0, 3):
                    snake.append((0, 0))
                # Sets a new randomly position for the storm
                stormpos = random.pos()
                # The speed will be up 10
                clockrate += 10
        # Defines what happens if the snake collides with herself
        for i in range(len(snake) - 1, 0, -1):
            if collision.collide(snake[0], snake[i]):
                # The game quits
                pygame.quit()
        # Defines what happens if the snake collides with the blocks of the edge
        for pos in range(0, 240):
            if collision.collide(snake[0], edgeblock_pos[pos]):
                # The game quits
                pygame.quit()
        # Defines the snake will be move parts by part
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])
        # Defines the moves of the snake
        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        # Creates the surface of the edgeblock and fills
        edgeblock = pygame.Surface((10, 10))
        edgeblock.fill((50, 205, 50))
        # Puts the edge blocks in positions of the edge blocks positions(in the list)
        for pos in edgeblock_pos:
            screen.blit(edgeblock, pos)
        # Puts the snake in game
        for pos in snake:
            screen.blit(snake_skin, pos)
        # Puts the apple in game
        screen.blit(apple, apple_pos)
        # Runs the game
        pygame.display.update()
