import turtle
import random

MAX_LEVEL = 7

def adjustColorValue(v):
	v = int(v * random.uniform(0.8, 1.2))
	if v > 255: v = 255
	return v

def setColor(level):
	if level <= 2:
		(r, g, b) = (80, 255 - level * 30, 80)
	else:
		bright = level - 2
		(r, g, b) = (180 - 20 * level, 120 - 10 * level, 80 - 8 * level)

	turtle.pencolor((adjustColorValue(r), adjustColorValue(g), adjustColorValue(b)))

def tree(level, leavesOnly = False):
	length = level * random.uniform(17, 23)
	turtle.width(level * 3 - 2)
	setColor(level)
	if not leavesOnly:
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
	if not leavesOnly:
		turtle.penup()
		turtle.backward(length)
	if level in range(3, 7):
		tree(2, True)

turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.backward(300)
turtle.pendown()
turtle.colormode(255)

tree(MAX_LEVEL)

turtle.exitonclick()
