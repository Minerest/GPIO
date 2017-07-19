import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

###########GLOBALS################
blue = 17
red = 22
green = 27

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

R = GPIO.PWM(red, 100)
R.start(0)

B = GPIO.PWM(blue, 100)
B.start(0)

G = GPIO.PWM(green,100)
G.start(0)

#Function to quickly use the python terminal after running this script.
def startGPIO(red, green, blue):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red, GPIO.OUT)
        GPIO.setup(blue, GPIO.OUT)
        GPIO.setup(green, GPIO.OUT)
        R = GPIO.PWM(red, 100)
        R.start(0)

        B = GPIO.PWM(blue, 100)
        B.start(0)

        G = GPIO.PWM(green,100)
        G.start(0)

#################-----------------------#####################
#################-----------------------#####################
#################-----------------------#####################
#################-----------------------#####################

def clr(red, green, blue): 
	#Try to prevent a crash if a bad value is passed in.
	if (red > 100):
		red = 100
	elif (red < 0):
		red = 0
	if (blue > 100):
		blue = 100
	elif (blue < 0):
		blue = 0
	if (green > 100):
		green = 100
	elif (green < 0):
		green = 0
	
	print("CHANGE DUTY CYCLE")
	R.ChangeDutyCycle(red)
	B.ChangeDutyCycle(blue)
	G.ChangeDutyCycle(green)	

def LEDOFF():
	R.ChangeDutyCycle(0)
	B.ChangeDutyCycle(0)
	G.ChangeDutyCycle(0)

def main():
	print("STARTING MAIN")
	deltaR = 0
	deltaB = 0
	deltaG = 0	#difference between color value and 50
	valR = 0
	valB = 0
	valG = 0		#actual color value picked each time
	numToSub = 0						#keep track of '<' && '>'
	cycles = 30


	random.seed() 
	try:
		valR = random.randint(0,100)
		valG = random.randint(0,100)
		valB = random.randint(0,100)

		deltaR = abs(valR - 50)
		deltaG = abs(valG - 50)
		deltaB = abs(valB - 50)

		modR = deltaR%cycles
		modG = deltaG%cycles
		modB = deltaB%cycles

		r = valR
		g = valG
		b = valB
		print("test")
		
		for i in range(0,cycles):
			if (valR < 50):
				r = r + ((deltaR/cycles) * 2)
			else:
				r = r - ((deltaR/cycles) * 2)

			if (valG < 50):
				g = g + ((deltaG/cycles) * 2)
			else:
				g = g - ((deltaG/cycles) * 2)

			if (valB < 50):
				b = b + ((deltaB/cycles) * 2)
			else:
				b = b - ((deltaB/cycles) * 2)

			clr(r,g,b)
			print("R= "+str(r)+" g= "+str(g)+" b= "+str(b))
			time.sleep(0.05)
		for i in range(0, 50):
			clr(100-i*2,i*2,i*2)
			print(i)
			time.sleep(0.05)

	except Exception as e:
		print(e)
		LEDOFF()
		
main()
print("ALL DONE")
LEDOFF()
print("GPIO CLEANUP")
GPIO.cleanup()



