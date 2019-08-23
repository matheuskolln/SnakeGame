import random


# Create a function to draw a random position for X and Y
def pos():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x//10 * 10, y//10 * 10


# Create a function to draw a random int in range(0, 3), that will represent a direction
def direction():
    randomdirection = random.randint(0, 3)
    return randomdirection
