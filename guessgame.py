import random

num = random.randint(0,10000)
guess = -1
previous = guess
tries = 0
words = ["lower","higher"]

while (guess != num):
	guess = abs(int(raw_input("Guess the magic number between 0 and 10,000?: ")))
	if (guess != previous):
		tries += 1

	diff = guess - num
	if (guess == num):
		break
	print "Your guess is " + words[diff>0] + " than the magic number."

	previous = guess

print "Guessed in " + str(tries) + " tries!"