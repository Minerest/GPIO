import random, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

###########GLOBALS################
red = 17
green = 22
blue = 27

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

def clr(red, green, blue): #<- time is a total duration for the loop
	
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



	random.seed() 
	try:
		valR = random.randint(0,100)
		valG = random.randint(0,100)
		valB = random.randint(0,100)

		deltaR = abs(valR - 50)
		deltaG = abs(valG - 50)
		deltaB = abs(valB - 50)

		modR = deltaR%30
		modG = deltaG%30
		modB = deltaB%30

		if (valR < 50):
			dirR = 1
		else:
			dirR = -1
		if (valG < 50):
			dirG = 1
		else:
			dirG = -1
		if (valB < 50):
			dirB = 1
		else:
			dirB = -1
		for i in range(0,30):
			clr(valR + i*modR*dirR, valG + i*modG*dirG, valB + i*modB*dirB)			


		'''while(k < 30):
			print("K LOOP")
			valR = random.randint(0,100)
			valG = random.randint(0,100)
			valB = random.randint(0,100)
			print ("R G B = "+str(valR)+" "+str(valG)+" "+str(valG))
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

			for i in range(0,10):
				rd = random.randint(0,100)
				gn = random.randint(0,100)
				bl = random.randint(0,100)
				clr(rd,gn,bl)
				time.sleep(0.1)
			k+=1
			time.sleep(0.05)'''

	except Exception as e:
		print(e)
		LEDOFF()
		
main()
print("ALL DONE")
LEDOFF()
print("GPIO CLEANUP")
GPIO.cleanup()



