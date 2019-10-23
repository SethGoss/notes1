# Seth Goss
# p:4

# variable declaration and assignment
#examples
mynum = 12 # integer tipe
mystring = "12" # string tipe
mynum + 3 # ok

# make a variable and assige it the value of your favret move
# print "my favret movie is " followed by the variable
mov = "Gods not dead"
print("my favorite movie is " + mov)

# while loops
# example - print from 1 to 10
x = 1
while x <= 10:
	print(x)
	x = x + 1

# count doun from 100
y = 100
while y >= 1:
	print(y)
	y = y -1

# string concatenation
# means putting two strings together
#example
myname = "Seth"
print("hello " + myname)

# input
# example
yourname = input("what is your name? ")
print("hello " + yourname + " have a nice day")

# ask for two numbers, add them and print the sum
m = "please enter two numbers "
num = input("enter your first number: ")
numtwo = input("enter your second number: ")
number = int(num) + int(numtwo)
print("The sum of your numbers is " + str(number))

# if / else statments
# example
n = int(input("enter a number: "))
if n > 100:
	print("your number is more than 100")
elif n == 100:
	print("your number is equal to 100")
else:
	print("your number is less than 100 ")

# ask if today is your birthday
# if yes print happy birthday
bday = input("is today your birthday (yes/no): ")
if bday == "yes":
	print("happy birthday")
elif bday == "no":
	print("have a nice day anyway")
else:
	print("lern how to read derections")





	