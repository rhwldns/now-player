from tkinter import *

##########################################################
# 단축 용어 정리

# pl = 플레이리스트 (playlist)

##########################################################
root = Tk()
root.title("Now Music Player")
root.geometry("640x480")
root.iconphoto(False, PhotoImage(file='nowico.ico'))
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
        with open(f'{aa}.txt', 'a', encoding='UTF-8') as f:
            f.write('.')
            f.seek(0)
            f.truncate()
        a.destroy()
        c = Toplevel(root)
        c.geometry('100x50')
        tt = Label(c, text = '플레이리스트 제작이 완료되었습니다.')
    
    b = Button(a, padx=10, pady=5, text='완료', command=btncmd)
    b.pack()
    
    
def play():
    print(1)
bt = Button(root, padx=10, pady=5, text='플레이리스트 제작', command=make_pl)
b = Button(root, padx=10, pady=5, text='재생', command=play)
bt.pack()

root.mainloop()