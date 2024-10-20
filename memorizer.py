from tkinter import *
from tkinter.filedialog import *
#main window
screen = Tk()
screen.title("memorizer")
#opening file function
def Openf():
    dialog=askopenfile(title="Open File")
    if dialog is not None:
        #clearing existing items
        listB.delete(0,END)
        items=dialog.readlines()
        for i in items:
            listB.insert(END,i.strip())
def addition():
    listB.insert(END,item.get())
    item.delete(0,END)
def deletion():
    element=listB.curselection()
    if element:
        listB.delete(element)







#buttons
open=Button(screen,text="Open",command=Openf,width=10)
save=Button(screen,text="Save",command=None,width=10)
delete=Button(screen,text="Delete",command=deletion,width=10)
open.pack(side=LEFT,padx=5,pady=5)
delete.pack(side=RIGHT,padx=5,pady=5)
save.pack(side=TOP,padx=5,pady=5)
#input for add
add=Button(screen,text="Add",command=addition,width=10)
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
    listB.insert(END,"LIST "+str(i))
listB.pack(side=LEFT,padx=5)
scroll.config(command=listB.yview)
frame.pack(side=RIGHT)






screen.mainloop()



