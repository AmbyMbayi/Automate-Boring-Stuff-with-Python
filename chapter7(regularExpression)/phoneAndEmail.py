'''
say you have task of finding every phone number and email address
in a long web page or document.
'''

#step 1: create a Regex for phone numbers

import pyperclip, re
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?					#area code
	(\s|-|\.)? 							#separator
	(\d{3}) 							#first 3 digits
	(\s|-|\.) 							# separtor
	(\d{4}) 							# last four digits
	(\s*(ext|x|ext.)\s*(\d{2, 5}))? 	#extension
	)''', re.VERBOSE)

#step 2: create a Regex for Email Address

emailRegex = re.compile(r'''(
		[a-zA-Z0-9._%+-]+ 	#username
		@       			# @ sysmbol
		[a-zA-Z0-9.-]+    	#domain name
		(\.[a-zA-Z]{2,4}) 	#dot-something
	)''', re.VERBOSE)

#step 3: find all matches in the clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] !='':
		phoneNum += 'x' + groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])


#copy results to the clipboard
if len(matches)> 0:
	pyperclip.copy('\n'.join(matches))
	print('copied to clipboard: ')
	print('\n'.join(matches))

else: 
	print('no phone number or email address found')