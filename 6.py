import turtle

m = 10

for i in range(7):
    turtle.forward(10 * m)
    turtle.right(120)

turtle.up()
for i in range(0, 10):
    for j in range(-10, 0):
        turtle.setpos(i * m, j * m)
        turtle.dot(5)

input()