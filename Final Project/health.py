#!/usr/bin/env python3

import tkinter as tk
from tkinter import *

# --- functions ---

def on_escape(event=None):
    print("escaped")
    root.destroy()

# --- main ---

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# --- fullscreen ---

#root.overrideredirect(True)  # sometimes it is needed to toggle fullscreen
                              # but then window doesn't get events from system
#root.overrideredirect(False) # so you have to set it back

root.attributes("-fullscreen", True) # run fullscreen
root.wm_attributes("-topmost", True) # keep on top
#root.focus_set() # set focus on window

# --- closing methods ---

# close window with key `ESC`
root.bind("<Escape>", on_escape)

# close window after 5s if `ESC` will not work
root.after(5000, root.destroy) 

# --- canvas ---

canvas = tk.Canvas(root)
canvas.pack(fill='none', expand=True)

# canvas.create_oval((0, 0, screen_width, screen_height), fill='red', outline='')

# load the .gif image file
gif1 = PhotoImage(file='panda.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image=gif1, anchor=NW)



canvas.create_text(100,100 ,fill="darkblue",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")
canvas.create_text(200,200 ,fill="darkblue",
                        text="Click the bubbles that are multiples of two.")

# --- start ---

root.mainloop()

exec(open("display.py").read())