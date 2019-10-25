from random import choice
myword = choice(["code", "club", "pizza", "elmo", "nemo", "sleep", "panda", "dwarves", "awkward", "jazz", "jukebox", "pixel", "sphynx", "zombie", "mystify", "oxygen", "haphazard", "gym", "myth", "shy", "glyphs", "nymphs", "rhythm", "yggdrasil", "atlas"])

#choice = input("type a word: ")

#if choice == myword:
#	print("its a match")
#else:
#	print("not a match")


guessed = []
wrong = []
  
turns = int(input("please tipe the number of tries: ")) 

while turns > 0:

	show = ""
	for let in myword:
		if let in guessed:
			show = show + let
		else:
			show = show + "_ "

	if show == myword:
		break

	print("right now the word is: " + show)
	print(turns, "chances left")
	print("the wrong guesses so far are")
	print( wrong)

	letter = input("type a letter: ")

	if letter in myword:
		print("letter is in the word")
		guessed.append(letter)
	else:
		print("letter is not in the word")
		turns = turns - 1
		wrong.append(letter)


print(myword)

end = 0
if turns == end:
	print(" you lost")
else:
	print(" you win")





#count = 0
#for l in myword:
#	if l == letter:
#		print(count)
#	count += 1




# how to turn a string into a list
# mystring ="arizona"
# mylist = list(mystring)
#print(mylist)

# how to create a list with _ where the letters go

# guesslist = []
#for a in mylist:
#     guesslist.append("_")
# print(guesslist)

# how to replace a specific item in a list
# so say the user types r for a guess you would

# guesslist[1] = "r"
# print(guesslist)
