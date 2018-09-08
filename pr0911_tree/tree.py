import turtle

MAX_LEVEL = 7

def tree(level):
	length = level * 20
	turtle.width(level * 2)
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

tree(MAX_LEVEL)

turtle.exitonclick()
