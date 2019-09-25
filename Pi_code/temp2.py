import RPi.GPIO as GPIO

def button_callback(channel):
    if GPIO.input(26):  
        print("Rising Edge")
    else:
        print("Falling edge detected on 26")
        
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.add_event_detect(26,GPIO.BOTH,callback=button_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup()