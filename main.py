from tkinter import filedialog
from tkinter import *

#ui_frontend
root = Tk()
root.title("Txt Editor")
root.geometry("600x500")
text=Text(root)
mymenu=Menu();lst_1=Menu()


#backend
def new_file():
    Text.delete(0.0,END)
    lst_1.add_command(label='New File',command=new_file)

def open_file():
    file_1=filedialog.askopenfile(mode='r')
    data=file_1.read();Text.delete(0.0,END)
    Text.insert(0.0,data)
    lst_1.add_command(label='Open File',command=open_file)

def save_file():
    #filename='Untitled.txt'
    data=Text.get(0.0,END)
#writing data
    file_1.write()
    file_1.write(data)

lst_1.add_command(label='Save File',command=save_file)

def save_file_as():
    filedialog.asksaveasfilename(mode='w')
#input and write data
    data=Text.get(0.0,END)
    file_1.write(data)

lst_1.add_command(label='Save File as',command=save_file_as)

lst_1.add_command(label='Exit',command=root.quit)
mymenu.add_cascade(label='File',menu=lst_1)
root.config(menu=mymenu)
root.mainloop()