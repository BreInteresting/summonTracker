'''
The purpose of this application is that during D&D, the players and the DM can track the 
status of a summon or companion. Allowing users to record the ability scores, hit points, 
duration of summon, abilities, attacks, and roll dice when needed from Saves, Check, and 
damage when attacking.
Program: summonSheet.py
Author: Bri Manning
Date: 2/5/2024
Version 1.0
'''
import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox
from PIL import ImageTk, Image
# this is the function for the summons windows
def summon():
    global summonWindow
    #makes the summon window and name it
    summonWindow = tk.Toplevel()
    summonWindow.title("New Summon")
    summonWindow.geometry("1200x672")
    # this put the image on the background
    image_path = "paper.jpg"
    img = Image.open(image_path)
    photo = ImageTk.PhotoImage(img)
    image_label = tk.Label(summonWindow, image=photo)
    image_label.image = photo
    image_label.place(x=0, y=0)
    # makes the enrty box for the summons name
    summonNameLabel = tk.Label(summonWindow, text="Name:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    summonNameLabel.place(x=25, y=8)
    summonNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    summonNameEntry.place(x=80, y=10)
    # makes a drop down box for type of creature
    typeLabel = tk.Label(summonWindow, text="Type:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    typeLabel.place(x=215, y=8)
    typeValues = ["Aberration", "Beast", "Celestial", "Construct","Dragon", "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Undead"]
    typeCombobox = ttk.Combobox(summonWindow, values=typeValues, style='CustomStyle.TCombobox')
    typeCombobox.place(x=270, y=10)
    # Create a custom style for the comboboxs in the summons window
    style = ttk.Style()
    style.theme_create('CustomStyle', parent='alt',
                       settings={'TCombobox': {'configure': {'selectbackground': '#E0E0E0',
                                                             'fieldbackground': '#E0E0E0',
                                                             'foreground': 'black',
                                                             'selectforeground': 'black',
                                                             'arrowcolor': 'black'}}})
    style.theme_use('CustomStyle')
    # makes a drop down box for the duration of the summon of the creature
    durationLabel = tk.Label(summonWindow, text="Duration:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    durationLabel.place(x=425, y=8)
    durationValues = ["Infinite", "1 minute", "10 minutes", "1 hour", "Until rest", "Until dawn"]
    durationCombobox = ttk.Combobox(summonWindow, values=durationValues)
    durationCombobox.place(x=505, y=10)
    # makes a drop down box for the armor class 
    armorClassLabel = tk.Label(summonWindow, text="Armor Class:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    armorClassLabel.place(x=665, y=8)
    armorClassValues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    armorClassCombobox = ttk.Combobox(summonWindow, values=armorClassValues)
    armorClassCombobox.place(x=775, y=10)
    # makes a entry box for the description of creature
    descriptionLabel = tk.Label(summonWindow, text="Description:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    descriptionLabel.place(x=25, y=40)
    descriptionEntry = tk.Entry(summonWindow, width=125, background="#FFFFE0")
    descriptionEntry.place(x=135, y=42)
    # makes a entry box for the Hit Points
    hpLabel = tk.Label(summonWindow, text="Hit Points:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    hpLabel.place(x=25, y=72)
    hpEntry = tk.Entry(summonWindow, background="#FFFFE0")
    hpEntry.place(x=115, y=77)
    # makes a entry box for the Temp Points
    tempPointsLabel = tk.Label(summonWindow, text="Temp Points:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    tempPointsLabel.place(x=260, y=72)
    tempPointsEntry = tk.Entry(summonWindow, background="#FFFFE0")
    tempPointsEntry.place(x=365, y=77)
    # makes a drop down box for the walking speed
    walkingSpeedLabel = tk.Label(summonWindow, text="Walking Speed:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    walkingSpeedLabel.place(x=920, y=8)
    walkingSpeedValues = [0, 10, 20, 25, 30, 60, 90]
    walkingSpeedCombobox = ttk.Combobox(summonWindow, values=walkingSpeedValues)
    walkingSpeedCombobox.place(x=1055, y=10)
    # makes a drop down box for the swimming Speed
    swimmingSpeedLabel = tk.Label(summonWindow, text="Swimming Speed:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    swimmingSpeedLabel.place(x=920, y=40)
    swimmingSpeedValues = [0, 10, 20, 25, 30, 60, 90]
    swimmingSpeedCombobox = ttk.Combobox(summonWindow, values=swimmingSpeedValues)
    swimmingSpeedCombobox.place(x=1055, y=42)
    # makes a drop down box for the flying Speed
    flyingSpeedLabel = tk.Label(summonWindow, text="Flying Speed:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    flyingSpeedLabel.place(x=920, y=72)
    flyingSpeedValues = [0, 10, 20, 25, 30, 60, 90]
    flyingSpeedCombobox = ttk.Combobox(summonWindow, values=flyingSpeedValues)
    flyingSpeedCombobox.place(x=1055, y=77)
    # makes the main label fo the Abilities drop down boxes and buttonm
    abilitiesLabel = tk.Label(summonWindow, text="Abilities:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    abilitiesLabel.place(x=25, y=175)
    # the list of the ablitites
    abilityLabels = ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]
    abilityComboboxes = []
    # the values that will go in to the drop dow boxes
    abilityValues = ['8 (-1)', '9 (-1)', '10 (0)' , '11 (0)', '12 (1)', '13 (1)', '14 (2)', '15 (2)', '16 (3)', '17 (3)', '18 (4)', '19 (4)', '20 (5)']
    # thie loop takes the drop downs and buttons for all of the ablities in the list
    for i, label in enumerate(abilityLabels):
        abilityLabel = tk.Label(summonWindow, text=label, bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
        abilityLabel.place(x=115, y=i*35+120)
        abilityCombobox = ttk.Combobox(summonWindow, values=abilityValues, background="#E0E0E0")
        abilityCombobox.place(x=230, y=i*37+120)
        abilityComboboxes.append(abilityCombobox)

        abilityButton = tk.Button(summonWindow, text="Roll Check", command=lambda combobox=abilityCombobox: abilityCheckRoll(combobox), bg="Light Blue", fg="black", font=('Comic Sans MS', 12))
        abilityButton.place(x=400, y=i*35+120)
    # makes the main label fo the Abilities saves for the drop down boxes and buttonm
    abilitiesSavesLabel = tk.Label(summonWindow, text="Abilities Saves:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    abilitiesSavesLabel.place(x=505, y=175)
    # list of the ablility saves
    abilitiesSavesLabels = ["Strength Save:", "Dexterity Save:", "Constitution Save:", "Intelligence Save:", "Wisdom Save:", "Charisma Save:"]
    abilitiesSavesComboboxes = []
    # the values that will go into the drop down boxes
    abilitiesSavesValue = ('-5', '-4', '-3', '-2', '-1', '+0', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10', '+11', '+12', '+13', '+14', '+15', '+16', '+17')
    # thie loop takes the drop downs and buttons for all of the ablities saves in the list
    for i, label in enumerate(abilitiesSavesLabels):
        abilitiesSaveLabel = tk.Label(summonWindow, text=label, bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
        abilitiesSaveLabel.place(x=640, y=i*35+120)
        abilitiesSaveCombobox = ttk.Combobox(summonWindow, values=abilitiesSavesValue)
        abilitiesSaveCombobox.place(x=785, y=i*37+120)
        abilitiesSavesComboboxes.append(abilitiesSaveCombobox)

        abilitySavesButton = tk.Button(summonWindow, text="Roll Save", command=lambda combobox=abilitiesSaveCombobox: abilitySavesRoll(combobox), bg="Light Green", fg="black", font=('Comic Sans MS', 12))
        abilitySavesButton.place(x=935, y=i*35+120)
    # Create the buttons to add more attacks that trigger the assorted funtions for the add attack
    addAttackButton1 = tk.Button(summonWindow, text="Add Attack 1", command=addAttack1, bg="Light Gray", fg="black", font=('Comic Sans MS', 12))
    addAttackButton1.place(x=25, y=350)
    addAttackButton2 = tk.Button(summonWindow, text="Add Attack 2", command=addAttack2, bg="#C0C0C0", fg="black", font=('Comic Sans MS', 12))
    addAttackButton2.place(x=25, y=450)
    addAttackButton3 = tk.Button(summonWindow, text="Add Attack 3", command=addAttack3, bg="Dark Gray", fg="black", font=('Comic Sans MS', 12))
    addAttackButton3.place(x=25, y=550)
# when attackButton1 is pressed it adds entry boxes for name and description as well as drop down boxesand buttons for the to hit, type of dice, qty of dice, and damage modifier
def addAttack1():
    # makes the entry box for the attacks name
    attackNameLabel = tk.Label(summonWindow, text="Attack Name:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    attackNameLabel.place(x=150, y=350)
    attackNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    attackNameEntry.place(x=260, y=352)
    # makes the entry box for the description of the attack
    descriptionLabel = tk.Label(summonWindow, text="Description:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    descriptionLabel.place(x=400, y=350)
    descriptionEntry = tk.Entry(summonWindow, width=100, background="#FFFFE0")
    descriptionEntry.place(x=500, y=352)
    # makes the to hit drop down box
    toHitLabel = tk.Label(summonWindow, text="To Hit:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    toHitLabel.place(x=25, y=400)
    toHitValues = ['+0', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10']
    toHitValuesCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=toHitValues, width=5)
    toHitValuesCombobox.place(x=95, y=404)
    # the to hit button that triggers the rollToHit fuction
    toHitButton = tk.Button(summonWindow, text="Roll To Hit", command=lambda: rollToHit(toHitValuesCombobox), bg="Light Gray", fg="black", font=('Comic Sans MS', 12))
    toHitButton.place(x=150, y=400)
    # makes the drop down box for the type of dice for the damage roll
    diceTypeLabel = tk.Label(summonWindow, text="Type of Dice:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    diceTypeLabel.place(x=255, y=400)
    diceTypeValues = ['D2', 'D4', 'D6', 'D8', 'D10', 'D12']
    diceTypeCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=diceTypeValues, width=5)
    diceTypeCombobox.place(x=375, y=404)
    # makes the drop down boxes for the quanty of damage dice
    qtyDiceLabel = tk.Label(summonWindow, text="Qty of Dice:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    qtyDiceLabel.place(x=430, y=400)
    qtyOfDiceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    qtyDiceCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=qtyOfDiceValues, width=5)
    qtyDiceCombobox.place(x=535, y=404)
    # makes the drop down box for the damage modifier
    damageModifierLabel = tk.Label(summonWindow, text="Damage Modifier:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    damageModifierLabel.place(x=590, y=400)
    damageModifierValues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    damageModifierCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=damageModifierValues, width=5)
    damageModifierCombobox.place(x=735, y=404)
    # Makes the button for the damage roll triggering the displayDamageResult to get the result
    damageButton = tk.Button(summonWindow, text="Calculate Damage", command=lambda: displayDamageResult(qtyDiceCombobox, diceTypeCombobox, damageModifierCombobox), bg="light salmon", fg="black", font=('Comic Sans MS', 12))
    damageButton.place(x=800, y=400)
    # makes the button for the crit damage roll triggering the displayCritDamageResult to get eh result of the roll
    critDamageButton = tk.Button(summonWindow, text="Crit!", command=lambda: displayCritDamageResult(qtyDiceCombobox, diceTypeCombobox, damageModifierCombobox), bg="red", fg="white", font=('Comic Sans MS', 12))
    critDamageButton.place(x=950, y=400)

    return toHitValuesCombobox, qtyDiceCombobox, diceTypeCombobox, damageModifierCombobox
# when attackButton2 is pressed it adds entry boxes for name and description as well as drop down boxesand buttons for the to hit, type of dice, qty of dice, and damage modifier
def addAttack2():
    # makes the entry box for the attacks name
    attackNameLabel = tk.Label(summonWindow, text="Attack Name:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    attackNameLabel.place(x=150, y=450)
    attackNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    attackNameEntry.place(x=260, y=450)
    # makes the entry box for the description of the attack
    descriptionLabel = tk.Label(summonWindow, text="Description:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    descriptionLabel.place(x=400, y=450)
    descriptionEntry = tk.Entry(summonWindow, width=100, background="#FFFFE0")
    descriptionEntry.place(x=500, y=450)
    # makes the to hit drop down box
    toHitLabel = tk.Label(summonWindow, text="To Hit:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    toHitLabel.place(x=25, y=500)
    toHitValues = ['+0', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10']
    toHitValuesCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=toHitValues, width=5)
    toHitValuesCombobox.place(x=95, y=504)
    # the to hit button that triggers the rollToHit fuction
    toHitButton = tk.Button(summonWindow, text="Roll To Hit", command=lambda: rollToHit(toHitValuesCombobox), bg="Light Gray", fg="black", font=('Comic Sans MS', 12))
    toHitButton.place(x=150, y=500)
    # makes the drop down box for the type of dice for the damage roll
    diceTypeLabel = tk.Label(summonWindow, text="Type of Dice:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    diceTypeLabel.place(x=255, y=500)
    diceTypeValues = ['D2', 'D4', 'D6', 'D8', 'D10', 'D12']
    diceTypeCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=diceTypeValues, width=5)
    diceTypeCombobox.place(x=375, y=504)
    # makes the drop down boxes for the quanty of damage dice
    qtyDiceLabel = tk.Label(summonWindow, text="Qty of Dice:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    qtyDiceLabel.place(x=430, y=500)
    qtyOfDiceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    qtyDiceCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=qtyOfDiceValues, width=5)
    qtyDiceCombobox.place(x=535, y=504)
    # makes the drop down box for the damage modifier
    damageModifierLabel = tk.Label(summonWindow, text="Damage Modifier:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    damageModifierLabel.place(x=590, y=500)
    damageModifierValues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    damageModifierCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=damageModifierValues, width=5)
    damageModifierCombobox.place(x=735, y=504)
    # Makes the button for the damage roll triggering the displayDamageResult to get the result
    damageButton = tk.Button(summonWindow, text="Calculate Damage", command=lambda: displayDamageResult(damageModifierCombobox, qtyDiceCombobox, diceTypeCombobox), bg="light salmon", fg="black", font=('Comic Sans MS', 12))
    damageButton.place(x=800, y=500)
    # makes the button for the crit damage roll triggering the displayCritDamageResult to get eh result of the roll
    critDamageButton = tk.Button(summonWindow, text="Crit!", command=lambda: displayCritDamageResult(damageModifierCombobox, qtyDiceCombobox, diceTypeCombobox), bg="red", fg="white", font=('Comic Sans MS', 12))
    critDamageButton.place(x=950, y=500)

    return toHitValuesCombobox, qtyDiceCombobox, diceTypeCombobox, damageModifierCombobox
# when attackButton3 is pressed it adds entry boxes for name and description as well as drop down boxesand buttons for the to hit, type of dice, qty of dice, and damage modifier
def addAttack3():
    # makes the entry box for the attacks name
    attackNameLabel = tk.Label(summonWindow, text="Attack Name:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    attackNameLabel.place(x=150, y=550)
    attackNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    attackNameEntry.place(x=260, y=550)
    # makes the entry box for the description of the attack
    descriptionLabel = tk.Label(summonWindow, text="Description:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    descriptionLabel.place(x=400, y=550)
    descriptionEntry = tk.Entry(summonWindow, width=100, background="#FFFFE0")
    descriptionEntry.place(x=500, y=550)
    # makes the to hit drop down box
    toHitLabel = tk.Label(summonWindow, text="To Hit:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    toHitLabel.place(x=25, y=600)
    toHitValues = ['+0', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10']
    toHitValuesCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=toHitValues, width=5)
    toHitValuesCombobox.place(x=95, y=604)
    # the to hit button that triggers the rollToHit fuction
    toHitButton = tk.Button(summonWindow, text="Roll To Hit", command=lambda: rollToHit(toHitValuesCombobox), bg="Light Gray", fg="black", font=('Comic Sans MS', 12))
    toHitButton.place(x=150, y=600)
    # makes the drop down box for the type of dice for the damage roll
    diceTypeLabel = tk.Label(summonWindow, text="Type of Dice:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    diceTypeLabel.place(x=255, y=600)
    diceTypeValues = ['D2', 'D4', 'D6', 'D8', 'D10', 'D12']
    diceTypeCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=diceTypeValues, width=5)
    diceTypeCombobox.place(x=375, y=604)
    # makes the drop down boxes for the quanty of damage dice
    qtyDiceLabel = tk.Label(summonWindow, text="Qty of Dice:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    qtyDiceLabel.place(x=430, y=600)
    qtyOfDiceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    qtyDiceCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=qtyOfDiceValues, width=5)
    qtyDiceCombobox.place(x=535, y=604)
    # makes the drop down box for the damage modifier
    damageModifierLabel = tk.Label(summonWindow, text="Damage Modifier:", bg="#D2B48C", fg="black", font=('Comic Sans MS', 12))
    damageModifierLabel.place(x=590, y=600)
    damageModifierValues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    damageModifierCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=damageModifierValues, width=5)
    damageModifierCombobox.place(x=735, y=604)
    # Makes the button for the damage roll triggering the displayDamageResult to get the result
    damageButton = tk.Button(summonWindow, text="Calculate Damage", command=lambda: displayDamageResult(damageModifierCombobox, qtyDiceCombobox, diceTypeCombobox), bg="light salmon", fg="black", font=('Comic Sans MS', 12))
    damageButton.place(x=800, y=600)
    # makes the button for the crit damage roll triggering the displayCritDamageResult to get eh result of the roll
    critDamageButton = tk.Button(summonWindow, text="Crit!", command=lambda: displayCritDamageResult(damageModifierCombobox, qtyDiceCombobox, diceTypeCombobox), bg="red", fg="white", font=('Comic Sans MS', 12))
    critDamageButton.place(x=950, y=600)

    return toHitValuesCombobox, qtyDiceCombobox, diceTypeCombobox, damageModifierCombobox

# used to generate a d20 roll add the modifier, triggered when the to hit button is hit
def rollToHit(toHitValuesCombobox):
    try:
        toHitValue = int(toHitValuesCombobox.get().replace('+', ''))
        toHitRoll = random.randint(1, 20)
        toHitValueResult = toHitRoll + toHitValue
        # Create a new window to display the result
        resultWindow = tk.Toplevel()
        resultWindow.title("To-Hit Result")
        resultWindow.geometry("370x250")
        # adds the image to the background of the rollToHit results window
        image_path = "toHitRoll.jpg"
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(resultWindow, image=photo)
        image_label.image = photo
        image_label.place(x=0, y=0)
        # Check if it's a critical hit or not and will give the right text on the result window
        if toHitRoll == 20:
            resultLabel = tk.Label(resultWindow, background="light yellow", fg="Red", text="Critical hit!", font=('Comic Sans MS', 20))
        else:
            resultLabel = tk.Label(resultWindow, background="light yellow", fg="black", text=f"{toHitValueResult}\nTo Hit!", font=('Comic Sans MS', 20))
        resultLabel.place(x=120, y=90)
        resultLabel.config(anchor=tk.CENTER)
        
        resultWindow.mainloop()
    # makes a error message pop up if the user did not pick anything in the drop down boxes
    except ValueError:
        messagebox.showinfo("To-Hit Result", "Invalid input")
    return toHitRoll
# used to generate a roll of they type of dice picked and then doubling the qty of dice. triggered by the crit button
def displayCritDamageResult(qtyDiceCombobox, diceTypeCombobox, damageModifierCombobox):
    try:
        # makes the window for the crit damage result
        resultWindow = tk.Toplevel()
        resultWindow.title("Crit Damage Result")
        resultWindow.geometry("370x250")
        # adds a image to the background of the results window
        image_path = "critDamage.jpg"
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(resultWindow, image=photo)
        image_label.image = photo
        image_label.place(x=0, y=0)
        # Retrieve the values from the comboboxes of the type of dice, qty of dice, and the damage modifier
        qtyOfDice = int(qtyDiceCombobox.get())
        damageDice = int(diceTypeCombobox.get().replace('D', ''))
        damageMod = int(damageModifierCombobox.get())
        qtyOfDice = qtyOfDice * 2 # doubles the qty of the dice
        # Roll for damage and add the damage modifier
        damageResult = rollDamage(qtyOfDice, damageDice) # uses the rollDamage function to generate the d20 roll
        damageResult = damageResult + damageMod
        # Create a label to display the damage result
        resultLabel = tk.Label(resultWindow, background="black", fg="red", text=f"!!CRITICAL DAMAGE!!\nThe Result is:\n{damageResult}", font=('Comic Sans MS', 18))
        resultLabel.place(x=60, y=50)
        resultLabel.config(anchor=tk.CENTER)

        resultWindow.mainloop()
    # makes a pop up error message window if any of the drop downs used in this function do not have values picked
    except ValueError:
        messagebox.showinfo("Crit Damage Roll", "Invalid input")
# makes a results window for the normal damage rolled and adding the damage modifier to the roll, this is triggered but the attack damage button is hit
def displayDamageResult(qtyDiceCombobox, diceTypeCombobox, damageModifierCombobox):
    try:
        #makes the window for the damage result roll
        resultWindow = tk.Toplevel()
        resultWindow.title("Damage Result")
        resultWindow.geometry("370x250")
        # puts a image in the background
        image_path = "damageRoll.jpg"
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(resultWindow, image=photo)
        image_label.image = photo
        image_label.place(x=0, y=0)
        # Retrieve the values from the comboboxes foe the type of dice, qty of dice and the damage modifier
        qtyOfDice = int(qtyDiceCombobox.get())
        damageDice = int(diceTypeCombobox.get().replace('D', ''))
        damageMod = int(damageModifierCombobox.get())
        # Roll for damage and add the modifier
        damageResult = rollDamage(qtyOfDice, damageDice) # uses the rollDamage function to generate the d20 roll
        damageResult = damageResult + damageMod
        # Create a label to display the damage result
        resultLabel = tk.Label(resultWindow, text=f"The Attack Damage Result:\n{damageResult}", bg="black", fg="white", font=('Comic Sans MS', 18))
        resultLabel.place(x=30, y=50)
        resultLabel.config(anchor=tk.CENTER)

        resultWindow.mainloop()
    # makes a pop up error message window if any of the drop downs used in this function do not have values picked
    except ValueError:
        messagebox.showinfo("Damage Result", "Invalid input")
 # generates the d20 roll
def rollDamage(qtyOfDice, damageDice):
    damageResult = 0
    for _ in range(qtyOfDice):
        roll = random.randint(1, damageDice)
        damageResult += roll
    return damageResult
# is trigged by the roll chheck button and make a results window
def abilityCheckRoll(abilityCombobox):
    try:
        # makes the results window
        resultWindow = tk.Toplevel()
        resultWindow.title("Ability Check")
        resultWindow.geometry("370x250")
        # puts a image in the background
        image_path = "abilityChecks.jpg"
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(resultWindow, image=photo)
        image_label.image = photo
        image_label.place(x=0, y=0)
        # Retrieve the value from the combobox
        selectedValue = abilityCombobox.get()
        abilityCheck = int(selectedValue.split(' ')[-1][1:-1])
        # rolls a d20 and adds the ablilty modifier
        abilityCheckResult = 0
        for _ in range(1):
            roll = random.randint(1, 20)
            abilityCheckResult = roll + abilityCheck
        # Create a label to display the ability check result
        resultLabel = tk.Label(resultWindow, text=f"The Ability Check Result:\n{abilityCheckResult}",bg="light blue", fg="purple", font=('Comic Sans MS', 18))
        resultLabel.place(x=30, y=60)
        resultLabel.config(anchor=tk.CENTER)

        resultWindow.mainloop()
    # makes a pop up error message window if any of the drop downs used in this function do not have values picked
    except ValueError:
        messagebox.showinfo("Ability Check", "Invalid input")
# is trigged by the roll save button and make a results window
def abilitySavesRoll(abilitiesSaveCombobox):
    try:
        # makes the window pop up
        resultWindow = tk.Toplevel()
        resultWindow.title("Ability Save Check")
        resultWindow.geometry("370x250")
        # puts a image on the background
        image_path = "abilitySaves.jpg"
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(resultWindow, image=photo)
        image_label.image = photo
        image_label.place(x=0, y=0)
        # Retrieve the value from the combobox
        selectedValue = abilitiesSaveCombobox.get()
        abilitySaves = int(selectedValue.split(' ')[-1])
        # rolls a d20 and adds the ablilty modifier
        abilitySavesResult = 0
        for _ in range(1):
            roll = random.randint(1, 20)
            abilitySavesResult = roll + abilitySaves

        # Create a label to display the ability check result
        resultLabel = tk.Label(resultWindow, text=f"The Ability Save Result:\n{abilitySavesResult}", bg="black", fg="light blue", font=('Comic Sans MS', 18))
        resultLabel.place(x=45, y=60)
        resultLabel.config(anchor=tk.CENTER)

        resultWindow.mainloop()
    # makes a pop up error message window if any of the drop downs used in this function do not have values picked
    except ValueError:
        messagebox.showinfo("Ability Save Check", "Invalid input")

'''
def captureSummonData(summonWindow):
    summonData = {}

    summonData['summonName'] = summonWindow.summonNameEntry.get()
    summonData['type'] = summonWindow.typeCombobox.get()
    summonData['duration'] = summonWindow.durationCombobox.get()
    summonData['description'] = summonWindow.descriptionEntry.get()
    summonData['hp'] = summonWindow.hpEntry.get()
    summonData['tempPoints'] = summonWindow.tempPointsEntry.get()
    summonData['walkingSpeed'] = summonWindow.walkingSpeedCombobox.get()
    summonData['swimmingSpeed'] = summonWindow.swimmingSpeedCombobox.get()
    summonData['flyingSpeed'] = summonWindow.flyingSpeedCombobox.get()

    ability_values = []
    for combobox in summonWindow.abilityComboboxes:
        ability_values.append(combobox.get())
    summonData['abilities'] = ability_values

    abilities_saves = []
    for combobox in summonWindow.abilitiesSavesComboboxes:
        abilities_saves.append(combobox.get())
    summonData['abilitiesSaves'] = abilities_saves

    attacks = []
    attack_functions = [summonWindow.addAttack1, summonWindow.addAttack2, summonWindow.addAttack3]

    for attack_function in attack_functions:
        attack = attack_function()
        attacks.append(attack)

    summonData['attacks'] = attacks

    return summonData

def saveButtonClick(summonData):
    filename = f"{summonData['summonName']}.txt"

    # Save the summon data to the file
    with open(filename, 'w') as file:
        file.write(str(summonData))
        file.close()

    saveWindow = tk.Toplevel()
    saveWindow.title("Saving")
    saveWindow.geometry("200x200")
    saveLabel = tk.Label(saveWindow, text=f"Saving: {filename}")
    saveLabel.grid(row=1, column=1, padx=100, pady=50)

    saveWindow.mainloop()
    '''
'''
def loadButtonClick():
    filename = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if filename:
        readEntries(filename)
        print("Entries were loaded from", filename, "file.")'''
