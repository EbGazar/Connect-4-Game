import random
import turtle as t

t.title("Connect 4")
t.setup(width=1800,height=1600,startx = 50,starty=0)
t.hideturtle()
t.bgpic(r"pic\game7.gif")
t.color("white")

t.penup()
t.sety(280)
t.pensize(0)
t.hideturtle()

t.write("WELCOME", False, 'center', ['Courier', 120, 'bold'])
t.sety(200)
t.color("snow2")
t.write("CONNECT FOUR GAME", False, 'center', ['Courier', 50, 'bold'])

t.sety(0)
t.color("snow2")
t.write("START GAME", False, 'center', ['Courier', 50, 'bold'])

t.sety(-100)
t.color("orange")
t.write("PLAYER VS COMPUTER", False, 'center', ['Courier', 45, 'italic']) 

t.sety(-175)
t.color("orange")
t.write("PLAYER VS PLAYER", False, 'center', ['Courier', 50, 'italic'])

t.shape("arrow")

t.sety(-60)
t.setx(-350)
t.showturtle()

x = 1

while x:


    t.setx(-350)

    def up():
        t.sety(-60)

    def down():
        t.sety(-135)

    def end():
        global x
        x = 0

        if int(t.distance(0,0)) == 355:
            global diff

            diff = 'mode1'
        else:
            diff= 'mode2'


    t.listen()

    t.onkeypress(up, "Up")
    t.onkeypress(down, "Down")
    t.onkeypress(end, "Return")
  

t.clearscreen()

t.speed(0)
t.hideturtle()
t.penup()

t.bgpic(r"pic\game7.gif")

t.sety(280)
t.setx(0)
t.color('white')
t.write("🥇 PLEASE CHOOSE YOUR COLOR 🥇", False,'center', ['Courier', 70, 'bold'])


t.color("red")
t.sety(50)
t.pendown()
t.begin_fill()
t.circle(80)
t.end_fill()
t.penup()

t.sety(-45)
t.color("white")
t.write("OR", False, 'center', ['Courier', 40, 'italic'])

t.sety(-235)
t.color('yellow')
t.pendown()
t.begin_fill()
t.circle(80)
t.end_fill()

t.penup()

t.sety(120)
l = True

while l :
    
    t.color('navy')
    
    t.shape('arrow')
    t.turtlesize(8)
    t.setx(-250)
    t.showturtle()

    def up():
        t.sety(120)

    def down():
        t.sety(-155)

    def end():

        global l
        global player_choice
        global comp_choice
        
        if int(t.distance(0, 0)) == 277:

            player_choice = 'X'
            comp_choice = 'O'
        else:
            player_choice = 'O'
            comp_choice = 'X'
        
        l = 0

    t.listen()

    t.onkeypress(up, "Up")
    t.onkeypress(down, "Down")
    t.onkeypress(end, "Return")


t.clearscreen()

t.speed(0)
t.pensize(30)
t.speed(0)
t.setup(width=1800,height=1600,startx = 50,starty=0)
t.color("lightblue")
t.shape('arrow')
t.shapesize(8)
t.hideturtle()

def board_draw():
    t.begin_fill()
    t.penup()
    t.setx(-810)
    t.sety(400)
    t.pendown()
    t.fd(1620)
    t.rt(90)
    t.fd(1000)
    t.rt(90)
    t.fd(1620)
    t.rt(90)
    t.fd(1000)
    t.end_fill()
    
board_draw()

t.color('white')

def draw_cir():


    x = -700
    y =  350

    for i in range(7):
        

        t.penup()
        t.setx(x)
        x+= 250
        y = 350

        for j in range(6):
            
            t.sety(y)
            t.pendown()
            t.begin_fill()
            t.circle(50)
            t.end_fill()
            y -= 147
            t.penup()
        

draw_cir()

free_cells = {1 :6, 2 :6, 3 :6, 4:6, 5 :6, 6 :6, 7 :6}
all = 0

filled_red = {1 :0, 2 :0, 3 :0, 4:0, 5 :0, 6 :0, 7 :0}
filled_yellow = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

filled_raw = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
filled_raw2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}



def draw_mark(col, color):

    global m
    global r
    global all
    global free_cells
    global raw_pos
    global col_pos
    global filled_red_raw
    global filled_yellow_raw
    global last_col
    global filled_raw2

    r = 0
    m = 0
    last_col2 = 0

    if all == 41:
        t.clearscreen()
        t.bgcolor('black')
        t.penup()
        t.bgpic(r"pic\game13.gif")
        t.exitonclick()

    col_pos = -709 + ((col - 1) * 250)



    if col_pos > 791:
        col_pos = 791
        return

    raw_pos = -385 +  ((free_cells[col] - 6) * (-147))

    if raw_pos >= 497:
        raw_pos = 497
        return


    t.penup()
    t.setx(col_pos)
    t.sety(raw_pos)

    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.penup()

    free_cells[col] -= 1
    all += 1

    
    for i in range(1 ,8):

        if col == i and color == "red":

            last_col = i

            if col > last_col2:

                filled_raw2[last_col2] = 0

            filled_raw[i] = 1

            filled_red[i] += 1
            filled_yellow[i] = 0

            if filled_red[i] == 4:
                t.clearscreen()
                t.bgcolor('black')
                t.hideturtle()
                t.penup()
                t.bgpic(r"pic\game15.gif")
                t.color("white")
                t.setx(0)
                t.sety(-230)
                t.write("🥇 RED WIN 🥇", False,'center', ['Courier', 70, 'bold'])
                t.sety(-300)
                t.write("💔 Click Anywhere To Exit 💔", False,'center', ['Courier', 30, 'normal'])
                t.exitonclick()
                exit()

        elif col == i and color == "yellow":
            
            last_col2 = i

            if col  > last_col:
        
                    filled_raw[last_col] = 0

            filled_yellow[i] += 1
            filled_red[i] = 0

            if filled_yellow[i] == 4:
                t.clearscreen()
                t.bgcolor('black')
                t.hideturtle()
                t.penup()
                t.bgpic(r"pic\game15.gif")
                t.color("white")
                t.setx(0)
                t.sety(-230)
                t.write("🥇 YELLOW WIN 🥇", False,'center', ['Courier', 70, 'bold'])
                t.sety(-300)
                t.write("💔 Click Anywhere To Exit 💔", False,'center', ['Courier', 30, 'normal'])
                t.exitonclick()
                exit()


    for i in [1,2,3,4]:

        if filled_raw[i] == filled_raw[i+1] == filled_raw[i+2] == filled_raw[i+3] == 1:
            t.clearscreen()
            t.bgcolor('black')
            t.hideturtle()
            t.penup()
            t.bgpic(r"pic\game15.gif")
            t.color("white")
            t.setx(0)
            t.sety(-230)
            t.write("🥇 RED WIN 🥇", False,'center', ['Courier', 70, 'bold'])
            t.sety(-300)
            t.write(" 💔 Click Anywhere To Exit 💔", False,'center', ['Courier', 30, 'normal'])
            t.exitonclick()
            exit()
            

    for i in [1, 2, 3, 4]:

        if filled_raw2[i] == filled_raw2[i+1] == filled_raw2[i+2] == filled_raw2[i+3] == 1:
            t.clearscreen()
            t.bgcolor('black')
            t.hideturtle()
            t.penup()
            t.bgpic(r"pic\game15.gif")
            t.color("white")
            t.setx(0)
            t.sety(-230)
            t.write("🥇 YELLOW WIN 🥇", False,'center', ['Courier', 70, 'bold'])
            t.sety(-300)
            t.write("💔 Click Anywhere To Exit 💔", False,'center', ['Courier', 30, 'normal'])
            t.exitonclick()
            exit()


    t.setx(p)
    t.sety(475)
    t.color("navy")

    

t.speed(0)
t.shape('arrow')
t.turtlesize(5)
t.tilt(-180)
t.color('navy')
z = True
defa = -750
p = -750
t.setx(-750)
t.showturtle()
col = 1


def turn():
    
    global col
    global z
    global p
    global color

    global player

    while z:
    
        t.sety(475)

        def right():
            global p
            global col

            if p >= 750:
                p = 750
                t.setx(p)
            else:
                col += 1
                p += 250
                t.setx(p)
                

        def left():

            global col
            global p
            if p <= -750:
                p = -750
                t.setx(p)
            else:
                col -= 1
                p-= 250
                t.setx(p)

        def end():

            global color
            global z
            draw_mark(col, color)
            z = False

        t.listen()

        t.onkeypress(right, "Right")
        t.onkeypress(left, "Left")
        t.onkeypress(end, "Return")     

    t.sety(475)
    z = True

    

def player_turn():

    global color

    if player_choice == 'X':
        color = 'red'
    else:
        color = 'yellow'

    turn()

e = True

def comp_turn_easy():

    global p
    global color
    global comp_col
    global q

    q = True

    if player_choice == 'X':
        color = 'yellow'
    else:
        color = 'red'


    comp_col = random.randint(1, 7)

    for i in range(7): 

        ff = random.randint(1,7)

        if free_cells[ff] == 0:

            continue

        else:

            comp_col = ff
            break


    t.setx(p)

    t.hideturtle()
    draw_mark(comp_col,color)
    t.showturtle()

    t.sety(475)


def player2_turn():

    global color

    if player_choice == 'X':
        color = 'yellow'
    else:
        color = 'red'

    turn()


if diff == 'mode1':

    while e:

        player_turn()
        comp_turn_easy()

else:
     while e :
        player_turn()
        player2_turn()

t.exitonclick()
