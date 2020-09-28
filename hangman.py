from PIL import Image, ImageTk
from tkinter import Tk,Label,Button,Entry,LabelFrame,messagebox
from random import randint
import mySqlModule as sql
import os,sys


liste = sql.pickAWord() #using this module in order to pick a word an its definition
word = liste[0]
defin = liste[1] #definition helps player
#since it causes bad look in program, if definition is too long, it has to be seperated
if len(defin) >=60 and len(defin) <=120:
    defin= defin[:60] + "\n"+ defin[60:]
elif len(defin) >= 120:
    defin = defin[:60] + "\n" + defin[60:120] +"\n"+defin[120:]

root = Tk()
root.title("Guess The Word!")
root.iconbitmap("adamasmaca.ico")
img0 = ImageTk.PhotoImage(Image.open("oyun/adam0.png"))
img1 = ImageTk.PhotoImage(Image.open("oyun/adam1.png"))
img2 = ImageTk.PhotoImage(Image.open("oyun/adam2.png"))
img3 = ImageTk.PhotoImage(Image.open("oyun/adam3.png"))
img4 = ImageTk.PhotoImage(Image.open("oyun/adam4.png"))
img5 = ImageTk.PhotoImage(Image.open("oyun/adam5.png"))
img6 = ImageTk.PhotoImage(Image.open("oyun/adam6.png"))
imgHeart = ImageTk.PhotoImage(Image.open("heart.png"))
imgList = [img0, img1, img2, img3, img4, img5 , img6]
lbl = Label(image = img0)
lbl.grid(row = 0, column = 0, columnspan = 3, rowspan = 6)

frame = LabelFrame(root, text = "Keyboard", padx = 5 , pady = 5)
frame.grid(row = 0, column = 3, columnspan = 2, rowspan = 6, padx = 10)
number = 1

#Creating keyboard on the right side.
def createKeyboard():
    global number, button
    button = list()
    j = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if j %2 ==0: #seperating letters into 2 part in order to create 2 columns and make good look
            button.insert(j,Button(frame, text = i,padx = 5 , pady = 5, command = lambda x = i, y = j: [letter_add(number,x),buttonDisable(y)]))
            button[j].grid(row=int(j / 2), column=0)
        else:
            button.insert(j,Button(frame, text=i,padx = 5 , pady = 5,command = lambda x= i , y = j: [letter_add(number,x),buttonDisable(y)]))
            button[j].grid(row= int(j/2),column=1)
        j += 1
createKeyboard()
#making clicked button disable
def buttonDisable(y):
    button[y].grid_forget()
#making all buttons disable when game ends
def allButtonsDisable():
    for i in range(0,len(button)):
        button[i].grid_forget()

#when click a button in keyboard it inserts this letter into word.
def letter_add(imageNumber, guessLetter):
    global lbl, lbl3, lblText,number,  word, lblHealth, health
    i=0
    pointGained = 0
    for letter in word:
        if guessLetter == letter:
            lblText[i] = word[i]
            lbl3.config(text=lblText)
            pointGained += 1
        i+=1
    if pointGained ==0:
        number = imageNumber + 1
        health = health - 1
        lbl.grid_forget()
        lbl = Label(image = imgList[imageNumber])
        lbl.grid(row=0, column=0, columnspan=3, rowspan=6)
        lblHealth.destroy()
        lblHealth = Label(root, text=health, fg="red", font=("Impact", 24))
        lblHealth.grid(row=6, column=4)
    elif not "-" in lblText: #if there is not a '-' in lbltext then player wins
        win()
    if health == 0:
        lose()

#checking whether the guess word in the entry is true or not. if it is true player wins and if it is not player loses.
def guess(wordGuessed):
    global word
    if wordGuessed.lower() == word:
        win()
    else:
        lose()
def win():
    lbl3 = Label(root, text=[i for i in word], font=("Courier", 44), fg="green")
    lbl3.grid(row=7, column=0, columnspan=3)
    allButtonsDisable()
    e.grid_forget()
    guessButton.grid_forget()
    response = messagebox.askyesno("You Won!", "You Won! Would you want to play again?")
    if response == 0:
        root.quit()
    else: #checking if the response of the player is 'Yes', if it is, restarting the game
        os.execl(sys.executable, sys.executable, *sys.argv)
def lose():
    lbl = Label(image=imgList[6])
    lbl.grid(row=0, column=0, columnspan=3, rowspan=6)
    lbl3 = Label(root, text=[i for i in word], font=("Courier", 44), fg="red")
    lbl3.grid(row=7, column=0, columnspan=3)
    allButtonsDisable()
    e.grid_forget()
    guessButton.grid_forget()
    response = messagebox.askyesno("You Lost!", "You Lost! Would you want to play again?")
    if response == 0:
        root.quit()
    else: #checking if the response of the player is 'Yes', if it is, restarting the game
        os.execl(sys.executable, sys.executable, *sys.argv)
lbl2 = Label(image = imgHeart)
lbl2.grid(row = 6, column = 3)

health = 6 #health of hangman. every decrease in health draws one line.
lblHealth = Label(root, text = health, fg = "red", font=("Impact", 24))
lblHealth.grid(row = 6, column = 4)

e = Entry(root, width = 50) #for checking the player's guess
e.grid(row = 6, column = 0, padx = 5, columnspan = 3)
e.insert(0, "Enter your guess here")

#creating a label, showing one random letter in the word.
lblText = ["-" for i in word]
rndNumber = randint(0,len(word)-1)
j = 0
for i in word:
    if word[rndNumber] == i:
        lblText[j] = word[j]
    j+=1
lbl3 = Label(root, text = lblText, font=("Courier", 44))
lbl3.grid(row = 7, column = 0, columnspan = 3)


lblDef = Label(root, text = defin, font=("Courier", 16))
lblDef.grid(row = 8, column = 0, columnspan = 3,padx = 10,pady = 10)

guessButton = Button(root, text = "GUESS",padx = 20, pady = 10, bg = "#cc9900", command = lambda : guess(e.get()))
guessButton.grid(row = 6, column = 1, columnspan = 3)
e.bind("<Return>", (lambda event: guess(e.get())))

root.mainloop()