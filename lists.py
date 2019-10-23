# how to make a list
favmovies = ["Star Wars", "Lord of the rings", "Gods not dead"]
#print the whole list
print(favmovies)
# prrint individuals
print(favmovies[0])
# to add you can use append or insert
# append adds to the end
favmovies.append("Person of intrest")
print(favmovies)
# insert will put the item wherever you want
favmovies.insert(1, "Harry Potter")
print(favmovies)
#how to remove items
#remove by name or by index
#remove by name use remove
favmovies.remove("Person of intrest")
print(favmovies)
#favmovies.remove("Endgame")
# pop will remove the last item inless index is given
favmovies.pop()
print(favmovies)
favmovies.pop(1)# will remove whatever is in index one
print(favmovies)

# get the length of a list
# this is a function
# the function name is len
print("my list has " + str(len(favmovies)) + " items")
favmovie = input("what is your favorite movie? ")
favmovies.append(favmovie)
print(favmovies)
print(favmovies[len(favmovies) - 1])

# loop through a list
count = 1

for x in favmovies:
	print("my number is " + str(count)+ " movie is " + x) 
	count = count + 1

numlist = [0,2,4,6,8,10]
# loop through the list and add all the numbers together, then print the sum

sun = 0

for q in numlist:
	print(str(q ))
	sun = sun + q

print("the sum is " + str(sun))

if "Star Wars" in favmovies:
	favmovies.remove("Star Wars")
	print("yeeeeeeesss")
else:
	print("not in list")