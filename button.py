from tkinter import*
root=Tk()
root.title("countinu")
w=Button(root, text='stop', activebackground='red',
activeforeground='blue',bg='yellow',  width=10, command=root.destroy)
w.pack()
root.mainloop()