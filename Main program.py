from machine import Pin
import time

# Initialize pins
pir_sensor = Pin(15, Pin.IN)   # PIR motion sensor on GPIO 15
buzzer = Pin(9, Pin.OUT)      # Buzzer on GPIO 16
led = Pin(18, Pin.OUT)         # LED on GPIO 17

# Set initial states
buzzer.off()
led.off()

print("Starting motion detection system...")

# Main loop to check for motion
while True:
    if pir_sensor.value() == 1:   # If motion is detected
        print("Motion detected!") # Print "Motion detected!"
        led.on()                  # Turn on LED
        buzzer.on()               # Turn on buzzer
        time.sleep(1)             # Keep alarm on for 1 second
        led.off()                 # Turn off LED
        buzzer.off()              # Turn off buzzer
    else:
        led.off()                 # Ensure LED is off
        buzzer.off()              # Ensure buzzer is off
    
    time.sleep(0.1)               # Short delay before the next check
