import turtle

print 'Enter the option you want to execute'
print '1 -> diaplay the empty board'
print '2 -> run the program using minmax algorithm'
print '3 -> run the program using alphabeta algorithm'
print '4 -> display all the statistical information'

inp = int(raw_input().strip())

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
def draw_floor(size):
	for y in range(size[1]):
		for x in range(size[0]):
			a = (x,y)
			screen_x = -250 + (x*50)
			screen_y = 250- (y*50)
			pen = tile_pen
			pen.turtlesize(2.2,2.2)
			pen.goto(screen_x,screen_y)
			pen.stamp()
size = (4,4)
tile_pen = Pen()
def show_grid(size):
	wn = turtle.Screen()
	wn.bgcolor("black")
	wn.title("Align3")
	wn.setup(700,700)

	draw_floor(size)

results = '''
R1 = 7312903\n
R2 = 452 bits\n
R3 = 16\n
R4 = 1364.75 seconds\n
R5 = 0.00535\n
R6 = 3175939\n
R7 = 0.565\n
R8 = 760.27 seconds\n
R9(minmax) = 3305432000 bits\n
R9(alpha beta) = 1435278000 bits\n
R10(minmax) = 1364.75 seconds\n
R10(alpha beta) = 1095.3 seconds\n
R11(minmax and alpha beta) = 10/10\n
R12(minmax and alpha beta) = 20/20\n
'''


if inp == 2:
	import align3

elif inp == 3:
	import align3_alphabeta

elif inp == 1:
	show_grid(size)

elif inp == 4:
	print results