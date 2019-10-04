from turtle import *
t = Turtle()
screen = t.getscreen()
t.fd(200)
def writename():
	name = screen.textinput("name box", "what is your name?")
	t.write(name, move=True, align="left", font=("Arial", 30, "normal"))
	screen.listen()
screen.onkey(writename, "w")






screen.listen()
screen.mainloop()