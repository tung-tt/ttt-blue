from tkinter import *
# Tkinter practice

# Window Initialize, size set
root = Tk() # Creates a root widget
root.title('Tungo GUI')
root.configure(background = 'white')
root.minsize(150,150)
root.maxsize(500,500)
# Label widget
text = Label(root, text='Hello World')
text.pack()
text2 = Label(root, text = '🍪 Cookie Dispenser')
text2.pack()
# Starts GUI window
root.mainloop()