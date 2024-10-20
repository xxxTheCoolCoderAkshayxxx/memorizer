from tkinter import *
from tkinter.filedialog import *
#main window
screen = Tk()
screen.title("memorizer")
#buttons
open=Button(screen,text="Open",command=None,width=10)
save=Button(screen,text="Save",command=None,width=10)
delete=Button(screen,text="Delete",command=None,width=10)
open.pack(side=LEFT,padx=5,pady=5)
delete.pack(side=RIGHT,padx=5,pady=5)
save.pack(side=TOP,padx=5,pady=5)
#input for add
add=Button(screen,text="Add",command=None,width=10)
item=Entry(screen,width=40)
item.pack(padx=5,pady=5)
add.pack(padx=5,pady=5)
#frame for lsit box
frame=Frame(screen)
scroll=Scrollbar(frame,orient="vertical")
scroll.pack(side=RIGHT,fill=Y)
#list box with background color
listB=Listbox(frame,width=70,yscrollcommand=scroll.set,bg="light grey")
for i in range(1,100):
    listB.insert(END,"LIST",str(i))
listB.pack(side=LEFT,padx=5)
scroll.config(command=listB.yview)
frame.pack(side=RIGHT)





screen.mainloop()