from vpython import *
r=5. #Radius
h=10. #Höhe
scene.background=color.green
scene.center=vector(0,h,0)
box(pos=vector(0,0,0),size=vector(2*h,r/2,h), color=color.green)
ball = sphere(radius=r, color=color.black)
ball.pos=vector(0,1*h,0) #Fallhöhe
ball.v = vector(0,0,0) #Anfangsgeschwindigkeit
g=119.81
dt = 0.01
while True:
    rate(100)
    ball.pos = ball.pos + ball.v*dt
    if ball.pos.y < r:
        ball.v.y = -ball.v.y
    else:
        ball.v.y = ball.v.y - g*dt