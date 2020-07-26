import pyperclip
import re

#Text containing email's and phone number to be pasted from clipboard
text = str(pyperclip.paste())

email_regex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+      # Username
	@                      # symbol
	[a-zA-Z0-9.-]+         # domain name
	(\.[a-z{2,4}])         # dot-something
	)''', re.VERBOSE)

match = [] # list for storing all the matched found

for groups in email_regex.findall(text):
	match.append(groups[0])

# Copy results to clipboard

if len(match) > 0:
	pyperclip.copy('\n'.join(match))
	print ('Copied to clipboard')
	print ('\n'.join(match))
else:
	print ('Nothing found')
