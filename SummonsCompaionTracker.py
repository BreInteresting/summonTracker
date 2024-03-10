'''
The purpose of this application is that during D&D, the players and the DM can track the 
status of a summon or companion. Allowing users to record the ability scores, hit points, 
duration of summon, abilities, attacks, and roll dice when needed from Saves, Check, and 
damage when attacking.
Program: SummonsCompaionTracker.py
Author: Bri Manning
Date: 2/5/2024
Version 1.0
'''
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import tkinter as tk
from PIL import ImageTk, Image
from summonSheet import summon

#main function to run the program
def main():
    # makes the main menu window
    global mainWindow
    mainWindow = tk.Tk()
    mainWindow.title("Summon Creator")
    mainWindow.geometry("675x703")
    # Load and display the background image on the main window
    imagePath = "mainWindowBackground.jpg"
    img = Image.open(imagePath)
    backgroundImg = ImageTk.PhotoImage(img)
    backgroundLabel = tk.Label(mainWindow, image=backgroundImg)
    backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
    # a frame around the text. just for looks
    frame = tk.Frame(mainWindow, bd=2, relief="solid", bg="black")
    frame.place(x=160, y=100, width=400, height=200)
    # the test on the window and placement of it 
    mainWindowLabel = tk.Label(mainWindow, text="Do you need allies?\nNo one to help?\nSummon a Companion to help", fg="black", font=("Comic Sans MS", 20), bg="#D2B48C", highlightthickness=0)
    mainWindowLabel.place(x=360, y=200, anchor="center")
    # this is the button that opens the summon window. you can push it multiple times and get as many windows as you like
    summonButton = tk.Button(mainWindow, text="New Summon", bg="Red", fg="white", font=('Comic Sans MS', 20), command=summon)
    summonButton.place(x=260, y=400)

    mainWindow.mainloop()

if __name__ == "__main__":
    main()

