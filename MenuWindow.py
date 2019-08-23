# Imports the functions of buttons and other things from the library Tkinter(in commandsmenu.py)
from commandsmenu import help_window, quit_window, tk, ImageTk, Image
# Imports the game
import pygamewindow as game

# Defines a font used casually
font = ("TW Cen MT", 30)

# Runs the window

menuwindow = tk.Tk()

# Configure the MenuWindow properties(icon, title and geometry)
menuwindow.geometry("250x350+520+180")
menuwindow.iconbitmap("assets/snakeicon.ico")
menuwindow.configure(bg="white")
menuwindow.title("Snake Game")
# Button that must be pressed to play
buttonplay = tk.Button(menuwindow, text="PLAY", width=46, font=font, fg="green", bg="white",
                       command=lambda: game.run())
# Button that must be pressed to quit
buttonquit = tk.Button(menuwindow, text="QUIT", width=46, font=font, fg="red", bg="white",
                       command=lambda: quit_window(menuwindow))
# Button that must be pressed to see the help instructions
buttonhelp = tk.Button(menuwindow, text="HELP", width=46, font=font, fg="blue", bg="white",
                       command=lambda: help_window())
# Loads the header image
imageheader = Image.open("assets/header.png")
headersnake = ImageTk.PhotoImage(imageheader)
labelsnake = tk.Label(menuwindow, image=headersnake)
# Puts the header
labelsnake.pack()
# Puts the button play
buttonplay.pack()
# Puts the button help
buttonhelp.pack()
# Puts the button quit
buttonquit.pack()
# Makes the window running
menuwindow.mainloop()
