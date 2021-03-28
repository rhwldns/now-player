from tkinter import *

root = Tk()
root.title("Now Music Player")
root.geometry("640x480")

root.resizable(False, False)

def change():
    a = Toplevel(root)
    a.title('Set Playlist Name')
    a.geometry('320x100')
    e = Label(a, text = '아래에 플레이리스트 이름을 작성하세요.')
    e.pack()
    txt = Text(a, width=50, height=1)
    txt.pack()
    

bt = Button(root, padx=10, pady=5, text='Make Playlist', command=change)
bt.pack()

root.mainloop()