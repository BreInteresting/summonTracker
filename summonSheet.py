import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox
from tkinter import filedialog


def summon():
    global summonWindow

    summonWindow = tk.Toplevel()
    summonWindow.title("New Summon")
    summonWindow.geometry("1700x500")
    summonWindow.configure(background="#E0E0E0")

    # name
    summonNameLabel = tk.Label(summonWindow, text="Name:", background="#E0E0E0", fg="black", font=("arial", 9))
    summonNameLabel.grid(row=0, column=0, padx=5)
    summonNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    summonNameEntry.grid(row=0, column=1, padx=5)
    # type
    typeLabel = tk.Label(summonWindow, text="Type:", background="#E0E0E0", fg="black", font=("arial", 9))
    typeLabel.grid(row=0, column=2, padx=5)
    typeValues = ["Aberration", "Beast", "Celestial", "Construct","Dragon", "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Undead"]
    typeCombobox = ttk.Combobox(summonWindow, values=typeValues, style='CustomStyle.TCombobox')
    typeCombobox.grid(row=0, column=3, padx=5)

    # Create a custom style for the combobox
    style = ttk.Style()
    style.theme_create('CustomStyle', parent='alt',
                       settings={'TCombobox': {'configure': {'selectbackground': '#E0E0E0',
                                                             'fieldbackground': '#E0E0E0',
                                                             'foreground': 'black',
                                                             'selectforeground': 'black',
                                                             'arrowcolor': 'black'}}})
    style.theme_use('CustomStyle')

    # duration
    durationLabel = tk.Label(summonWindow, text="Duration:", background="#E0E0E0", fg="black", font=("arial", 9))
    durationLabel.grid(row=0, column=4, sticky=tk.E)
    durationValues = ["Infinite", "1 minute", "10 minutes", "1 hour", "Until rest", "Until dawn"]
    durationCombobox = ttk.Combobox(summonWindow, values=durationValues)
    durationCombobox.grid(row=0, column=5)

        # armor class
    armorClassLabel = tk.Label(summonWindow, text="Armor Class:", background="#E0E0E0", fg="black", font=("arial", 9))
    armorClassLabel.grid(row=0, column=6, padx=5)
    armorClassValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    armorClassCombobox = ttk.Combobox(summonWindow, values=armorClassValues)
    armorClassCombobox.grid(row=0, column=7, padx=5)
    
    # description of creature
    descriptionLabel = tk.Label(summonWindow, text="Description:", background="#E0E0E0", fg="black", font=("arial", 9))
    descriptionLabel.grid(row=1, column=0, padx=5)
    descriptionEntry = tk.Entry(summonWindow, background="#FFFFE0")
    descriptionEntry.grid(row=1, column=1, padx=5)
    # Hit Points
    hpLabel = tk.Label(summonWindow, text="Hit Points:", background="#E0E0E0", fg="black", font=("arial", 9))
    hpLabel.grid(row=2, column=0, padx=5)
    hpEntry = tk.Entry(summonWindow, background="#FFFFE0")
    hpEntry.grid(row=2, column=1, padx=5)
    # Temp Points
    tempPointsLabel = tk.Label(summonWindow, text="Temp Points:", background="#E0E0E0", fg="black", font=("arial", 9))
    tempPointsLabel.grid(row=2, column=2)
    tempPointsEntry = tk.Entry(summonWindow, background="#FFFFE0")
    tempPointsEntry.grid(row=2, column=3)
    # walking Speed
    walkingSpeedLabel = tk.Label(summonWindow, text="Walking Speed:", background="#E0E0E0", fg="black", font=("arial", 9))
    walkingSpeedLabel.grid(row=2, column=4, sticky=tk.E)
    walkingSpeedValues = [0, 10, 20, 25, 30, 60, 90]
    walkingSpeedCombobox = ttk.Combobox(summonWindow, values=walkingSpeedValues)
    walkingSpeedCombobox.grid(row=2, column=5, sticky=tk.W)
    # swimming Speed
    swimmingSpeedLabel = tk.Label(summonWindow, text="Swimming Speed:", background="#E0E0E0", fg="black", font=("arial", 9))
    swimmingSpeedLabel.grid(row=2, column=6, sticky=tk.W)
    swimmingSpeedValues = [0, 10, 20, 25, 30, 60, 90]
    swimmingSpeedCombobox = ttk.Combobox(summonWindow, values=swimmingSpeedValues)
    swimmingSpeedCombobox.grid(row=2, column=7, sticky=tk.W)
    # flyingSpeed
    flyingSpeedLabel = tk.Label(summonWindow, text="Flying Speed:", background="#E0E0E0", fg="black", font=("arial", 9))
    flyingSpeedLabel.grid(row=2, column=8, sticky=tk.W)
    flyingSpeedValues = [0, 10, 20, 25, 30, 60, 90]
    flyingSpeedCombobox = ttk.Combobox(summonWindow, values=flyingSpeedValues)
    flyingSpeedCombobox.grid(row=2, column=9, sticky=tk.W)

    # Abilities
    abilitiesLabel = tk.Label(summonWindow, text="Abilities:", background="#E0E0E0", fg="black", font=("arial", 9))
    abilitiesLabel.grid(row=3, column=0, sticky=tk.E)

    abilityFrame = tk.Frame(summonWindow, background="#E0E0E0")
    abilityFrame.grid(row=3, column=1, sticky=tk.E)

    abilityLabels = ["Strength:", "Dexterity:", "Constitution:", "Intelligence:", "Wisdom:", "Charisma:"]
    abilityComboboxes = []

    abilityValues = ['8 (-1)', '9 (-1)', '10 (0)' , '11 (0)', '12 (1)', '13 (1)', '14 (2)', '15 (2)', '16 (3)', '17 (3)', '18 (4)', '19 (4)', '20 (5)']

    for i, label in enumerate(abilityLabels):
        abilityLabel = tk.Label(abilityFrame, text=label, background="#E0E0E0", fg="black", font=("arial", 9))
        abilityLabel.grid(row=i, column=0, sticky=tk.W)
        abilityCombobox = ttk.Combobox(abilityFrame, values=abilityValues, background="#E0E0E0")
        abilityCombobox.grid(row=i, column=1, sticky=tk.W)
        abilityComboboxes.append(abilityCombobox)

        abilityButton = tk.Button(abilityFrame, text="Roll Check", command=lambda combobox=abilityCombobox: abilityCheckRoll(combobox), bg="Light Blue", fg="black", font=("arial", 9))
        abilityButton.grid(row=i, column=2, sticky=tk.W)

    # Abilities Saves
    abilitiesSavesLabel = tk.Label(summonWindow, text="Abilities Saves:", background="#E0E0E0", fg="black", font=("arial", 9))
    abilitiesSavesLabel.grid(row=3, column=3, sticky=tk.E)

    abilitiesSavesFrame = tk.Frame(summonWindow, background="#E0E0E0")
    abilitiesSavesFrame.grid(row=3, column=4, sticky=tk.E)

    abilitiesSavesLabels = ["Strength Save:", "Dexterity Save:", "Constitution Save:", "Intelligence Save:", "Wisdom Save:", "Charisma Save:"]
    abilitiesSavesComboboxes = []

    abilitiesSavesValue = ('-5', '-4', '-3', '-2', '-1', '+0', '+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10', '+11', '+12', '+13', '+14', '+15', '+16', '+17')

    for i, label in enumerate(abilitiesSavesLabels):
        abilitiesSaveLabel = tk.Label(abilitiesSavesFrame, text=label, background="#E0E0E0", fg="black", font=("arial", 9))
        abilitiesSaveLabel.grid(row=i, column=3, sticky=tk.W)
        abilitiesSaveCombobox = ttk.Combobox(abilitiesSavesFrame, values=abilitiesSavesValue)
        abilitiesSaveCombobox.grid(row=i, column=4, sticky=tk.W)
        abilitiesSavesComboboxes.append(abilitiesSaveCombobox)

        abilitySavesButton = tk.Button(abilitiesSavesFrame, text="Roll Save", command=lambda combobox=abilitiesSaveCombobox: abilitySavesRoll(combobox), bg="Light Green", fg="black", font=("arial", 9))
        abilitySavesButton.grid(row=i, column=5, sticky=tk.W)

    # Create the button to add more attacks
    addAttackButton1 = tk.Button(summonWindow, text="Add Attack 1", command=addAttack1, bg="Light Gray", fg="black", font=("arial", 9))
    addAttackButton1.grid(row=13, column=1, sticky=tk.W)
    addAttackButton2 = tk.Button(summonWindow, text="Add Attack 2", command=addAttack2, bg="#C0C0C0", fg="black", font=("arial", 9))
    addAttackButton2.grid(row=16, column=1, sticky=tk.W)
    addAttackButton3 = tk.Button(summonWindow, text="Add Attack 3", command=addAttack3, bg="Dark Gray", fg="black", font=("arial", 9))
    addAttackButton3.grid(row=19, column=1, sticky=tk.W)

def addAttack1():
    attackNameLabel = tk.Label(summonWindow, text="Attack Name:", background="#E0E0E0", fg="black", font=("arial", 9))
    attackNameLabel.grid(row=14, column=0, sticky=tk.W)
    attackNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    attackNameEntry.grid(row=14, column=1, sticky=tk.W)

    descriptionLabel = tk.Label(summonWindow, text="Description:", background="#E0E0E0", fg="black", font=("arial", 9))
    descriptionLabel.grid(row=14, column=2, sticky=tk.W)
    descriptionEntry = tk.Entry(summonWindow, background="#FFFFE0")
    descriptionEntry.grid(row=14, column=3, sticky=tk.W) 

    toHitLabel = tk.Label(summonWindow, text="To Hit:", background="Light Gray", fg="black", font=("arial", 9))
    toHitLabel.grid(row=15, column=0)

    # Create a Combobox widget
    toHitValues = ['+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10']
    toHitValuesCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=toHitValues, width=5)
    toHitValuesCombobox.grid(row=15, column=1, sticky=tk.W)

    toHitButton = tk.Button(summonWindow, text="Roll To Hit", command=lambda: rollToHit(toHitValuesCombobox), bg="Light Gray", fg="black", font=("arial", 9))
    toHitButton.grid(row=15, column=2)

    diceTypeLabel = tk.Label(summonWindow, text="Type of Dice:", background="#E0E0E0", fg="black", font=("arial", 9))
    diceTypeLabel.grid(row=15, column=3, sticky=tk.W)
    diceTypeValues = ['D2', 'D4', 'D6', 'D8', 'D10', 'D12']
    diceTypeCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=diceTypeValues, width=5)
    diceTypeCombobox.grid(row=15, column=4, sticky=tk.W)

    qtyDiceLabel = tk.Label(summonWindow, text="Qty of Dice:", background="#E0E0E0", fg="black", font=("arial", 9))
    qtyDiceLabel.grid(row=15, column=5, sticky=tk.W)
    qtyOfDiceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    qtyDiceCombobox = ttk.Combobox(summonWindow, background="Light Gray", values=qtyOfDiceValues, width=5)
    qtyDiceCombobox.grid(row=15, column=6, padx=5, sticky=tk.W)

    damageButton = tk.Button(summonWindow, text="Calculate Damage", command=lambda: displayDamageResult(qtyDiceCombobox, diceTypeCombobox), bg="light salmon", fg="black", font=("arial", 9))
    damageButton.grid(row=15, column=7, padx=5, sticky=tk.W)

    critDamageButton = tk.Button(summonWindow, text="Crit!", command=lambda: displayCritDamageResult(qtyDiceCombobox, diceTypeCombobox), bg="red", fg="white", font=("arial", 9))
    critDamageButton.grid(row=15, column=8, padx=5, sticky=tk.W)

    return toHitValuesCombobox, qtyDiceCombobox, diceTypeCombobox

def addAttack2():
    attackNameLabel = tk.Label(summonWindow, text="Attack Name:", background="#E0E0E0", fg="black", font=("arial", 9))
    attackNameLabel.grid(row=17, column=0,  sticky=tk.W)
    attackNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    attackNameEntry.grid(row=17, column=1, sticky=tk.W)

    descriptionLabel = tk.Label(summonWindow, text="Description:", background="#E0E0E0", fg="black", font=("arial", 9))
    descriptionLabel.grid(row=17, column=2, sticky=tk.W)
    descriptionEntry = tk.Entry(summonWindow, background="#FFFFE0")
    descriptionEntry.grid(row=17, column=3, sticky=tk.W)

    toHitLabel = tk.Label(summonWindow, text="To Hit:", background="#C0C0C0", fg="black", font=("arial", 9))
    toHitLabel.grid(row=18, column=0)

    # Create a Combobox widget
    toHitValues = ['+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10']
    toHitValuesCombobox = ttk.Combobox(summonWindow, background="#C0C0C0", values=toHitValues, width=5)
    toHitValuesCombobox.grid(row=18, column=1, sticky=tk.W)

    toHitButton = tk.Button(summonWindow, text="Roll To Hit", command=lambda: rollToHit(toHitValuesCombobox), bg="#C0C0C0", fg="black", font=("arial", 9))
    toHitButton.grid(row=18, column=2)

    diceTypeLabel = tk.Label(summonWindow, text="Type of Dice:", background="#E0E0E0", fg="black", font=("arial", 9))
    diceTypeLabel.grid(row=18, column=3, sticky=tk.W)
    diceTypeValues = ['D2', 'D4', 'D6', 'D8', 'D10', 'D12']
    diceTypeCombobox = ttk.Combobox(summonWindow, background="#C0C0C0", values=diceTypeValues, width=5)
    diceTypeCombobox.grid(row=18, column=4, sticky=tk.W)

    qtyDiceLabel = tk.Label(summonWindow, text="Qty of Dice:", background="#E0E0E0", fg="black", font=("arial", 9))
    qtyDiceLabel.grid(row=18, column=5, sticky=tk.W)
    qtyOfDiceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    qtyDiceCombobox = ttk.Combobox(summonWindow, background="#C0C0C0", values=qtyOfDiceValues, width=5)
    qtyDiceCombobox.grid(row=17, column=6, padx=5, sticky=tk.W)

    damageButton = tk.Button(summonWindow, text="Calculate Damage", command=lambda: displayDamageResult(qtyDiceCombobox, diceTypeCombobox), bg="light salmon", fg="black", font=("arial", 9))
    damageButton.grid(row=18, column=7, padx=5, sticky=tk.W)

    critDamageButton = tk.Button(summonWindow, text="Crit!", command=lambda: displayCritDamageResult(qtyDiceCombobox, diceTypeCombobox), bg="red", fg="white", font=("arial", 9))
    critDamageButton.grid(row=18, column=8, padx=5, sticky=tk.W)

    return toHitValuesCombobox, qtyDiceCombobox, diceTypeCombobox

def addAttack3():
    # Create the widgets for the new attack cell
    attackNameLabel = tk.Label(summonWindow, text="Attack Name:", background="#E0E0E0", fg="black", font=("arial", 9))
    attackNameLabel.grid(row=20, column=0, sticky=tk.W)
    attackNameEntry = tk.Entry(summonWindow, background="#FFFFE0")
    attackNameEntry.grid(row=20, column=1, sticky=tk.W)

    descriptionLabel = tk.Label(summonWindow, text="Description:", background="#E0E0E0", fg="black", font=("arial", 9))
    descriptionLabel.grid(row=20, column=2, sticky=tk.W)
    descriptionEntry = tk.Entry(summonWindow, background="#FFFFE0")
    descriptionEntry.grid(row=20, column=3, sticky=tk.W)

    toHitLabel = tk.Label(summonWindow, text="To Hit:", background="#E0E0E0", fg="black", font=("arial", 9))
    toHitLabel.grid(row=21, column=0)

    # Create a Combobox widget
    toHitValues = ['+1', '+2', '+3', '+4', '+5', '+6', '+7', '+8', '+9', '+10']
    toHitValuesCombobox = ttk.Combobox(summonWindow, background="Dark Gray", values=toHitValues, width=5)
    toHitValuesCombobox.grid(row=21, column=1, padx=5, sticky=tk.W)

    toHitButton = tk.Button(summonWindow, text="Roll To Hit", command=lambda: rollToHit(toHitValuesCombobox), bg="Dark Gray", fg="black", font=("arial", 9))
    toHitButton.grid(row=21, column=2, padx=5, sticky=tk.W)

    diceTypeLabel = tk.Label(summonWindow, text="Type of Dice:", background="#E0E0E0", fg="black", font=("arial", 9))
    diceTypeLabel.grid(row=21, column=3, sticky=tk.W)
    diceTypeValues = ['D2', 'D4', 'D6', 'D8', 'D10', 'D12']
    diceTypeCombobox = ttk.Combobox(summonWindow, background="Dark Gray", values=diceTypeValues, width=5)
    diceTypeCombobox.grid(row=21, column=4, sticky=tk.W)

    qtyDiceLabel = tk.Label(summonWindow, text="Qty of Dice:", background="#E0E0E0", fg="black", font=("arial", 9))
    qtyDiceLabel.grid(row=21, column=5, sticky=tk.W)
    qtyOfDiceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    qtyDiceCombobox = ttk.Combobox(summonWindow, background="Dark Gray", values=qtyOfDiceValues, width=5)
    qtyDiceCombobox.grid(row=21, column=6, padx=5, sticky=tk.W)

    damageButton = tk.Button(summonWindow, text="Calculate Damage", command=lambda: displayDamageResult(qtyDiceCombobox, diceTypeCombobox), bg="light salmon", fg="black", font=("arial", 9))
    damageButton.grid(row=21, column=7, padx=5, sticky=tk.W)
    
    critDamageButton = tk.Button(summonWindow, text="Crit!", command=lambda: displayCritDamageResult(qtyDiceCombobox, diceTypeCombobox), bg="Red", fg="white", font=("arial", 9))
    critDamageButton.grid(row=21, column=8, padx=5, sticky=tk.W)

    return toHitValuesCombobox,qtyDiceCombobox, diceTypeCombobox

# used to generate a d20 roll as will as the modifier beign added
def rollToHit(toHitValuesCombobox):
    try:
        toHitValue = int(toHitValuesCombobox.get().replace('+', ''))
        toHitRoll = random.randint(1, 20)
        toHitValueResult = toHitRoll + toHitValue
        # Create a new window to display the result
        resultWindow = tk.Toplevel()
        resultWindow.title("To-Hit Result")
        resultWindow.geometry("340x150")
        resultWindow.configure(background="Orange")

        # Check if it's a critical hit
        if toHitRoll == 20:
            resultLabel = tk.Label(resultWindow, background="Red", fg="White", text="Critical hit!", width=20, height=4, font=('arial', 20))
        else:
            resultLabel = tk.Label(resultWindow, background="Orange", fg="White", text=f"{toHitValueResult}\nTo Hit!", width=20, height=4, font=('arial', 20))
        
        resultLabel.grid(row=1, column=1, padx=1, pady=5)
        resultLabel.config(anchor=tk.CENTER)
        
        resultWindow.mainloop()
    except ValueError:
        messagebox.showinfo("To-Hit Result", "Invalid input")
    return toHitRoll

def displayCritDamageResult(qtyDiceCombobox, diceTypeCombobox):
    resultWindow = tk.Toplevel()
    resultWindow.title("Crit Damage Result")
    resultWindow.geometry("355x150")
    resultWindow.configure(background="Red")
    # Retrieve the values from the comboboxes
    qtyOfDice = int(qtyDiceCombobox.get())
    damageDice = int(diceTypeCombobox.get().replace('D', ''))
    qtyOfDice = qtyOfDice * 2
    # Roll for damage
    damageResult = rollDamage(qtyOfDice, damageDice)
    # Create a label to display the damage result
    resultLabel = tk.Label(resultWindow,background="Red", fg="white", text=f"!!CRITICAL DAMAGE!!\nThe Result is:\n{damageResult}", width=25, height=5, font=('arial', 18))
    resultLabel.grid(row=1, column=1, padx=1, pady=5)
    resultLabel.config(anchor=tk.CENTER)

    resultWindow.mainloop()

def displayDamageResult(qtyDiceCombobox, diceTypeCombobox):
    resultWindow = tk.Toplevel()
    resultWindow.title("Damage Result")
    resultWindow.geometry("345x150")
    resultWindow.configure(background="#FF9999")
    # Retrieve the values from the comboboxes
    qtyOfDice = int(qtyDiceCombobox.get())
    damageDice = int(diceTypeCombobox.get().replace('D', ''))

    # Roll for damage
    damageResult = rollDamage(qtyOfDice, damageDice)

    # Create a label to display the damage result
    resultLabel = tk.Label(resultWindow, background="#FF9999", text=f"The Attack Damage Result is:\n{damageResult}", width=25, height=5, font=('arial', 18))
    resultLabel.grid(row=1, column=1, padx=1, pady=5)
    resultLabel.config(anchor=tk.CENTER)

    resultWindow.mainloop()

def rollDamage(qtyOfDice, damageDice):
    damageResult = 0
    for _ in range(qtyOfDice):
        roll = random.randint(1, damageDice)
        damageResult += roll
    return damageResult

def abilityCheckRoll(abilityCombobox):
    resultWindow = tk.Toplevel()
    resultWindow.title("Ability Check")
    resultWindow.geometry("340x150")
    resultWindow.configure(background="Light Blue")
    # Retrieve the value from the combobox
    selectedValue = abilityCombobox.get()
    abilityCheck = int(selectedValue.split(' ')[-1][1:-1])

    abilityCheckResult = 0
    for _ in range(1):
        roll = random.randint(1, 20)
        abilityCheckResult = roll + abilityCheck

    # Create a label to display the ability check result
    resultLabel = tk.Label(resultWindow, background="Light Blue", text=f"The Ability Check Result is: \n{abilityCheckResult}", width=25, height=5, font=('arial', 18))
    resultLabel.grid(row=1, column=1, padx=1, pady=5)
    resultLabel.config(anchor=tk.CENTER)

    resultWindow.mainloop()

def abilitySavesRoll(abilitiesSaveCombobox
                     ):
    resultWindow = tk.Toplevel()
    resultWindow.title("Ability Save Check")
    resultWindow.geometry("340x150")
    resultWindow.configure(background="Light Green")
    # Retrieve the value from the combobox
    selectedValue = abilitiesSaveCombobox.get()
    abilitySaves = int(selectedValue.split(' ')[-1])

    abilitySavesResult = 0
    for _ in range(1):
        roll = random.randint(1, 20)
        abilitySavesResult = roll + abilitySaves

    # Create a label to display the ability check result
    resultLabel = tk.Label(resultWindow, background="Light Green", text=f"The Ability Save Result is: \n{abilitySavesResult}", width=25, height=5, font=('arial', 18))
    resultLabel.grid(row=1, column=1, padx=1, pady=5)
    resultLabel.config(anchor=tk.CENTER)

    resultWindow.mainloop()

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