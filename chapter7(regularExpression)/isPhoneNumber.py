#finding patterhn of Text without regular Expression
import re
def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False

	if text[3] !='-':
		return False

	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] !='-':
		return False

	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


message = 'call me at 415-555-1011 tommor. 415-555-9999 is my office number'

for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('phone number found: ' + chunk)
print('done')

#using regex
phoneNumberRegex  = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('my number is 415-555-4242')
print('phone number found: ' + mo.group())


#grouping with parenthesis

phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phone = phoneNumber.search('My phone number is 415-555-4242')
print(phone.group(1))
print(phone.group(2))
print(phone.group(0))
print(phone.group())

#matchng multiple groups with the pipe
heroRegex = re.compile(r'Battman|Tina Fey')
mo1 = heroRegex.search('Battman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Battman')
print(mo2.group())

#matching multiple Groups with the pipe

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
bat = batRegex.search('Batmobile lost a wheel')
print(bat.group())
print(bat.group(1))

#optional Matching with the Question Mark

batRegex  = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('the adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventres of Batwoman')
print(mo2.group())


phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

#matching zero or more with the star

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The adventure of Batwoman')
print(mo1.group())

mo3 = batRegex.search('the adventure of Batwowowowowoman')
print(mo3.group())

#matching one or More with the plus
batRegex = re.compile(r'Bat(wo)+man')
mo5 = batRegex.search('The adventures of Batman')
#print(mo5.group())
#print(mo1.group())

mo2 = batRegex.search('the adventures of Batwowowowowoman')
print(mo2.group())

mo3 = batRegex.search('the adventures of Batman')
mo3 == None
print(mo3)


#matching specific Repetitions with Curly Brackets

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
mo2 == None
print(mo2)

#greedy and Nongreedy Maching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

#character Classes
xmasRegex = re.compile(r'\d+\s\w+')
xams = xmasRegex.findall('12 drummers, 11 pipers, 10 Lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 brisds, 3 hens, 2 doves, 1 partridge')

print(xams)

#making your own Character classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowel = vowelRegex.findall('RoboCop eats baby food. BABY FOOD')
print(vowel)

#negating the characters by anding (^)
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consta = consonantRegex.findall('RoboCop eats batRegex food. BABY FOOD')
print(consta)

#the wildcard character

atRegex = re.compile(r'.at')
atReg = atRegex.findall('the cat in the hat sat on the flat mat')
print(atReg)