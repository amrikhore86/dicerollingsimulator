import numpy
import random
from tkinter import *
from PIL import Image,ImageTk
import os

filedir = os.path.dirname(__file__)
assetsfolder = os.path.join(filedir, 'Dice')

def roll():
    global pilimage, dice_pic, labelphoto
    chance=(1,2,3,4,5,6)
    probability=(0.05,0.15,0.3,0.3,0.15,0.05)
    result=str((random.choices(chance,probability)))
    result=result[1:-1]
    if result == "1":
        pilimage=Image.open(os.path.join(assetsfolder, 'one.png'))
        dice_pic= ImageTk.PhotoImage(pilimage)
        labelphoto= Label(root,image=dice_pic)
        labelphoto.place(x=185,y=50)
        print("1")
    if result == "2":
        pilimage=Image.open(os.path.join(assetsfolder, 'two.png'))
        dice_pic= ImageTk.PhotoImage(pilimage)
        labelphoto= Label(root,image=dice_pic)
        labelphoto.place(x=185,y=50)
        print("2")
    if result == "3":
        pilimage=Image.open(os.path.join(assetsfolder, 'three.png'))
        dice_pic= ImageTk.PhotoImage(pilimage)
        labelphoto= Label(root,image=dice_pic)
        labelphoto.place(x=185,y=50)
        print("3")
    if result == "4":
        pilimage=Image.open(os.path.join(assetsfolder, 'four.png'))
        dice_pic= ImageTk.PhotoImage(pilimage)
        labelphoto= Label(root,image=dice_pic)
        labelphoto.place(x=185,y=50)
        print("4")
    if result == "5":
        pilimage=Image.open(os.path.join(assetsfolder, 'five.png'))
        dice_pic= ImageTk.PhotoImage(pilimage)
        labelphoto= Label(root,image=dice_pic)
        labelphoto.place(x=185,y=50)
        print("5")
    if result == "6":
        pilimage=Image.open(os.path.join(assetsfolder, 'six.png'))
        dice_pic= ImageTk.PhotoImage(pilimage)
        labelphoto= Label(root,image=dice_pic)
        labelphoto.place(x=185,y=50)
        print("6")
    
root=Tk()
root.geometry("640x640")
root.title("Dice Rolling Simulator")
root.iconbitmap(root,(os.path.join(assetsfolder, 'icon.ico')))
roll_button=Button(root,text="Roll",font=('Arial',16,('bold')),height=2,width=10,command=roll)
roll_button.place(x=240,y=520)
root.mainloop()

