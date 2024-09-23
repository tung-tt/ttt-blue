from tkinter import *
# Tkinter practice
root = Tk() # Creates a root widget

#
turn_on = Button(root, text="ON")
turn_on.pack()

turn_off = Button(root, text="OFF")
turn_off.pack()

volume = Label(root, text="VOLUME")
volume.pack()

volume_up = Button(root, text="+")
volume_up.pack()

volume_down = Button(root, text="-")
volume_down.pack()

# Starts GUI window
root.mainloop()