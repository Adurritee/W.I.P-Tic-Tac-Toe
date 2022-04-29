#Imports
from tkinter import *
from PIL import Image,ImageTk

#Functions
def raise_frame(frame):
    frame.tkraise()
    display_win_loss.configure(text= " ")

def check_win():
    length = grid_size.get()

    #Horizontals
    for i in range(0,length*length,length):
        win = True
        StartofHorizontal = GameButtonList[i]
        for button in GameButtonList[i+1:i+length]:
            if button.cget('text') != StartofHorizontal.cget('text'):
                win = False
        if win and StartofHorizontal.cget('text') != '':
            return StartofHorizontal.cget('text')
    return False
    

    #Vertical


def game_button_press(button):
    global player_turn
    if button.cget('text') == '':
        button.config(text=player_turn,fg='black')
        player_turn = {'X':'O','O':'X'}[player_turn]
        winner = check_win()
        if winner:
            display_win_loss.config(text='Player ' +winner+ ' Wins!') 
            
def start_game():
    global GameButtonList
    GameButtonList = []
    size = grid_size.get()
    for i in range(size**2):
        current = Button(start_frame,text="",bg="white",activebackground="white",fg="white",font="Times 15 bold",borderwidth=10)
        current.config(command=lambda c=current:game_button_press(c))
        current.place(x=150+(i%size)*300/size,y=100+(i//size)*300/size,width=300/size,height=300/size)
        GameButtonList.append(current)
    raise_frame(start_frame)

#Root Widget
root = Tk()
root.title("AP Computer Science Principle Performance Task")
root.geometry('600x500')

#Variables
player_turn = 'X'
GameButtonList = []
grid_size = IntVar()

#Home Page
home_frame = Frame(root)
Welcome_label = Label(home_frame,text="Welcome to Tic Tac Toe!",bg="Green",font="Courier")
Start_button = Button(home_frame,text="Start",bg='Red',fg="black",font="Courier",command = start_game)
FAQ_button = Button(home_frame,text="FAQ",fg="black",bg="Yellow",font="Courier", command = lambda: raise_frame(faq_frame))
Options_button = Button(home_frame,text="Options",bg='blue',fg="black",font="Courier", command = lambda: raise_frame(options_frame))
Gamemode_button = Button(home_frame,text="Game Modes",bg='orange',fg="black",font="Courier", command = lambda: raise_frame(gamemode_frame))

#>
home_frame.place(x=0,y=0,width=600,height=500)
Welcome_label.place(x=150,y=50,width=300,height=50)
Start_button.place(x=250,y=150,width=110,height=50)
FAQ_button.place(x=250,y=300,width=110,height=50)
Options_button.place(x=250,y=250,width=110,height=50)
Gamemode_button.place(x=250,y=200,width=110,height=50)

#Home Page Images
x_resize1 = 95,95
x = ImageTk.PhotoImage(Image.open("x.png").resize(x_resize1))
home_x= Label(home_frame,image=x)
home_x.place(x=430,y=190)
o_resize1 = 150,150
o = ImageTk.PhotoImage(Image.open("ok1.png").resize(o_resize1)) 
home_plus= Label(home_frame,image=o)
home_plus.place(x=60,y=190)

#Start Page
start_frame=Frame(root)
goback_start=Button(start_frame,text="Home",font="Courier",command = lambda: raise_frame(home_frame))

#>
start_frame.place(x=0,y=0,width=600,height=500)
goback_start.place(x=250,y=20,width=100,height=50)

display_win_loss = Label(start_frame,text='',font="Courier 25 bold ")
display_win_loss.place(x=162,y=420)




#Gamemodes Page
gamemode_frame=Frame(root)
gamemode_label_1=Label(gamemode_frame,text="[5x5 Grid] ",font=" Courier 13 bold")
gamemode_label_2=Label(gamemode_frame,text="[4x4 Grid] ",font=" Courier 13 bold")
gamemode_label_3=Label(gamemode_frame,text="[3x3 Grid] ",font=" Courier 13 bold")
gamemode_label_4=Label(gamemode_frame,text="Select any of the game modes to play with a new grid! ",font=" Courier 13 underline",bg="green")
goback_gamemode=Button(gamemode_frame,text="Home",font="Courier",command = lambda: raise_frame(home_frame))
#>
gamemode_frame.place(x=0,y=0,width=600,height=500)
gamemode_label_1.place(x=370,y=150,width=300,height=50)
gamemode_label_2.place(x=160,y=150,width=300,height=50)
gamemode_label_3.place(x=-50,y=150,width=300,height=50)
gamemode_label_4.place(x=30,y=350,width=550,height=50)
goback_gamemode.place(x=250,y=20,width=100,height=50)

#Grids 
gamemode_resize = 90,90
gamemode_3x3 = ImageTk.PhotoImage(Image.open("3x3.png").resize(gamemode_resize))
gamemode= Label(gamemode_frame,image=gamemode_3x3)
gamemode.place(x=47,y=190)

gamemode_resize1 = 95,95
gamemode_4x4 = ImageTk.PhotoImage(Image.open("4x4.png").resize(gamemode_resize1))
gamemode_1= Label(gamemode_frame,image=gamemode_4x4)
gamemode_1.place(x=255,y=190)

gamemode_resize2 = 100,100
gamemode_5x5 = ImageTk.PhotoImage(Image.open("5x5.png").resize(gamemode_resize2))
gamemode_2= Label(gamemode_frame,image=gamemode_5x5)
gamemode_2.place(x=463,y=185)


    
Button1 = Radiobutton(gamemode_frame,variable=grid_size,value=3)
Button1.place(x=15,y=225)

Button2 = Radiobutton(gamemode_frame,variable=grid_size,value=4)
Button2.place(x=220,y=225)

Button3 = Radiobutton(gamemode_frame,variable=grid_size,value=5)
Button3.place(x=435,y=225)


#Options Page
options_frame=Frame(root)
options_label=Label(options_frame,text="Beta Beta Beta Beta Beta Beta\n Beta Beta Beta Beta Beta Beta\n Beta Beta Beta Beta Beta Beta\n Beta Beta Beta Beta Beta Beta",font="Courier")
goback_options=Button(options_frame,text="Home",font="Courier",command = lambda: raise_frame(home_frame))
#>
options_frame.place(x=0,y=0,width=600,height=500)
options_label.place(x=150,y=50,width=300,height=300)
goback_options.place(x=250,y=20,width=100,height=50)

#FAQ Page
faq_frame=Frame(root)
faq_label=Label(faq_frame,text="[FAQ: Frequently Asked Questions]\n This is a tic tac toe game in which you play tic tac\n toe to win games. There are many different game modes to enjoy,\n such as 5x5, 4x4, and 3x3 modes. ",font="Courier 10 ")
goback_faq=Button(faq_frame,text="Home",font="Courier",command = lambda: raise_frame(home_frame))
#>
faq_frame.place(x=0,y=0,width=600,height=500)
faq_label.place(x=50,y=90,width=500,height=200)
goback_faq.place(x=250,y=20,width=100,height=50)



raise_frame(home_frame)
root.mainloop()
