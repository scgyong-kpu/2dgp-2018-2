import turtle
import random

MAX_LEVEL = 7

COLORS = [ (80, 223, 80), (80, 193, 80), (80, 52, 36), (65, 42, 31), (50, 32, 26), (35, 22, 21), (20, 12, 16) ]

def adjustColorValue(v):
	v = int(v * random.uniform(0.8, 1.2))
	if v > 255: v = 255
	return v

def setColor(level):
	(r, g, b) = COLORS[level - 1]
	turtle.pencolor((adjustColorValue(r), adjustColorValue(g), adjustColorValue(b)))

# 21, 12, 6
# 83, 49, 24

def tree(level):
	length = level * random.uniform(17, 23)
	turtle.width(level * 2 - 1)
	setColor(level)
	turtle.pendown()
	turtle.forward(length)
	if (level > 1):
		left = random.uniform(15, 25)
		right = random.uniform(15, 25)
		turtle.left(left)
		tree(level - 1)
		turtle.right(left + right)
		tree(level - 1)
		turtle.left(right)
	turtle.penup()
	# setColor(level)
	turtle.backward(length)

turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.backward(300)
turtle.pendown()
turtle.colormode(255)

tree(MAX_LEVEL)

turtle.exitonclick()
