from tkinter import *
root = Tk()
root.geometry("400x200")

def printSomething():
    label.config(text=entry.get())



ok=Label(root, text="Username")
ok.grid(row=2,column=1)
entryvalue = StringVar()

ok1=Label(root, text="Password")
ok1.grid(row=3,column=1)
entryvalue2 = StringVar()




button = Button(root, text="Login", command=printSomething)
button.grid(row=8, column=2)


#Create a Label to print the Name
label= Label(root, text="", font= ('Helvetica 14 bold'), foreground= "red3")
label.grid(row=1, column=2)
label= Label(root, text="", font= ('Helvetica 14 bold'), foreground= "red3")
label.grid(row=1, column=4)

root.mainloop()