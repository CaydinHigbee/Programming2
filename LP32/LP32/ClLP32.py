
class ClLP32:
	def __init__(self, diameter):
		mat = 0.05 * diameter * diameter
		self.cost = mat + 0.75 + 1.00
	
	def costcalc(self):
		return self.cost
		
