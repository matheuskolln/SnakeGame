# Imports the library Tkinter
import tkinter as tk
# Imports components to load images in Tkinter
from PIL import Image, ImageTk


# Function that will close the called windows
def quit_window(window):
    window.destroy()


# Function that will open a window with the help instructions
def help_window():
    # Runs the window
    windowhelp = tk.Toplevel()
    # Configure the HelpWindow properties(icon, title and geometry)
    windowhelp.geometry("550x600")
    windowhelp.title("Help")
    windowhelp.iconbitmap("assets/snakeicon.ico")
    # Loads the help image and puts it.
    help = Image.open("assets/help.png")
    helpimage = ImageTk.PhotoImage(help)
    helplabel = tk.Label(windowhelp, image=helpimage)
    helplabel.pack()
    # Makes the window running
    windowhelp.mainloop()
