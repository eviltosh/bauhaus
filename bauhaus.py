import turtle
window=turtle.Screen()
window.bgcolor('purple')
tess=turtle.Turtle()
tess.pensize(10)
tess.pensize(10)
tess.shape('turtle')
tess.color('yellow')
tess.speed(3)
draw=[(180,100),(135,141.4213562373095),(225,100),(120,100),(120,100),(30,100),(135,141.4213562373095),(225,100)]

def house(angle,distance):
    tess.right(angle)
    tess.forward(distance)

for angle,distance in draw:
    house(angle,distance)

window.mainloop()
