from tkinter import *

##########################################################
# 단축 용어 정리

# pl = 플레이리스트 (playlist)

##########################################################
root = Tk()
root.title("Now Music Player")
root.geometry("640x480")

root.resizable(False, False)

def make_pl():
    a = Toplevel(root)
    a.title('Set Playlist Name')
    a.geometry('320x100')


    t = Label(a, text = '아래에 플레이리스트 이름을 작성하세요.')
    t.pack()
    e = Entry(a, width=10)
    e.pack()
    def btncmd():
        aa = e.get()
        print(aa)
        a.destroy()
    
    b = Button(a, padx=10, pady=5, text='완료', command=btncmd)
    b.pack()
    
    

bt = Button(root, padx=10, pady=5, text='Make Playlist', command=make_pl)
bt.pack()

root.mainloop()