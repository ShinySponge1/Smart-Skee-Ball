import pygame
from pygame.locals import *
from subprocess import call
import RPi.GPIO as GPIO
import os
import random
import time


LeftButton = 4
RightButton = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(LeftButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RightButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)


pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)

#Load the previous high score from a file, if it exists
if os.path.exists("1st Place.txt"):
    with open("1st Place.txt","r") as file:
        high_score1 = int(file.read())
        file.close()
else:
    high_score1 = 0

#Load the previous high score from a file, if it exists
if os.path.exists("2nd Place.txt"):
    with open("2nd Place.txt","r") as file:
        high_score2 = int(file.read())
        file.close()
else:
    high_score2 = 0

        
#Load the previous high score from a file, if it exists
if os.path.exists("3rd Place.txt"):
    with open("3rd Place.txt","r") as file:
        high_score3 = int(file.read())
        file.close()
else:
    high_score3 = 0


screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

button_font = pygame.font.SysFont('Comic Sans MS', 80)
score_font = pygame.font.SysFont('Comic Sans MS', 100)
title_font = pygame.font.SysFont('Comic Sans MS', 120)
title = title_font.render("Skee Ball", False, (0, 0, 0))
classic_button = button_font.render("Classic", False, (0, 0, 0))
atw_button = button_font.render("Around the World", False, (0, 0, 0))
first_place = button_font.render("1st: {}".format(high_score1), False, (0, 0, 0))
second_place = button_font.render("2nd: {}".format(high_score2), False, (0, 0, 0))
third_place = button_font.render("3rd: {}".format(high_score3), False, (0, 0, 0))

pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)

running = True
while running:
    
    random_color = (random.randint(100, 240), random.randint(100, 240), random.randint(100, 240))
    highscore_title = title_font.render("Highscores:", False, (random_color))
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (144, 238, 144), [1030, 890, 250, 90])
    pygame.draw.rect(screen, (230, 100, 100), [2180, 890, 530, 90])
    
    # highscore lines
    pygame.draw.rect(screen, (random_color), [0, 720, 700, 10])
    pygame.draw.rect(screen, (random_color), [700, 0, 10, 730])
    
    # border lines
    pygame.draw.rect(screen, (random_color), [0, 0, 3440, 20])
    pygame.draw.rect(screen, (random_color), [0, 0, 20, 1440])
    pygame.draw.rect(screen, (random_color), [3420, 0, 20, 1440])
    pygame.draw.rect(screen, (random_color), [0, 1420, 3440, 20])
    
    # skeeball title lines
    pygame.draw.rect(screen, (random_color), [1520, 250, 430, 10])
    pygame.draw.rect(screen, (random_color), [1520, 250, 10, 180])
    pygame.draw.rect(screen, (random_color), [1950, 250, 10, 180])
    pygame.draw.rect(screen, (random_color), [1520, 430, 440, 10])
    
    # titles
    screen.blit(title, (1550, 300))
    screen.blit(highscore_title, (100, 80))
    screen.blit(classic_button, (1050, 900))
    screen.blit(atw_button, (2200, 900))
    screen.blit(first_place, (60, 250))
    screen.blit(second_place, (60, 350))
    screen.blit(third_place, (60, 450))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
    if GPIO.input(RightButton) == 0:
        #pygame.mixer.music.stop()
        pygame.quit()
        call(["python", "ATW.py"])
        running = False
    if GPIO.input(LeftButton) == 0:
        #pygame.mixer.music.stop()
        pygame.quit()
        call(["python", "classic.py"])
        running = False
    time.sleep(0.1)

GPIO.cleanup()
        
## click same button during game to quit ompletely
        
        
