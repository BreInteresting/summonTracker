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
import random
from summonSheet import summon

def main():
    global mainWindow
    
    mainWindow = tk.Tk()
    mainWindow.title("Summon Creator")
    mainWindow.geometry("250x120")
    mainWindow.configure(background="gray")

    summonButton = tk.Button(mainWindow, text="New Summon", bg="Red", fg="white", font=('arial', 20), command=summon)
    summonButton.grid(row=4, column=2, padx=30, pady=30)

    #loadButton = tk.Button(mainWindow, text="Load", command=loadButtonClick)
    #loadButton.grid(row=5, column=2, padx=20, pady=30)

    mainWindow.mainloop()

if __name__ == "__main__":
    main()

