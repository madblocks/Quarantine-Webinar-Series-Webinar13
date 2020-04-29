# LED - (A, K) - (+VE, -VE) 
# LED CAN BE CONNECTED - HIGH (ON), LOW (OFF)
# LED is connected to GPIO2

import RPi.GPIO as GPIO  # COMES WITH OS

# RPi - 2 Numbering Standards - GPIO2 (BCM Numbering Standard), 3 (BOARD Numbering Standard)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # To configure Numbering Standard of RPi

# LED - CONFIGURATION
GPIO.setup(2,GPIO.OUT) # LED - OUTPUT PERIPHERAL

# ASSIGN LOGIC -> LED WILL BE ON AND OFF
GPIO.output(2,0) # Assigning Logic to GPIO2, - 1 (HIGH)

