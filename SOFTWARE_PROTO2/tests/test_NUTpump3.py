import RPI.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
NUTpump3_pin = ...                     #FloraBloom
GPIO.setup(NUTpump3_pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.output(NUTpump3_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(NUTpump3_pin, GPIO.LOW)
time.sleep(10)
GPIO.output(NUTpump3_pin, GPIO.HIGH)
time.sleep(10)
GPIO.output(NUTpump3_pin, GPIO.LOW)
