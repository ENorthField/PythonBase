from tkinter import *

root = Tk()
root.title("Login Frame")
root.geometry("400x400")
ImaY = PhotoImage(file="Y2.png")
labFirst = Label(root, image=ImaY)
labFirst.pack()
b = "*"


#####
def show():
    global b
    b = None
    print(b)


####
fra = Frame(root)
fra.pack()
lab = Label(fra, text="Account", font=("Aldrich", 12), width=20)
lab.pack(side=LEFT)
ent = Entry(fra)
ent.pack(side=LEFT)
butA = Button(fra, text="Clean", font=("Aldrich", 8))
butA.pack(side=RIGHT)
# 密码栏
fra2 = Frame(root)
fra2.pack()
lab2 = Label(fra2, text="Password", font=("Aldrich", 12), width=20)
lab2.pack(side=LEFT)
ent2 = Entry(fra2, show=b)
ent2.pack(side=LEFT)
but3 = Button(fra2, text="Show", font=("Aldrich", 8), command=show)
but3.pack(side=RIGHT)
#####
fra3 = Frame(root)
fra3.pack()
but = Button(fra3, text="Login", font=("Aldrich", 12))
but.pack(side=LEFT)
but2 = Button(fra3, text="Register", font=("Aldrich", 12))
but2.pack(side=RIGHT, padx=25)

root.mainloop()
