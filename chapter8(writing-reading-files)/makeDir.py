import os, random


#make a new directory
#os.makedirs('C:\\Users\\Faded\\Desktop\\python\chapter8(writing-reading-files)\\kenya')

#writing to a file
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

#
capitals = {
	'Kenya': 'Nariobi',
	'Uganda': 'Kampala',
	'Tanzania': 'Dodoma',
	'Sudan': 'Khartoum'
}

for quizNum in range(3):
	quizFile = open('quiz%s.txt' % (quizNum + 1), 'w')
	quizFile.write('Name: \n\nDate: \n\nPeriod: \n\n')
	quizFile.write((' ' * 20 ) + 'Question %s' % (quizNum + 1))
	quizFile.write('\n\n')

	countries = list(capitals.key())
	random.shuffle(countries)

	for question in range(3):
		correctAnswer = capitals[countries[question]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
	quizFile.close()