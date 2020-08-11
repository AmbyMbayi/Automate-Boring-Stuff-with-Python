passwordFile = open('SecretPasswordFile.txt')
secretPassword = passwordFile.read()
print('enter your password: ')
typedPassword = input()
if typedPassword == secretPassword:
	print('access granted')
	if typedPassword == '12345':
		print('that password is one that idiots put')
else: 
	print('access denied')