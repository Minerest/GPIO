import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

###########GLOBALS################

R = GPIO.PWM(red, freq)
R.start(0)

B = GPIO.PWM(blue, freq)
B.start(0)

G = GPIO.PWM(green,freq)
G.start(0)

#################-----------------------#####################
#################-----------------------#####################
#################-----------------------#####################
#################-----------------------#####################

def clr(red ,green ,blue , t): #<- time is a total duration for the loop
	tInterval = t/30 #
	

	R.ChangeDutyCycle(red)
	B.ChangeDutyCycle(blue)
	G.ChangeDutyCycle(green)
	time.sleep(tINterval)

def LEDOFF():
	R.ChangeDutyCycle(0)
	B.ChangeDutyCycle(0)
	G.ChangeDutyCycle(0)

def main():
	deltaR = 0, deltaB = 0, deltaG = 0	#difference between color value and 50
	valR = 0, valB = 0, valG = 0		#actual color value picked each time
	numToSub = 0						#keep track of '<' && '>'



	random.seed()

	red = pin1
	blue = pin2
	green = pin3

	GPIO.setup(red, GPIO.OUT)
	GPIO.setup(blue, GPIO.OUT)
	GPIO.setup(green, GPIO.OUT)

	freq = 100; #HZ??? 
	try:
		k = 0
		while(k < 50):
			valR = random.randint(0,100)
			valG = random.randint(0,100)
			valB = random.randint(0,100)

			deltaR = abs(valR - 50)
			deltaG = abs(valG - 50)
			deltaB = abs(valB - 50)

			modR = deltaR%30
			modB = deltaB%30
			modG = deltaG%30

			if (valR - 50 < 0):
				dirR = 1
			else:
			 	dirR = -1
			
			if (valG - 50 < 0):
				dirG = 1
			else:
			 	dirG = -1
			 	
			if (valB - 50 < 0):
				dirB = 1
			else:
			 	dirB = -1

			for i in range(0,28):
				color(valR + modR * dirR, valB + modB*dirB, valG + modG*dirG, 30)
				valR += modR*dirR
				valG += modG*dirG			
				valB += modB*dirB
			k+=1

		LEDOFF()

	except:
		LEDOFF()

	finally:
		GPIO.cleanup()




