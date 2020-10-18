from tkinter import * #Imports all of the tkinter packages. 
from tkinter import filedialog
def new_file():
    text.delete(0.0,END)  #Deletes all the contents of the text editor.
def open_file():
    file1=filedialog.askopenfile(mode='r') #To open open_file   filedialog.
    data=file1.read()
    text.delete(0.0,END)
    text.insert(0.0,data) #Inserts data variable in text editor.
def save_file():
    filename="Untilted.txt"
    data=text.get(0.0,END)
    file1=open(filename,"w")
    file1.write(data)
def save_as():
    file1=filedialog.asksaveasfile(mode='w') #To open save_as filedialog.
    data=text.get(0.0,END)
    file1.write(data)

gui=Tk() #For tkinter object.
gui.title("Guapo editor") 
gui.geometry("600x500") #600 is length and 500 is breadth of the text editor.
text=Text(gui)
text.pack() #To display the text in the centre.
Guapmenu=Menu()
list1=Menu()
list1.add_command(label='New file',command=new_file) #To create menus.
list1.add_command(label='Open file',command=open_file)
list1.add_command(label='Save',command=save_file)
list1.add_command(label='Save as',command=save_as)
list1.add_command(label='Exit Guapo Editor',command=gui.quit)
Guapmenu.add_cascade(label='File',menu=list1) #To create a file option.
gui.config(menu=Guapmenu)
gui.mainloop() #To display the window in the screen.This line is compulsory.