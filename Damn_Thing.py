#1-st number 
t = turtle.Turtle('turtle')

t.width(1.5)
t.color('forestgreen')

t.left(90)

for _ in range(5):
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(25)
    t.left(90)

turtle.done()

#2-nd number
t = turtle.Turtle('turtle')

t.width(1.5)
t.color('forestgreen')

f  = 35

for _ in range(10):
    t.forward(f)
    f = f - 5
    t.right(90)
    

turtle.done()
