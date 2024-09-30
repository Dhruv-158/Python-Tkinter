from tkinter import *
import pygame

def play():
    pygame.mixer.music.load("./Audio/Rest Songs/Maan Chali By KK.mp3")
    pygame.mixer.music.play(loops=0)
    
def stop():
    pygame.mixer.music.stop()

root = Tk()
root.title("MusicApp")

pygame.mixer.init()

my_btn = Button(root,text = "Paly Song",command=play,font =("Helvetica",32)  )
my_btn.pack(pady=20)

stp_btn = Button(root,text = "Stop",command=stop,font =("Helvetica",32)  )
stp_btn.pack(pady=20)

root.mainloop()