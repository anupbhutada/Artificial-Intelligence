import turtle

turtle.ht()

width = 800
height = 800
turtle.screensize(width, height)

##Definitions
def text(text, size, color, pos1, pos2):
     turtle.penup()
     turtle.goto(pos1, pos2)
     turtle.color(color)
     turtle.begin_fill()
     turtle.write(text, font=('Arial', size, 'normal'))
     turtle.end_fill()


def onTextClick(event):
    x, y = event.x, event.y
    print('x={}, y={}'.format(x, y))    
    if (x >= 600 and x <= 800) and (  y >= 280 and y <= 300):
        turtle.onscreenclick(lambda x, y: turtle.bgcolor('red'))

##Screen
turtle.bgcolor('purple')
text('This is an example', 20, 'orange', 100, 100)

canvas = turtle.getcanvas()
canvas.bind('<Button-1>', onTextClick)    

turtle.done()