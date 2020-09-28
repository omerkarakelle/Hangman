from tkinter import *
from tkinter import messagebox
import mySqlModule as sql

root = Tk()
root.title("Sql Edit")
def submit(word,df):
    global addDef,addWord
    addDef.delete(0,END)
    addWord.delete(0,END)
    try:
        sql.addWord(word.lower(),df)
        messagebox.showinfo("SUCCESSFUL", "Your data successfully added to database.")
    except:
        messagebox.showwarning("FAIL","An unexpected situation occured. Try again.")

addWord = Entry(root, width =30)
addWord.grid(row = 0, column = 1, padx = 20, pady = 10)

addDef = Entry(root, width =30)
addDef.grid(row = 1, column = 1, padx = 20, pady = 10)

lblAdd = Label(root, text = "Word you want to add to database: ")
lblAdd.grid(row = 0, column = 0,padx = 5)
lblAdd2 = Label(root, text = "Definition of the word: ")
lblAdd2.grid(row = 1, column = 0,padx = 5)


btn = Button(root, text="SUBMIT", command = lambda : submit(addWord.get(),addDef.get()),width = 50,pady = 20)
btn.grid(row = 2, column = 0,columnspan= 2, padx = 20, pady = 10)

root.mainloop()
