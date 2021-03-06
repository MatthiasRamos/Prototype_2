from AtlasI2C import *
import time

class EC:

	def __init__(self):
		self.EC_I2C_address= 0x64
		self.device = AtlasI2C(self.EC_I2C_address)

	def read(self):
		EC = self.device.query("R").split()[2]
		print("La conductivité vaut " + str(EC) + " uS")

	def dry(self):
		self.device.query("Cal,dry")

	def low(self):
		self.put("de conductivité 1413 uS")
		self.wait()
		self.device.query("Cal,low,1413")

	def high(self):
		self.put("de conductivité 12880 uS")
		self.wait()
		self.device.query("Cal,high,12880")

	def calibration(self):
		self.dry()
		self.low()
		self.high()
		print("La sonde est calibrée")


	def put(self,solution)
		print("Mettre la sonde pH dans la solution " + solution)
		isPut = False
		while !isPut:
			rep = input("Rentrer y si c'est fait")
			isPut = (rep=="y")

	def wait(self)
		print("Attendre 2 minutes avec la sonde dans la solution")
		time.sleep(120)