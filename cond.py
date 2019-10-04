print("welcome to movie Bot")

age = int(input("how old are you? "))
if age > 17:
	print("you can see an R rated movie")
else:
	print("you can not see a R rated movie")

print("have a good day")

num = 4
ch = int(input("pick a number between 1 and 10 "))
if num == ch:
	print("you gest it")
elif ch < num:
	print("too low")
else:
	print("too high")

# == (equal to), <, >, <=, >=, !=(not equal to)

bday = input("is today your birthday (yes/no): ")
if bday == "yes":
	print("happy birthday")
elif bday == "no":
	print("have a nice day anyway")
else:
	print("lern how to read derections")