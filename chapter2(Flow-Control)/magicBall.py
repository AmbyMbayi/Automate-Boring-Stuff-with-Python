import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'it is certain'

	if answerNumber == 2:
		return 'it is decidely so'

r = random.randint(1,2)
fortune = getAnswer(r)
print(fortune)