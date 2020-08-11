import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'it is certain'

	elif answerNumber == 2:
		return 'it is decidely so'
	elif answerNumber == 3:
		return 'Yes'

	elif answerNumber == 4:
		return 'reply hazy try again'
	elif answerNumber == 5:
		return 'Ask again later'
	elif answerNumber == 6:
		return 'my repy is no'

	elif answerNumber == 7:
		return 'concentrate an ask again'

	elif answerNumber == 8:
		return 'outloo not so good'
	elif answerNumber == 9:
		return 'very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)