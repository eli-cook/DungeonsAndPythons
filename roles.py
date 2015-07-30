class Role(object):
	def __init__ (self, role_name):
		self.health = 0
		self.mana - 0
		self.weapon_slot = None
		self.base_attack_bonus = 0

class Fighter(Role):
	def __init__ (self):
		super(Fighter, self).__init__()
		self.health = 125
		self.mana = 50
		self.weapon_slot = IronShortSword()
		self.base_attack_bonus = 3

class Mage(Role):
	def __init__ (self):
		super(Mage, self).__init__()
		self.health = 75
		self.mana = 125
		self.weapon_slot = WoodenStaff()
		self.base_attack_bonus = 1

class Thief(Role):
	def __init__ (self):
		super(Mage, self).__init__()
		self.health = 100
		self.mana = 100
		self.weapon_slot = IronDagger()
		self.base_attack_bonus = 2