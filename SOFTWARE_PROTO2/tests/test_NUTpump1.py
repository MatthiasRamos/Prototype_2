import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
NUTpump1_pin = ...                     #Flora Micro/Mato
GPIO.setup(NUTpump1_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(NUTpump1_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(NUTpump1_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(NUTpump1_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(ANUTpump1_pin, GPIO.LOW)
