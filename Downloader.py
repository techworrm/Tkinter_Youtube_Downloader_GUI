from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from PIL import ImageTk,Image

root = Tk()
root.configure(background='black')
#Set Title
root.title("YouTube Video Downloader")

#Set size of window
root.geometry("855x500")

#Make the Window not Resizeable
root.resizable(False, False)

#Set Labels
img=ImageTk.PhotoImage(file="logo.jpg")
headLabel       = Label(root,image=img).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root,   text="URL",                 font=("Century Gothic",15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel    = Label(root,   text="SELECT QUALITY",      font=("Century Gothic",15)).grid(row=2, column=0, padx=10, pady=10)
locLabel        = Label(root,   text="LOCATION",            font=("Century Gothic",15)).grid(row=3, column=0, padx=10, pady=10)

#Get Input
getURL = StringVar()
getLoc = StringVar()

#Set Entry
urlEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

#List box for video Quality
listbox     = Listbox(root, font=("Century Gothic",11), width = 56, height = 12, bd=3, relief=SOLID, borderwidth=1)
listbox.grid(row=2,column=1, padx=10, pady=10)

#Set Buttons
urlButton       = Button(root, text = "SEARCH",    font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1).grid(row=1, column=2, padx=10, pady=10)
browseButton    = Button(root, text = "BROWSE...",     font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1).grid(row=3, column=2, padx=10, pady=10)
downloadButton  = Button(root, text = "DOWNLOAD",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1).grid(row=4, column=1, padx=10, pady=10)
resetButton     = Button(root, text = "CLEAR ALL",  font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1).grid(row=4, column=2, padx=10, pady=10)
root.iconbitmap(r'C:\Users\Usman\Downloads\iconphot.ico')

#Set an infinite loop so window stays in view
root.mainloop()