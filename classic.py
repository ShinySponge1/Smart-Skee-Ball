#imports
import RPi.GPIO as GPIO
import time
import pygame
import sys
import os
import random
from subprocess import call
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
 
# Set up GPIO pins for sensors and LEDs
sensor_pin_1 = 17
led_pin_1 = 22
sensor_pin_2 = 16
led_pin_2 = 21
sensor_pin_3 = 13
led_pin_3 = 20
sensor_pin_4 =  12
led_pin_4 = 19
sensor_pin_5 = 6
led_pin_5 = 18

# Initialize the sensors and LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin_1, GPIO.IN)
GPIO.setup(led_pin_1, GPIO.OUT)
GPIO.setup(sensor_pin_2, GPIO.IN)
GPIO.setup(led_pin_2, GPIO.OUT)
GPIO.setup(sensor_pin_3, GPIO.IN)
GPIO.setup(led_pin_3, GPIO.OUT)
GPIO.setup(sensor_pin_4, GPIO.IN)
GPIO.setup(led_pin_4, GPIO.OUT)
GPIO.setup(sensor_pin_5, GPIO.IN)
GPIO.setup(led_pin_5, GPIO.OUT)
GPIO.setup(LeftButton, GPIO.IN)
GPIO.setup(RightButton, GPIO.IN)

# Getting the previous highscores
if os.path.exists("1st Place.txt"):
    with open("1st Place.txt","r") as file:
        high_score1 = int(file.read())
else:
    high_score1 = 0
    
if os.path.exists("2nd Place.txt"):
    with open("2nd Place.txt","r") as file:
        high_score2 = int(file.read())
else:
    high_score2 = 0
    
if os.path.exists("3rd Place.txt"):
    with open("3rd Place.txt","r") as file:
        high_score3 = int(file.read())
else:
    high_score3 = 0
     
#declare variables
score = 0
throws = 5
all_holes = [sensor_pin_1, sensor_pin_2, sensor_pin_3, sensor_pin_4, sensor_pin_5]

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the window
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
pygame.display.set_caption("Classic")

# Set up the font
font = pygame.font.Font(None, 150) 

# Set up variables to track the score and throws remaining
score = 0
throws = 5

# IR status booleans
IR2_status = False
IR3_status = False
IR4_status = False
IR5_status = False

# Loop forever
game = True
while game == True:
    if throws >= 1:
        # Clear the screen
        screen.fill((255, 255, 255))
        
        #reset made hole variable
        made_hole = None
    
        if GPIO.input(sensor_pin_1):
            # If sensor 1 doesn't detect anything, turn off LED 1
            GPIO.output(led_pin_1, GPIO.LOW)
            IR1_status = False
            IR2_status = True
        else:
            # If sensor 1 detects something, turn on LED 1
            GPIO.output(led_pin_1, GPIO.HIGH)
            score += 1000
            throws -= 1
            made_hole = sensor_pin_1
            time.sleep(1)

        
        while (IR2_status == True):
        
            if GPIO.input(sensor_pin_2):
                # If sensor 2 doesn't detect anything, turn off LED 2
                GPIO.output(led_pin_2, GPIO.LOW)
                IR2_status = False
                IR3_status = True
            else:
                # If sensor 2 detects something, turn on LED 2

                GPIO.output(led_pin_2, GPIO.HIGH)
                score += 1000
                throws -= 1
                made_hole = sensor_pin_2
                time.sleep(1)

            
        while (IR3_status == True):
        
            if GPIO.input(sensor_pin_3):
                # If sensor 3 doesn't detect anything, turn off LED 2
                GPIO.output(led_pin_3, GPIO.LOW)
                IR3_status = False
                IR4_status = True
            else:
                # If sensor 3 detects something, turn on LED 2
                GPIO.output(led_pin_3, GPIO.HIGH)
                score += 500
                throws -= 1
                made_hole = sensor_pin_3
                time.sleep(1)
                
        while (IR4_status == True):
            
            if GPIO.input(sensor_pin_4):
                # If sensor 4 doesn't detect anything, turn off LED 2
                GPIO.output(led_pin_4, GPIO.LOW)
                IR4_status = False
                IR5_status = True
            else:
                # If sensor 4 detects something, turn on LED 2
                GPIO.output(led_pin_4, GPIO.HIGH)
                score += 250
                throws -= 1
                made_hole = sensor_pin_4
                time.sleep(1)
                
        while (IR5_status == True):
            
            if GPIO.input(sensor_pin_5):
                # If sensor 5 doesn't detect anything, turn off LED 2
                GPIO.output(led_pin_5, GPIO.LOW)
                IR5_status = False
            else:
                # If sensor 5 detects something, turn on LED 2
                GPIO.output(led_pin_5, GPIO.HIGH)
                throws -= 1
                made_hole = None
                time.sleep(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                                                                                 
        if made_hole != None:
            hole_text = font.render("Scored!!", True, (0, 0, 255))
            screen.blit(hole_text, (1350, 300))

        # Draw the score and throws remaining text
        score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
        screen.blit(score_text, (1350, 500))

        throws_text = font.render("Throws remaining: {}".format(throws), True, (0, 0, 0))
        screen.blit(throws_text, (1350, 600))
        
        # border lines
        pygame.draw.rect(screen, ((0, 0, 255)), [0, 0, 3440, 20])
        pygame.draw.rect(screen, ((0, 0, 255)), [0, 0, 20, 1440])
        pygame.draw.rect(screen, ((0, 0, 255)), [3420, 0, 20, 1440])
        pygame.draw.rect(screen, ((0, 0, 255)), [0, 1420, 3440, 20])
        
        
        # Update the display
        pygame.display.update()
    else:
        end_time = 0
        
        if score >= high_score1:
            new_highscore1 = score
            with open("1st Place.txt", "w") as file:
                file.write(str(new_highscore1))
                file.close()
            with open("2nd Place.txt", "w") as file:
                file.write(str(high_score1))
                file.close()
            with open("3rd Place.txt", "w") as file:
                file.write(str(high_score2))
                file.close()

                
        elif (score < high_score1) and (score >= high_score2):
            new_highscore2 = score
            with open("2nd Place.txt", "w") as file:
                file.write(str(new_highscore2))
                file.close()
            with open("3rd Place.txt", "w") as file:
                file.write(str(high_score2))
                file.close()
                
                
        elif (score < high_score2) and (score > high_score3):
            high_score3 = score
            with open("3rd Place.txt", "w") as file:
                file.write(str(high_score3))
                file.close()
                
        while end_time < 10:
            random_color = (random.randint(100, 240), random.randint(100, 240), random.randint(100, 240))
            screen.fill((255, 255, 255))
            throws_text = font.render("Game Over!", True, (0, 255, 0))
            screen.blit(throws_text, (1350, 300))
            score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
            screen.blit(score_text, (1350, 500))
   
             # border lines
            pygame.draw.rect(screen, (random_color), [0, 0, 3440, 20])
            pygame.draw.rect(screen, (random_color), [0, 0, 20, 1440])
            pygame.draw.rect(screen, (random_color), [3420, 0, 20, 1440])
            pygame.draw.rect(screen, (random_color), [0, 1420, 3440, 20])
            
            # Update the display
            pygame.display.flip()
            end_time += 0.5
            time.sleep(0.1)
        pygame.quit()
        GPIO.cleanup()
        call(["python", "start_menu.py"])
        
            

