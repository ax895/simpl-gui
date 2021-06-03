from tkinter import *
import webbrowser

colour = 'magenta2'
	
gui = Tk()
gui.geometry('500x300')
gui.resizable(0,0)
gui.title("ax895-Socials")
gui.configure(bg='black')


def on_enter1(e):
   button1.config(background='grey20', foreground='deep pink')
def on_leave1(e):
   button1.config(background='black', foreground=colour)

def on_enter2(e):
   button2.config(background='grey20', foreground='deep pink')
def on_leave2(e):
   button2.config(background='black', foreground=colour)

def on_enter3(e):
   button3.config(background='grey20', foreground='deep pink')
def on_leave3(e):
   button3.config(background='black', foreground=colour)

def on_enter4(e):
   button4.config(background='grey20', foreground='deep pink')
def on_leave4(e):
   button4.config(background='black', foreground=colour)


def github():
	webbrowser.open('https://github.com/ax895', new=2)
def reddit():
	webbrowser.open('https://www.reddit.com/user/Ax895', new=2)
def youtube():
	webbrowser.open('https://www.youtube.com/channel/UCHPRxYfkMBQWasDswZMNXCQ', new=2)
def exit():
	gui.destroy()


button1 = Button(gui,text = 'GitHub', font = 'calisto 15 ', bg = 'black', fg = colour, bd = 0, activebackground = 'grey', cursor="hand2", command = github)
button1.place(x=195 ,y = 60)
button2 = Button(gui,text = 'Reddit', font = 'calisto 15 ', bg = 'black', fg = colour, bd = 0, activebackground = 'grey', cursor="hand2",command = reddit)
button2.place(x=196 ,y = 140)
button3 = Button(gui,text = 'Youtube', font = 'calisto 15 ', bg = 'black', fg = colour, bd = 0, activebackground = 'grey', cursor="hand2",command = youtube)
button3.place(x=189 ,y = 220)
button4 = Button(gui,text = 'exit', font = 'calisto 10 ', bg = 'black', fg = colour, bd = 0, activebackground = 'grey', cursor="hand2",command = exit)
button4.place(x=455 ,y = 260)

button1.bind('<Enter>', on_enter1)
button1.bind('<Leave>', on_leave1)

button2.bind('<Enter>', on_enter2)
button2.bind('<Leave>', on_leave2)

button3.bind('<Enter>', on_enter3)
button3.bind('<Leave>', on_leave3)

button4.bind('<Enter>', on_enter4)
button4.bind('<Leave>', on_leave4)



gui.mainloop()