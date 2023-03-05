# 1. The first question will ask about reversing only the words in a given sentence.

sentence = "Hello Logichive how are you"
for i in (sentence):
	if ' '.join(i.split(' ')[::1]):
		print(i, end='')