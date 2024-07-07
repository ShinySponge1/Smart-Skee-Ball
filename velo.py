import RPi.GPIO as GPIO
import time
import pygame

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)  # First sensor connected to GPIO pin 17
GPIO.setup(4, GPIO.IN)  # Second sensor connected to GPIO pin 18

# Initialize variables
start_time = 0
end_time = 0
distance = 21  # Distance between sensors in inches
velocity = 0

# Define callback functions for sensor events
def sensor1_callback(channel):
    global start_time
    start_time = time.time()  # Record the start time when the first sensor is triggered
    print('1on')

def sensor2_callback(channel):
    global end_time, velocity
    end_time = time.time()  # Record the end time when the second sensor is triggered
    elapsed_time = end_time - start_time
    velocity = distance / elapsed_time  # Calculate the velocity of the ball

BEAM_PIN = 4

def break_beam_callback():
    if GPIO.input(BEAM_PIN):
        print("beam unbroken")
    else:
        print("beam broken")

GPIO.setmode(GPIO.BCM)

# Set up interrupts for sensor events
GPIO.add_event_detect(5, GPIO.RISING, callback=sensor1_callback)
GPIO.add_event_detect(4, GPIO.RISING, callback=sensor2_callback)

# Initialize Pygame
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont(None, 48)
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Velocity")

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                GPIO.cleanup()
                exit()
        import RPi.GPIO as GPIO
        GPIO.setup(BEAM_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(BEAM_PIN, GPIO.BOTH, callback=break_beam_callback)

        # Draw the velocity on the Pygame screen
        screen.fill((255, 255, 255))
        if velocity is not None:
            velocity_str = "{:.2f} inches/second".format(velocity)
            text_surface = FONT.render(velocity_str, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(text_surface, text_rect)
        
        pygame.display.update()
        
        time.sleep(2)  # Wait for a short time to avoid excessive CPU usage

except KeyboardInterrupt:
    # Clean up the GPIO pins and Pygame on exit
    pygame.quit()
    GPIO.cleanup()
