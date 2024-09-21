from tkinter import *
from time import sleep
# Tkinter practice

# Window Initialize, size set
root = Tk() # Creates a root widget
root.title('Tungo GUI')
root.minsize(150,150)
root.maxsize(500,500)
# Label widget
cookie_amount = 0
while True:
    sleep(1)
    cookie_amount += 1
    text = Label(root, text=cookie_amount)
    text.pack()
    # Starts GUI window
    root.mainloop()