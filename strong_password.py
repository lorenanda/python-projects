import re

def strong_pass(password):
	if re.match(r'([a-zA-Z0-9]).{8,}', password) is not None:
		print ('Strong password!')
	else:
		print ('Weak password!')