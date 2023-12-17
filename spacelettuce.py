#space lettuce prototype
import RPi.GPIO as GPIO
import time
import datetime
import board #output? for blinka python
import digitalio #input

Relay_Ch1 = 5
Relay_Ch2 = 6
Relay_Ch3 = 13
Relay_Ch4 = 16
Relay_Ch5 = 19
Relay_Ch6 = 20
Relay_Ch7 = 21
Relay_Ch8 = 26
Air_Pump = 12


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(Relay_Ch1,GPIO.OUT)
GPIO.setup(Relay_Ch2,GPIO.OUT)
GPIO.setup(Relay_Ch3,GPIO.OUT)
GPIO.setup(Relay_Ch4,GPIO.OUT)
GPIO.setup(Relay_Ch5,GPIO.OUT)
GPIO.setup(Relay_Ch6,GPIO.OUT)
GPIO.setup(Relay_Ch7,GPIO.OUT)
GPIO.setup(Relay_Ch8,GPIO.OUT)
GPIO.setup(Air_Pump,GPIO.OUT)

print("Setup The Relay Module is [success]")


#led = digitalio.DigitalInOut(board.D16)
#led.direction = digitalio.Direction.OUTPUT

#airpump = digitalio.DigitalInOut(board.D12)
#airpump.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.D4)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.D17)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button3 = digitalio.DigitalInOut(board.D27)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.UP

#while True:
    #led.value = not button.value # light when button is pressed!
   # led.value = button.value 



while True:
    now = datetime.datetime.now()
    if 8 <= now.hour < 20:
        print("Turn the lights on")
        print(now)
        GPIO.output(Relay_Ch1,GPIO.HIGH)
        GPIO.output(Relay_Ch2,GPIO.HIGH)
        GPIO.output(Relay_Ch3,GPIO.HIGH)
        GPIO.output(Relay_Ch4,GPIO.HIGH)
        GPIO.output(Relay_Ch5,GPIO.HIGH)
        GPIO.output(Relay_Ch6,GPIO.HIGH)
        GPIO.output(Relay_Ch7,GPIO.HIGH)
        GPIO.output(Relay_Ch8,GPIO.HIGH)

        #Lights ON
        
        GPIO.output(Relay_Ch1,GPIO.LOW)
       # print("Channel 1:The Common Contact is access to the Normal Open Contact!")

        GPIO.output(Relay_Ch2,GPIO.LOW)
       # print("Channel 2:The Common Contact is access to the Normal Open Contact!")
        
        GPIO.output(Relay_Ch3,GPIO.LOW)
       # print("Channel 3:The Common Contact is access to the Normal Open Contact!")
       
        GPIO.output(Air_Pump,GPIO.HIGH)
        time.sleep(60)
        GPIO.output(Air_Pump,GPIO.LOW)
       
        if button1.value == False:
            print("Tray1 Low Water")
            GPIO.output(Relay_Ch8,GPIO.LOW)
            time.sleep(5)
            while button1.value == False:
                print("Tray 1 Water Pump ON")
                GPIO.output(Relay_Ch4,GPIO.LOW)
        
                
        elif button2.value == False:
            print("Tray2 Low Water")
            GPIO.output(Relay_Ch7,GPIO.LOW)
            time.sleep(5)
            while button2.value == False:
                print("Tray 2 Water Pump ON")
                GPIO.output(Relay_Ch4,GPIO.LOW)
         
                
        elif button3.value == False:
            print("Tray3 Low Water")
            GPIO.output(Relay_Ch6,GPIO.LOW)
            time.sleep(5)
            while button3.value == False:
                print("Tray 3 Water Pump ON")
                GPIO.output(Relay_Ch4,GPIO.LOW)
            
                
        else:
            print("Water Check")
            GPIO.output(Relay_Ch4,GPIO.HIGH)
            GPIO.output(Relay_Ch8,GPIO.HIGH)
            GPIO.output(Relay_Ch7,GPIO.HIGH)
            GPIO.output(Relay_Ch6,GPIO.HIGH)
            #print("Air Pump on 15 seconds")
            #GPIO.output(Relay_Ch5,GPIO.LOW)
            #time.sleep(15)
            #GPIO.output(Relay_Ch5,GPIO.HIGH)
            time.sleep(360)
        
        
            
        
        
    else:
        print("turn off da lights")
        print(now)
        GPIO.output(Relay_Ch1,GPIO.HIGH)
        GPIO.output(Relay_Ch2,GPIO.HIGH)
        GPIO.output(Relay_Ch3,GPIO.HIGH)
        GPIO.output(Relay_Ch4,GPIO.HIGH)
        GPIO.output(Relay_Ch5,GPIO.HIGH)
        GPIO.output(Relay_Ch6,GPIO.HIGH)
        GPIO.output(Relay_Ch7,GPIO.HIGH)
        GPIO.output(Relay_Ch8,GPIO.HIGH)
        time.sleep(60)
    

GPIO.cleanup()

  