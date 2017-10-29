import turtle as t
import random

# 500x500 frame
t.shape("turtle")
t.up()
t.speed(0)
t.goto(-250,-250)
t.setheading(0)
t.down()
t.color("black")
t.pensize(5)

for x in range(4):
    t.fd(500)
    t.lt(90)


#obstacle a
t.color("red")
billax=random.randint(-110,150)
billay=random.randint(-150,200)
billaz=random.randint(50,100)

t.up()
t.goto(billax,billay)
t.down()
t.pensize(5)

for x in range(4):
    t.fd(billaz)
    t.rt(90)


#obstacle b
t.color("blue")

billbx=random.randint(-250,0)
billby=random.randint(0,250)
billbz=random.randint(50,100)

t.up()
t.goto(billbx,billby)
t.down()
t.pensize(1)

for x in range(4):
    t.fd(billbz)
    t.rt(90)

#obstacle c
t.color("green")
billcx=random.randint(-150,150)
billcy=random.randint(100,230)
billcz=random.randint(50,100)

t.up()
t.goto(billcx,billcy)
t.down()
t.pensize(2)

for x in range(4):
    t.fd(billcz)
    t.rt(90)

    
#center
t.up()
t.goto(0,0)
t.down

t.color("black")


#random
a=random.randint(1,360)
t.setheading(a)
t.speed(10)



#1000 repeating
for x in range(1000):
    while True:
        t.fd(5)
        a=t.xcor()
        b=t.ycor()
        t.goto(a,b)
        
        if a>=250:
            break
        
        if b>=250:
            break
        
        if a<=-250:
            break
        
        if b<=-250:
            break
        
        #obstacle a
        if billax<a<billax+billaz and billay-billaz<b<billay: 
            break
        
        #ostacle b
        if billbx<a<billbx+billbz and billby-billbz<b<billby:
            break
        
        #obstacle c
        if billcx<a<billcx+billcz and billcy-billcz<b<billcy: 
            break
        
            
    #reflecting
    while True:
        ang=t.heading()
        ang1=180+ang
        a=t.xcor()
        b=t.ycor()
        t.goto(a,b)
        
        if a>=250:
            t.setheading(-ang+180)
            break
        
        if a<=-250:
            t.setheading(-ang+180)
            break
        
        if b>=250:
            t.setheading(-ang)
            break
        
        if b<=-250:
            t.setheading(-ang)
            break
        
        #obstacle a
        if billax<a<billax+billaz and b<billay:
            t.setheading(-ang)
            break
        if billax<a<billax+billaz and b>billay-billaz:
            t.setheading(-ang)
            break
        if billay-billaz<b<billay and billax<a:
            t.setheading(ang1)
            break
        if billay-billaz<b<billay and billax+billaz>a:
            t.setheading(ang1)
            break
        
        #obstacle b
        if billbx<a<billbx+billbz and b<billby:
            t.setheading(-ang)
            break
        if billbx<a<billbx+billbz and b>billby-billbz: 
            t.setheading(-ang)
            break
        if billby-billbz<b<billby and billbx<a: 
            t.setheading(ang1)
            break
        if billby-billbz<b<billby and billbx+billbz>a: 
            t.setheading(ang1)
            break
        
        #obstacle c
        if billcx<a<billcx+billcz and b<billcy: 
            t.setheading(-ang)
            break
        if billcx<a<billcx+billcz and b>billcy-billcz:
            t.setheading(-ang)
            break
        if billcy-billcz<b<billcy and billcx<a:
            t.setheading(ang1)
            break
        if billcy-billcz<b<billcy and billcx+billcz>a:
            t.setheading(ang1)
            break
       
