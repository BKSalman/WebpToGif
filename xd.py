import tkinter as tk
from tkinter import  filedialog, Text
from tkinter.constants import SINGLE
from TkinterDnD2 import DND_FILES, TkinterDnD
import os
from PIL import Image


imagess = []

"""def drop_image(event):
    frame.insert("end", event.data)"""

def addImage():
    imagename = filedialog.askopenfilename(initialdir="/", title = "Select an Image",filetypes=(("Images","*.webp"),("all files","*.*")))
    imagess.append(imagename)
    for image in imagess:
        label = tk.Label(frame, text=image, bg="black",fg="white")
        label.pack()

"""def clearEntryInput():
    frame.delete(0, END)"""

def toGif():
    for imaage in imagess:
        im = Image.open('{}'.format(imaage))
        head, _, _ = imaage.partition(".")
        im.info.pop('background', None)
        im.save('{}.gif'.format(head), 'gif', save_all=True)
    """imagess.clear()"""
   
root = TkinterDnD.Tk()
root.title("Salman's shitty program")
root.resizable(True,True)
canvas = tk.Canvas(root, height=700, width=700, bg="gray")
canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
"""frame.drop_target_register(DND_FILES)
frame.dnd_bind("<<Drop>>", drop_image)"""


openFile = tk.Button(root, text="Open Image", padx=10, pady=5, fg="white",bg="black", command=addImage)
openFile.pack()


convertFile = tk.Button(root, text="Convert to gif", padx=10, pady=5, fg="white",bg="black", command=toGif)
convertFile.pack()

"""clear = tk.Button(root, text="Clear", padx=10, pady=5, fg="white",bg="black", command=clearEntryInput)
clear.pack()"""

root.mainloop()