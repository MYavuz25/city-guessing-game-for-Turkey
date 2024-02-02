import turtle
import pandas
from tkinter import messagebox
import time
screen = turtle.Screen()
screen.title("Guess the Names of cities of Turkey")
screen.setup(width=1250, height=712)
image = 'unnamed.gif'
screen.addshape(image)
turtle.shape(image)
pencil = turtle.Turtle()
pencil.hideturtle()
pencil.penup()
# -----founding Coordinates of cities Name-----
# ı used this code for finding coordinates and ı printed coordinates
# def print_xy(x,y):
#     print(f"{x}, {y}")
#turtle.onscreenclick(print_xy)
# After this ı copied all the coordinates to cities.csv file
data = pandas.read_csv('cities.csv')
states = data['State'].to_list()
missing_cities=data['State'].to_list()
correct_guesses = []
score=0
while len(correct_guesses) < 81:

	answer = screen.textinput(
	title=f'Guess the State {len(correct_guesses)}/81',
	prompt='Enter City Name or "Exit" to Quit')
	answer=answer.upper()

	if answer == "EXIT":
		break
	elif answer in correct_guesses:
		messagebox.showinfo("Warning!!!", f"This city {answer} already entered")
		score+=-10
	elif answer in states and answer not in correct_guesses :
		state = data[data.State == answer]
		x_ = int(state.x)
		y_ = int(state.y)
		correct_guesses.append(answer)
		pencil.goto(x=x_, y=y_)
		pencil.write(f"{answer}", font=('Arial', 8, 'normal'))
		score+=30
		missing_cities.remove(answer)
	else:
		messagebox.showwarning("Warning!!!",f"There is no city name {answer} in Turkey")
		score+=-20
ShowMissingCities=messagebox.askquestion("Question","Do you Want show cities not found")
if ShowMissingCities=="yes":
	for a in missing_cities:
		missing_cities = data[data.State == a]
		x_ = int(missing_cities.x)
		y_ = int(missing_cities.y)
		pencil.color("purple")
		pencil.goto(x=x_, y=y_)
		pencil.write(f"{a}", font=('Arial', 8, 'bold',))
time.sleep(15)
screen.clear()
pencil.color("black")
pencil.goto(0, 0)
end_text = ""
Total_Cities = len(correct_guesses)
if Total_Cities == 81:
	end_text = 'You Guessed Them All Correctly'
elif Total_Cities >= 60:
	end_text = f"Good Work: {Total_Cities}/81"
elif Total_Cities >= 40:
	end_text = f"Average Performance: {Total_Cities}/81"
else:
	end_text = f"Poor Performance: {Total_Cities}/81"
pencil.write(f"{end_text}\nYour Score:{score}", align='center', font=("Arial", 22, 'normal'))
turtle.mainloop()
