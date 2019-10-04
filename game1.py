from turtle import *
T = Turtle()
myScreen = T.getscreen()
T.penup()
T.goto(myScreen.window_width() /2-200, myScreen.window_height()/2-50)
T.hideturtle()
score = 0

def us():
	T.clear()
	T.write("score: " + str(score), False, "left", font=("Arial", 20, "normal"))
us()

myScreen.mainloop()
