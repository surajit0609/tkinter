from tkinter import *
root=Tk()
root.title("entry code")
root.geometry("340x200")
lab=Label(root, text='are you geek')
lab.grid()
# adding Entry Field
txt=Entry(root,width='10')
txt.grid(column=1, row=0)
# function to display user text when
# button is clicked
def clicked():
    res="you wrote " + txt.get()
    lab.configure(text = res)
# button widget with red color text inside
btn=Button(root, text='click me', fg='red', command=clicked)
btn.grid(column=3, row=0)

root.mainloop()