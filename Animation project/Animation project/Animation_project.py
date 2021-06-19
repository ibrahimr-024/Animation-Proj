# "Valcano Car"
# Ibrahim Rashid
# 2021/03/04
# ICS3UC-04


import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()
yellow = (252, 219, 3)
grey = (89, 82, 78)
brown = (232, 126, 56)
dark_Green = (92, 143, 4)
orange = (255, 98, 0)
font = pygame.font.SysFont('Calibri', 25, True, False)
# Set the width and height of the screen [width, height]
size = (1920, 1080)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")


# Define functions for car, ufo and clouds

# Create function to draw car
def draw_Car(screen, x_coord):
    pygame.draw.rect(screen, RED, [680 + x_coord, 780, 500, 75])
    pygame.draw.rect(screen, RED, [900 + x_coord , 700, 125, 100])
    pygame.draw.polygon(screen, RED, [[890 + x_coord, 780], [900 + x_coord, 780], [900 + x_coord, 700]])
    pygame.draw.polygon(screen, RED, [[1025 + x_coord, 700], [1025 + x_coord, 780], [1100 + x_coord, 780]])
    pygame.draw.rect(screen, grey, [915 + x_coord, 720, 75, 50])
    pygame.draw.rect(screen, grey, [1000 + x_coord, 725, 45, 45])
    pygame.draw.line(screen, BLACK, [885 + x_coord, 780], [885 + x_coord, 853], 5)
    pygame.draw.line(screen, BLACK, [995 + x_coord , 700], [995 + x_coord, 853], 5)
    pygame.draw.line(screen, BLACK, [1100 + x_coord, 780], [1100 + x_coord, 853], 5)
    pygame.draw.circle(screen, BLACK,(800 + x_coord, 880), 40)
    pygame.draw.circle(screen, BLACK, (1100 + x_coord , 880), 40)
       
    # Text
    text_B = font.render('"AHHHH ITS RAINING LAVA!!!"', True, BLACK)
    screen.blit(text_B, [900 + x_coord, 650])
        
    if left == True:
        text_A = font.render('"WHY AM I DRIVING TOWARDS THE LAVA"', True, BLACK)
        screen.blit(text_A, [900 + x_coord, 500])
    

# function to draw UFO
def UFO(screen, x, y):
    pygame.draw.polygon(screen, RED, [[x + 10, y + 18], [x + 20, y + 28], [x + 30, y + 18]])
    pygame.draw.ellipse(screen, grey, [x, y, 40, 20])
    pygame.draw.circle(screen, BLACK,(x + 18 , y + 3), 10)

# function for smoke clouds 
def smoke_Cloud(screen):
    for item in ellipse_Cloud:
        pygame.draw.ellipse(screen, grey, [item[0], item[1], item[2], item[3]])
            
        if 175 < pos[0] < 335 and 125 < pos[1] < 305:
            item[0] = 0
            item[1] = 0
            item[2] = 0
            item[3] = 0
            
        elif pos[0] != item[0] and pos[0] != item[1]:
            item[0] = random.randrange(175,256)
            item[1] = random.randrange(125, 225)
            item[2] = random.randrange(70, 160)
            item[3] = random.randrange(60, 130)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initiliaze variables
lava_x_change = 0
lava_y_change = 0
lava_x_change_1 = 0
pool_width_change = 0
stop = False
left = False
x_coord = 0
car_x_speed = 0
# Create list for random generated lava and clouds
rain_Lava = []
for i in range(50):
    x = random.randrange(0, 1920)
    y = random.randrange(0 ,1080)
    rain_Lava.append([x, y])

ellipse_Cloud = []
for f in range(25):
    l = random.randrange(175,256)
    m = random.randrange(125, 225)
    n = random.randrange(70, 160)
    o = random.randrange(60, 130)
    ellipse_Cloud.append([l, m, n, o])


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- event loop for pressing left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car_x_speed = 8
            if event.key == pygame.K_LEFT:
                left = True
                car_x_speed =-8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car_x_speed = 0
            if event.key == pygame.K_LEFT:
                left = False
                car_x_speed = 0

    # --- Game logic should go here
    x_coord += car_x_speed
    lava_x_change -= 5
    lava_y_change -= 5
    lava_x_change_1 += 5
    lava_x_a = 50 + lava_x_change
    lava_y_a = 220 + lava_y_change
    lava_x_b = 150 + lava_x_change
    lava_y_b = 300 + lava_y_change
    lava_y_c = 300 + lava_y_change
    lava_y_d = 200 + lava_y_change
    lava_y_e = 300 + lava_y_change
    lava_x_f = 400 + lava_x_change_1
    lava_y_f = 200 + lava_y_change

    pos = pygame.mouse.get_pos()
    x_Mouse = pos[0]
    y_Mouse = pos[1]
    # Conditions for if lava go off screen
    if lava_y_f < 0:
        lava_x_change = 0
        lava_y_change = 0


    if lava_x_f < 425:
        lava_x_change_1 = 0


    # --- Screen-clearing code goes here

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)

    # --- Drawing code should go here

    # Grass
    pygame.draw.rect(screen, GREEN, [0, 540, 1920, 370])

    # Road
    pygame.draw.rect(screen, grey, [0, 910, 1920, 170])
    for offset in range(0, 1920, 200):
        pygame.draw.rect(screen, yellow, [0 + offset, 980, 90, 30])



    # Tree
    pygame.draw.rect(screen, brown, [ 1450, 660, 50,170])
    pygame.draw.circle(screen, dark_Green, (1475, 570), 100)

    # Sun
    pygame.draw.circle(screen, yellow, (1800, 100), 100)

    # Lava
    pygame.draw.line(screen, orange, [lava_x_a, lava_y_a], [lava_x_b, lava_y_b], 5)
    pygame.draw.line(screen, orange, [200, lava_y_c], [200, lava_y_d], 5)
    pygame.draw.line(screen, orange, [325, lava_y_e], [lava_x_f, lava_y_f], 5)
    
    # repetition for raining lava
    for item in rain_Lava:
        item[1] += 10
        pygame.draw.line(screen, orange, [item[0], item[1]], [item[0], item[1] + 40] , 5)

        if item[1] > 1080:
            item[1] = 0
            item[0] = random.randrange(1920)
    
    # Volcano
    pygame.draw.polygon(screen, brown, [[100, 540], [200, 300], [300, 540]])
    pygame.draw.circle(screen, RED, (200, 311), 10)
    pygame.draw.line(screen, RED, [200, 310], [225, 400], 10)
    pygame.draw.line(screen, orange, [200, 310], [175, 415], 10)
    pygame.draw.line(screen, RED, [200, 310], [200, 420], 13)
    
    # Draw car
    draw_Car(screen, x_coord)
    
    # Draw UFO
    UFO(screen, x_Mouse, y_Mouse)
    
    # Draw smoke clouds
    smoke_Cloud(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    
    # --- Limit frames per second
    clock.tick(60)
    pygame.mouse.set_visible(0)

# Close the window and quit.
pygame.quit()

