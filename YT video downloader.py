

from tkinter import *
from pytube import YouTube

window= Tk()
window.geometry("500x300")
window.resizable(0,0)
window.title("Youtube Video Downloader")
Label(window, text="Youtube Video Downloader", font = "arial  20 bold"). pack()


link= StringVar()
Label(window, text= "Enter the link here", font= "arial 15 bold").place(x=160, y=60)
link_enter= Entry(window, width=70,  textvariable= link ).place(x= 32, y=90)


def downloader():
    url= YouTube(str(link.get()))
    video= url.streams.first()
    video.download()
Button(window, text="Download", font="arial 15 bold", bg="blue", padx = 2, command= downloader). place(x= 180, y=150)

window.mainloop()
