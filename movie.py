import time
import os

framelist = [
		'''
		 +---+
		 O   |
		/|\  |
		/ \  |
		    ===''', '''
		 +---+
		\O/  |
		 |   |
		 \\\\  |
		    ===''', '''
		 +---+
		     |
		\O/  |
		 |   |
		/ \ ==='''
]

framelista = [
			'''
			 +---+
			 O   |
			/|\  |
			/ \  |
			    ===''', '''
			 +---+
			\O/  |
			 |   |
			 \\\\  |
			    ===''', '''
			 +---+
			     |
			\O/  |
			 |   |
			/ \ ==='''
]
framelistb = [
				'''
				 +---+
				 O   |
				/|\  |
				/ \  |
				    ===''', '''
				 +---+
				\O/  |
				 |   |
				 \\\\  |
				    ===''', '''
				 +---+
				     |
				\O/  |
				 |   |
				/ \ ==='''
]
while True:
	frame = 1
	if frame <= 2:
		os.system("cls")
		print(framelist)
		time.sleep(.3)
while True:
	for framea in framelista:
		os.system("cls")
		print(framelista)
		time.sleep(.3)
while True:
	for frameb in framelistb:
		os.system("cls")
		print(framelistb)
		time.sleep(.3)

