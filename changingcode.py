from tkinter import *
root=Tk()
root.title("my frist program")
root.geometry('350x200')
leb1=Label(root, text="HI i am surajit")
leb1.grid()
# function to display text when
# button is clicked
def clicked():
    leb1.configure(text = "I just got clicked")
# button widget with red color text
# inside
btn=Button(root, text='cleck me',  fg='red', command=clicked)
btn.grid(column=1, row=0)
root.mainloop()