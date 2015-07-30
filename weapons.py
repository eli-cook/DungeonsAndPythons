class Weapon(object):
	def __init__ (self):
		self.name = None
		self.damage = 0
		self.weight = 0
		self.descrip = None
		self.special = None

class IronDagger(Weapon):
	def __init__ (self):
		super(Weapon, self).__init__()
		self.name = "Iron Dagger"
		self.damage = [5,10]
		self.weight = 1
		self.descrip = "Just an old dagger, sharp though."

class WoodenStaff(Weapon):
	def __init__ (self):
		super(Weapon, self).__init__()
		self.name = "Wooden Staff"
		self.weight = 3
		self.damage =[2,4]
		self.descrip = "It's really just a stick"

class IronShortSword(Weapon):
	def __init__ (self):
		super(Weapon,self).__init__()
		self.name = "Iron Shortsword"
		self.weight = 2
		self.damage = [7,8]
		self.descrip = "A pretty rusty old sword"