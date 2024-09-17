import random
from tkinter import *
from tkinter import messagebox
# Imports Tkinter as tk
# Import random for procedural choices

greeting = "  Hello from Tung, what'd you like to do today?  "

def main_screen():
    
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("100x100")
    
    mainloop()

# # Todo function, will take a list and then re-order it.
# def todo(list):
#     # Makes a new list as well as a copy
#     new_list = []
#     todo_copy = list[:]
#     # For every iteration in the list it will take one random from Copy over to New List
#     for i in range(len(list)):
#         selection = random.choice(todo_copy)
#         new_list.append("-" + selection)
#         todo_copy.remove(selection)
#         pass
#     return new_list
# # New list for to-do
# user_todo = []
# # Loop to get user input
# while True:
#     user_add = input("What's on your to-do? X to end: ")
#     if (user_add).lower() == "x":
#         print(todo(user_todo))
#         break
#     user_todo.append(user_add)
# print("Bye!")

# GUI
main_screen()