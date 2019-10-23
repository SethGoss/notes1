print("Welcome to the to do list")
todo = []

while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	count = 1
	choice = input("Make your choice: ")
	if choice == "q":
		break
	elif choice == "a":
		doa = input("please add something to the list: ")
		todo.append(doa)
	elif choice == "r":
		dor = input("please remove something from the list: ")
		if dor in todo:
			todo.remove(dor)
		else:
			print("not posible to remove something thats not there")
	elif choice == "p":
		for x in todo:
			print("task: " + str(count)+ " " + x) 
			count = count + 1
	else:
		print("that is not a choice")

todo = todo -1