from tkinter import *
import pytube
from pytube import YouTube

window = Tk()
window.geometry('500x400')
window.resizable()
window.title('YouTube Downloader')

heading = Label(window,text='YouTube Downloader!!',font='arial 20 bold').pack(pady=20)

Label(window,text='Put your link to download.',font='arial 15 bold').pack()

link = StringVar()

Entry(window,textvariable=link,width='50').place(x=20,y=120)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    #window2 = Tk()
    #window2.geometry('200x150')
    #Label(window2,text='Downloaded').pack()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

Button(window,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

window.mainloop()
