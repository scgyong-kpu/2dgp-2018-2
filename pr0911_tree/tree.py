import turtle

MAX_LEVEL = 7

def tree(level):
	length = level * 10
	turtle.forward(length)
	if (level > 1):
		turtle.left(20)
		tree(level - 1)
		turtle.right(40)
		tree(level - 1)
		turtle.left(20)
	turtle.backward(length)

tree(MAX_LEVEL)

