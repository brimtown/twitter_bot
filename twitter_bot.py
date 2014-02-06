import random

class TwitterBot:
	
	CHAR_LIMIT = 140

	def __init__(self, source, level):
		self.source = source
		self.level = level

	#Finds the position of the nth occurence of a substring within a string
	def find_nth(self, string, substring, n):
		start = string.find(substring)
		while start >= 0 and n > 1:
			start = string.find(substring, start+len(substring))
			n -= 1
		return start

	#Returns index of an upper-case letter in the string
	def pick_random_character(self, string):
		initial_char = "a"
		if string != "":
			while not initial_char.isupper():
				rand_value = random.randint(0, len(string))
				initial_char = string[rand_value]
			return rand_value

	#Generates a string of length 'self.level', guaranteed to be in the source
	#and starting with an upper-case letter
	def generate_target(self):
		start = self.pick_random_character(self.source)
		return self.source[start:start+self.level]

	#Given a target, probabilistically generates the next character
	def generate_next_char(self, target):
		if len(target) != self.level:
			return "x"

		if self.source.find(target) == -1:
			return "~"

		num_matches = self.source.count(target)

		#If there is more than once occurence of the target
		#then select a random instance
		if(num_matches > 1):
			random_match = random.randint(1, num_matches)
			pos = self.find_nth(self.source, target, random_match)
		else:
			pos = self.source.find(target)

		#If there are no characters after the target, then recall the
		#function until a different instance is chosen
		if pos+self.level < len(self.source):
			next_char = self.source[pos+self.level]
			return next_char
		else:
			return self.generate_next_char(target)	

	#Returns a <=140 character string generated from the source text
	def tweet(self):
		target = self.generate_target()
		status = target
		for i in range(self.CHAR_LIMIT-len(target)):
			next_char = self.generate_next_char(target)
			target = target[1:] + next_char
			status += next_char
		return status