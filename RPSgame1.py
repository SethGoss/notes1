# seth
# rock paper scissors
# added a comment
# variabls
import random

ps = 0
cs = 0
ties = 0
copCh = ["r", "p", "s"]

# print messege
print("Welcom to Rock paper scissors")
# prompt player name
pname = input("Whats your name ")





# welcom message
# game loop

# final score
def Prs():
	#write message
	print("the score is: ")
	# player score
	print(pname + ": " + str(ps))
	# coputer score
	print("computer: " + str(cs))
	# ties
	print("Ties: " + str(ties))

#game loop
# make a forever loop
while True:
	# print current score
	Prs()
	# prompt for chouse (r (rock), p (paper) s q)
	pCh = input("enter r (rock), p (paper), s (scissors) or q (to quit): ")
	# deal with player entering q
	if pCh == "q":
		break
	# get computers choiceq (random)
	cChoice = random.choice(copCh)
	#compare for r
	if pCh == "r":
		print(pname + " picked rock")
	# if computer is r
		if cChoice == "r":
			print("computer picked rock ")
			print("this is a tie")
			ties = ties + 1
		# if p
		elif cChoice == "p":
			print("computer picked paper")
			print("paper covers rock")
			cs = cs + 1
		#if s
		else:
			print("computer picked scissors ")
			print("rock brakes scissors")
			ps = ps + 1
	#p
	elif pCh == "p":
		print(pname + " picked paper")
		if cChoice == "p":
			print("computer picked paper")
			print("this is a tie")
			ties = ties + 1
		elif cChoice == "s":
			print("computer picked scissors")
			print("scissors cuts paper")
			cs = cs + 1
		else:
			print("computer picked rock")
			print("paper covers rock")
			ps = ps + 1
	#s
	elif pCh == "s":
		print(pname + " picked scissors")
		if cChoice == "s":
			print("computer picked scissors")
			print("this is a tie")
			ties = ties + 1
		elif cChoice == "r":
			print("computer picked rock")
			print("rock brakes scissors")
			cs = cs + 1
		else:
			print("computer picked paper")
			print("scissors cuts paper")
			ps = ps + 1
	# eney thing else
	else:
		print("lern how to reed")