# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from tkinter import *
import os
import os.path
import requests
from youtubesearchpython import VideosSearch
import youtube_dl
from audioplayer import AudioPlayer
from pygame import mixer
import time
import pygame
import random

##########################################################
# 단축 용어 정리

# pl = 플레이리스트 (playlist)

##########################################################
mixer.init()
root = Tk()
root.title("Now Music Player")
root.geometry("640x480")
root.iconphoto(False, PhotoImage(file="nowico.ico"))
root.resizable(False, False)


def make_pl():

    a = Toplevel(root)
    a.title("Set Playlist Name")
    a.geometry("320x100")

    t = Label(a, text="아래에 플레이리스트 이름을 작성하세요.\n특수문자는 사용이 불가능합니다.")
    t.pack()
    e = Entry(a, width=10)
    e.pack()

    def btncmd():
        aa = e.get()
        if os.path.isdir("./playlist/"):
            pass
        else:
            os.mkdir("playlist/")
        with open(f"playlist/{aa}.txt", "a", encoding="UTF-8") as f:
            f.write(".")
            f.seek(0)
            f.truncate()
        a.destroy()
        c = Toplevel(root)
        c.geometry("250x70")
        tt = Label(c, text="플레이리스트 제작이 완료되었습니다.")
        tt.pack()

    b = Button(a, padx=10, pady=5, text="완료", command=btncmd)
    b.pack()


def del_pl():
    a = Toplevel(root)
    z = ""
    for currentdir, dirs, files in os.walk("playlist/"):

        for file in files:
            file = file.replace(".txt", "")
            z += file + "\n"
    pl_list = Label(a, text=f"플레이리스트 목록입니다.\n삭제할 플레이리스트 이름을 작성해주세요.\n\n{z}")
    pl_list.pack()
    e = Entry(a, width=10)
    e.pack()

    def delpl():

        aa = e.get()
        if os.path.isfile(f"playlist/{aa}.txt"):

            os.remove(f"playlist/{aa}.txt")
            c = Toplevel(root)
            c.geometry("250x70")
            tt = Label(c, text="플레이리스트 삭제가 완료되었습니다.")
            tt.pack()

        else:
            c = Toplevel(root)
            c.geometry("250x70")
            tt = Label(c, text="플레이리스트를 찾을 수 없습니다.\n오타가 있는지 확인해주세요.")
            tt.pack()

    b = Button(a, padx=10, pady=5, text="완료", command=delpl)
    b.pack()


def plays():
    a = Toplevel(root)
    z = ""
    for currentdir, dirs, files in os.walk("playlist/"):

        for file in files:
            file = file.replace(".txt", "")
            z += file + "\n"
    pl_list = Label(a, text=f"플레이리스트 목록입니다.\n재생할 플레이리스트 이름을 입력해주세요.\n\n{z}")
    pl_list.pack()
    e = Entry(a, width=10)
    e.pack()

    def playpl():

        aa = e.get()
        if os.path.isfile(f"playlist/{aa}.txt"):

            with open(f"playlist/{aa}.txt", "r") as f:
                r = f.readlines()
                ll = []

                for i in r:
                    iii = i.rstrip()
                    ll.append(iii)

                for i in ll:
                    mixer.music.load(f"./music/{i}.mp3")

                    mixer.music.play()

                    while pygame.mixer.music.get_busy():
                        time.sleep(0.01)

                    if len(ll) == 0:
                        break
                    else:
                        pass

        else:
            c = Toplevel(a)
            c.geometry("250x70")
            tt = Label(c, text="플레이리스트를 찾을 수 없습니다.\n오타가 있는지 확인해주세요.")
            tt.pack()

    b = Button(a, padx=10, pady=5, text="완료", command=playpl)
    b.pack()


def shuffle_play():
    a = Toplevel(root)
    z = ""
    for currentdir, dirs, files in os.walk("playlist/"):

        for file in files:
            file = file.replace(".txt", "")
            z += file + "\n"
    pl_list = Label(a, text=f"플레이리스트 목록입니다.\n셔플 재생할 플레이리스트 이름을 입력해주세요.\n\n{z}")
    pl_list.pack()
    e = Entry(a, width=10)
    e.pack()

    def playpl():

        aa = e.get()
        if os.path.isfile(f"playlist/{aa}.txt"):

            with open(f"playlist/{aa}.txt", "r") as f:
                r = f.readlines()
                ll = []

                for i in r:
                    iii = i.rstrip()
                    ll.append(iii)

                for i in range(5):
                    random.shuffle(ll)

                for i in ll:
                    mixer.music.load(f"./music/{i}.mp3")

                    mixer.music.play()

                    while pygame.mixer.music.get_busy():
                        time.sleep(0.01)

                    if len(ll) == 0:
                        break
                    else:
                        pass

        else:
            c = Toplevel(a)
            c.geometry("250x70")
            tt = Label(c, text="플레이리스트를 찾을 수 없습니다.\n오타가 있는지 확인해주세요.")
            tt.pack()

    b = Button(a, padx=10, pady=5, text="완료", command=playpl)
    b.pack()


def search():
    a = Toplevel(root)
    a.title("Set Playlist Name")
    a.geometry("320x250")

    t = Label(a, text="아래에 검색할 곡의 이름을 작성하세요.")
    t.pack()
    e = Entry(a, width=10)
    e.pack()

    def bncmd():
        sn = e.get()

        vs = VideosSearch(f"IU {sn}", limit=1)
        vs = vs.result()

        url = vs["result"][0]["link"]
        name = vs["result"][0]["title"]
        n = name
        name = name.replace("[MV]", " ")
        if "iu" or "IU" in vs:
            bb = Label(a, text=f"검색 결과 : \n{name} \n")
            bb.pack()

        z = ""
        for currentdir, dirs, files in os.walk("playlist/"):

            for file in files:
                file = file.replace(".txt", "")
                z += file + "\n"

        def addSongs():
            win = Toplevel(a)
            infortxt = Label(
                win, text=f"플레이리스트 목록입니다. \n곡을 추가할 플레이리스트의 이름을 작성하세요.\n\n{z}"
            )
            infortxt.pack()
            e = Entry(win, width=10)
            e.pack()

            def asdf():
                aa = e.get()
                if os.path.isfile(f"playlist/{aa}.txt"):
                    with open(f"playlist/{aa}.txt", "a", encoding="UTF-8") as f:
                        f.write(f"{sn}\n")

                    ydl_opts = {
                        "outtmpl": f"music/{sn}",
                        "postprocessors": [
                            {
                                "key": "FFmpegExtractAudio",
                                "preferredcodec": "mp3",
                                "preferredquality": "192",
                            }
                        ],
                    }

                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([url])

                    donetxt = Label(win, text="곡 추가를 완료했습니다.")
                    donetxt.pack()

            b = Button(win, padx=10, pady=5, text="완료", command=asdf)
            b.pack()

        addbtn = Button(a, padx=10, pady=5, text="곡 추가하기", command=addSongs)
        addbtn.pack()

    b = Button(a, padx=10, pady=5, text="완료", command=bncmd)
    b.pack()


def delsong():
    a = Toplevel(root)
    a.title("Delete Song")
    a.geometry("320x250")

    t = Label(a, text="아래에 삭제하고 싶은 곡이 있는 \n플레이리스트를 입력하세요.")
    t.pack()
    e = Entry(a, width=10)
    e.pack()

    def delsongs():
        sn = e.get()

        if os.path.isfile(f"playlist/{sn}.txt"):
            bb = Toplevel(a)
            bb.geometry("320x250")

            tt = Label(bb, text="아래에 삭제하고 싶은 \n곡명을 입력하세요.")
            tt.pack()
            ee = Entry(bb, width=10)
            ee.pack()

            def inputsong():
                b = ee.get()
                with open(f"playlist/{sn}.txt", "r", encoding="UTF-8") as f:
                    lines = f.readlines()
                with open(f"playlist/{sn}.txt", "w", encoding="UTF-8") as f:
                    for line in lines:
                        if line.strip("\n") != f"{b}":
                            f.write(line)

                t = Label(bb, text="곡 삭제를 완료했습니다.")
                t.pack()

            inpsns = Button(bb, padx=7, pady=3, text="완료", command=inputsong)
            inpsns.pack()

    d = Button(a, padx=7, pady=3, text="완료", command=delsongs)
    d.pack()


makepl = Button(root, padx=10, pady=5, text="플레이리스트 제작", command=make_pl)
del_pl = Button(root, padx=10, pady=5, text="플레이리스트 삭제", command=del_pl)
playsong = Button(root, padx=10, pady=5, text="재생", command=plays)
search = Button(root, padx=10, pady=5, text="곡 추가", command=search)
deletesong = Button(root, padx=10, pady=5, text="곡 삭제", command=delsong)
shuffle_song = Button(root, padx=10, pady=5, text="셔플 재생", command=shuffle_play)
makepl.pack()
del_pl.pack()
playsong.pack()
search.pack()
deletesong.pack()
shuffle_song.pack()

root.mainloop()
