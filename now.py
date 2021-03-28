from tkinter import *

root = Tk()
root.title("Now Music Player")
root.geometry("640x480")

root.resizable(False, False)

def change():
    a = Toplevel(root)
    a.title('Set Playlist Name')
    a.geometry('640x480')
    txt = Text(a)
    txt.pack()

bt = Button(root, padx=10, pady=5, text='Make Playlist', command=change)
bt.pack()

root.mainloop()