import pygame

# Starts pygame
pygame.init()

# Tuple passed in is size of game screen
window = pygame.display.set_mode((500, 500))

# Set windows name
pygame.display.set_caption("First Game, who hoo!!!")

# Character stats
x = 50
y = 50
width = 40
height = 60
vel = 5 # Velocity, character speed

run = True
while run:
    pygame.time.delay(10) # wait 100 ms aka .1 seconds

    # Checks for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        print("Left")

    if keys[pygame.K_RIGHT]:
        x += vel
        print("Right")

    if keys[pygame.K_UP]:
        y += vel
        print("Up")

    if keys[pygame.K_DOWN]:
        y -= vel
        print("Down")

    # Where to draw, color of character and character dimensions
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit