'''

except KeyboardInterrupt:
    GPIO.cleanup()


'''
   
import RPi.GPIO as GPIO
import time
import pygame

# Set up GPIO pins for sensors and LEDs
sensor_pin_1 = 23
led_pin_1 = 26
sensor_pin_2 = 17
led_pin_2 = 13
sensor_pin_3 = 5
led_pin_3 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin_1, GPIO.IN)
GPIO.setup(led_pin_1, GPIO.OUT)
GPIO.setup(sensor_pin_2, GPIO.IN)
GPIO.setup(led_pin_2, GPIO.OUT)
GPIO.setup(sensor_pin_3, GPIO.IN)
GPIO.setup(led_pin_3, GPIO.OUT)
last_score = 0
score = 0
throws = 5
IR1_status = True
# Loop forever
while True:
    if GPIO.input(sensor_pin_1):
        # If sensor 1 detects something, turn on LED 1
        GPIO.output(led_pin_1, GPIO.LOW)
        IR1_status = False
        IR2_status = True
    else:
        # If sensor 1 doesn't detect anything, turn off LED 1
        GPIO.output(led_pin_1, GPIO.HIGH)
        score += 1000
        throws -= 1
        time.sleep(1)
    while (IR2_status == True):
        
        if GPIO.input(sensor_pin_2):
            # If sensor 2 detects something, turn on LED 2
            GPIO.output(led_pin_2, GPIO.LOW)
            IR2_status = False
            IR3_status = True
        else:
            # If sensor 2 doesn't detect anything, turn off LED 2
            GPIO.output(led_pin_2, GPIO.HIGH)
            score += 1000
            throws -= 1
            time.sleep(1)
    while (IR3_status == True):
        
        if GPIO.input(sensor_pin_3):
            # If sensor 2 detects something, turn on LED 2
            GPIO.output(led_pin_3, GPIO.LOW)
            IR3_status = False
            IR4_status = True
        else:
            # If sensor 2 doesn't detect anything, turn off LED 2
            GPIO.output(led_pin_3, GPIO.HIGH)
            score += 500
            throws -= 1
            time.sleep(1)
            '''
    while (IR4_status == True):
        
        if GPIO.input(sensor_pin_4):
            # If sensor 2 detects something, turn on LED 2
            GPIO.output(led_pin_4, GPIO.LOW)
            IR4_status = False
            IR5_status = True
        else:
            # If sensor 2 doesn't detect anything, turn off LED 2
            GPIO.output(led_pin_4, GPIO.HIGH)
            score += 
            time.sleep(1)'''
    # Wait for a short time before repeating the loop
    time.sleep(0.1)
    last_score = score
    print(f"score: {score}")
    print(f"throws: {throws}")

GPIO.cleanup()

 
