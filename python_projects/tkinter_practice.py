from tkinter import *
# Tkinter practice

# Window Initialize, size set
root = Tk() # Creates a root widget
root.title('Tungo GUI')
root.configure(background = 'grey')
root.minsize(150,150)
root.maxsize(500,500)
# Label widget
text = Label(root, text='Hello World')
text.pack()
# Starts GUI window
root.mainloop()