import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title('Wikipedia')
win.geometry('250x70')

# Creating Function
def serach_wiki() :
    search = entry.get()
    answer = wikipedia.summary(search)
    showinfo("Wikipedia Answer",answer)

# Creating Label
label = Label(win,text="Wikipedia Search :")
label.grid(row=0,column=0)

# Creting Entry Box
entry = Entry(win)
entry.grid(row=1,column=0)

# Creating Button
button = Button(win,text="Search",command=serach_wiki)
button.grid(row=1,column=1,padx=10)

win.mainloop()
