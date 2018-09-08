import turtle

MAX_LEVEL = 7

COLORS = [ (80, 223, 80), (80, 193, 80), (80, 52, 26), (65, 42, 21), (50, 32, 16), (35, 22, 11), (20, 12, 6) ]

def setColor(level):
	turtle.pencolor(COLORS[level - 1])

# 21, 12, 6
# 83, 49, 24

def tree(level):
	length = level * 20
	turtle.width(level * 2)
	setColor(level)
	turtle.forward(length)
	if (level > 1):
		turtle.left(20)
		tree(level - 1)
		turtle.right(40)
		tree(level - 1)
		turtle.left(20)
	turtle.backward(length)

turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.backward(300)
turtle.pendown()
turtle.colormode(255)

tree(MAX_LEVEL)

turtle.exitonclick()
