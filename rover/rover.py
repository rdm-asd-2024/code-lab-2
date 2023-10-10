# We want to develop a class that models a rover that can move over the Moon's surface. It should support the following features:


# It should receive commands via a string on characters R, L, U, D - that encode respectively move right, move left, move up, move down commands;

# What if I receive an unknown command? 

# Should throw an exception when moving in a certain direction would hit an obstacle;

# Who tells me where obstacles are?


class UnknownCommandException(Exception):
	def __init__(self, message):
		super().__init__(message)

class EmptyCommand(Exception):
	def __init__(self):
		super().__init__('')

class Rover:
	def __init__(self):
		self.x = 0
		self.y = 0

	def command(self, commands):
		if len(commands) == 0:
			raise EmptyCommand()
		
		for cmd in commands:
			if cmd == 'U':
				self.y += 1
			elif cmd == 'D':
				self.y -= 1
			elif cmd == 'L':
				self.x -= 1
			elif cmd == 'R':
				self.x += 1
			else:
				raise UnknownCommandException("Unknown command: {}".format(cmd))



	@property
	def position(self):
		return (self.x, self.y) 
