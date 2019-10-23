# Name: Seth Goss
# Period: 4
# Dice Rolling Simulator
import random

rolls = int(input("how many rolls "))

aa = 0
ab = 0
ac = 0
ad = 0
ae = 0
af = 0
x = 1

while x <= rolls:
	ran = random.randint(1,6)
	print("role number: " + str(x) + " rolled a " + str(ran))
	if ran == 1:
		aa = aa + 1
	elif ran == 2:
		ab = ab + 1
	elif ran == 3:
		ac = ac + 1
	elif ran == 4:
		ad = ad + 1
	elif ran == 5:
		ae = ae + 1
	else:
		af = af + 1
	x = x + 1
print("nomber of rolls = " + str(x-1))

print("nomber of 1s = " + str(aa))
print("nomber of 2s = " + str(ab))
print("nomber of 3s = " + str(ac))
print("nomber of 4s = " + str(ad))
print("nomber of 5s = " + str(ae))
print("nomber of 6s = " + str(af))

Z = 100/(int(aa)+int(ab)+int(ac)+int(ad)+int(ae)+int(af))
print('Percent of 1s: '+str(aa*Z)+'%')
print('Percent of 2s: '+str(ab*Z)+'%')
print('Percent of 3s: '+str(ac*Z)+'%')
print('Percent of 4s: '+str(ad*Z)+'%')
print('Percent of 5s: '+str(ae*Z)+'%')
print('Percent of 6s: '+str(af*Z)+'%')