from tkinter import *
import os
import os.path

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
        if os.path.isdir('./playlist/'):
            pass
        else:
            os.mkdir('playlist/')
        with open(f'playlist/{aa}.txt', 'a', encoding='UTF-8') as f:
            f.write('.')
            f.seek(0)
            f.truncate()
        a.destroy()
        c = Toplevel(root)
        c.geometry('250x70')
        tt = Label(c, text = '플레이리스트 제작이 완료되었습니다.')
        tt.pack()
    
    b = Button(a, padx=10, pady=5, text='완료', command=btncmd)
    b.pack()
    
    
def play():
    print(1)

def del_pl(): 
    a = Toplevel(root)
    z = ''
    for currentdir, dirs, files in os.walk("playlist/"):
    
        for file in files :
            file = file.replace('.txt', '')
            z += file + '\n'
    pl_list = Label(a, text = f'플레이리스트 목록입니다.\n삭제할 플레이리스트 이름을 작성해주세요.\n\n{z}')
    pl_list.pack()
    e = Entry(a, width=10)
    e.pack()

    def delpl():

        aa = e.get()
        if os.path.isfile(f'playlist/{aa}.txt'):

            os.remove(f'playlist/{aa}.txt')
            c = Toplevel(root)
            c.geometry('250x70')
            tt = Label(c, text = '플레이리스트 삭제가 완료되었습니다.')
            tt.pack()

        else:
            c = Toplevel(root)
            c.geometry('250x70')
            tt = Label(c, text = '플레이리스트를 찾을 수 없습니다.\n오타가 있는지 확인해주세요.')
            tt.pack()

    b = Button(a, padx=10, pady=5, text='완료', command=delpl)
    b.pack()

            

bt = Button(root, padx=10, pady=5, text='플레이리스트 제작', command=make_pl)
del_pl = Button(root, padx=10, pady=5, text='플레이리스트 삭제', command=del_pl)
b = Button(root, padx=10, pady=5, text='재생', command=play)
bt.pack()
del_pl.pack()

root.mainloop()