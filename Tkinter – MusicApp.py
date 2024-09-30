from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3 # type: ignore
import tkinter.ttk as ttk
# import os

# Initialize Pygame Mixer
pygame.mixer.init()   

# Global volume variable
current_volume = 0.5
pygame.mixer.music.set_volume(current_volume)

# Open file dialog to choose a song with specified initial directory and file types
def add_song():
    song = filedialog.askopenfilename(initialdir = './Audio',title="Chooose A Song",filetypes = (("mp3 Files","*.mp3"),))
    
    #strip out the directory info and .mp3 extension from the song 
    
    song= song.replace("D:/dhruv/Python/GUI/GUIGFG/Audio/Rest Songs/", "").replace(".mp3", "")
    
    
    # add song to songbox
    
    song_box.insert(END,song)

# Add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir = './Audio',title="Chooose A Song",filetypes = (("mp3 Files","*.mp3"),))

    # Loop thru song list and replace directory info and mp3
    for song in songs:
        song= song.replace("D:/dhruv/Python/GUI/GUIGFG/Audio/Rest Songs/","").replace(".mp3", "")
        #insert into playlist
        song_box.insert(END, song)
    
    
#Play selected song
def play():
    song = song_box.get(ACTIVE)
    # song_path = os.path.join(r'D:\dhruv\Python\GUI\GUIGFG\Audio\Rest Songs', f'{song}.mp3')
    song_path = f'D:\dhruv\Python\GUI\GUIGFG\Audio\Rest Songs\{song}.mp3'
    
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)
    
# Stop playing current song

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    
# Create Global Pause Variable

global paused
paused = False

# Pause and Unpause the Current Song
def pause(is_paused):
    global paused
    paused = is_paused
    
    if paused:
        #Unpuase
        pygame.mixer.music.unpause()
        paused = False
    else:
        #Pause
        pygame.mixer.music.pause()
        paused = True
  
# Play next song in Play list

def next_song():
    #Get the Cuurrent song number
    next_one = song_box.curselection()
    # Add one to the Current song number
    next_one = next_one[0]+1
    #Grab song title from playlist
    song = song_box.get(next_one)
    # add directory structure and mp3 to song title 
    song_path = f'D:\dhruv\Python\GUI\GUIGFG\Audio\Rest Songs\{song}.mp3'
    # load and play song
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)
    
    # Clear active bar in playlist listbox
    song_box.selection_clear(0,END)
    
    # Activate new song bar
    song_box.activate(next_one)
    
    #Set Active Bar TO Next Song
    song_box.selection_set(next_one,last=None)
    
def previous_song():
     #Get the Cuurrent song number
    next_one = song_box.curselection()
    # Add one to the Current song number
    next_one = next_one[0]-1
    #Grab song title from playlist
    song = song_box.get(next_one)
    # add directory structure and mp3 to song title 
    song_path = f'D:\dhruv\Python\GUI\GUIGFG\Audio\Rest Songs\{song}.mp3'
    # load and play song
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(loops=0)
    
    # Clear active bar in playlist listbox
    song_box.selection_clear(0,END)
    
    # Activate new song bar
    song_box.activate(next_one)
    
    #Set Active Bar TO Next Song
    song_box.selection_set(next_one,last=None)
    
# Increase the volume
def volume_up():
    global current_volume
    if current_volume < 1.0:
        current_volume += 0.1
        pygame.mixer.music.set_volume(current_volume)
        volume_label.config(text=f"Volume: {current_volume:.1f}")
    

# Decrease the volume
def volume_down():
    global current_volume
    if current_volume > 0.0:
        current_volume -= 0.1
        pygame.mixer.music.set_volume(current_volume)
        volume_label.config(text=f"Volume: {current_volume:.1f}")
    
# Delete A Song    
def delete_song():
    # Delete Currently Selected song
    song_box.delete(ANCHOR)
    # Stop Music if it's playlist
    pygame.mixer.music.stop()

# Delete All Songs from Playlist
def delete_all_songs():
    # Delete All Songs 
    song_box.delete(0,END)
    # Stop Music if it's playlist
    pygame.mixer.music.stop()

root = Tk()
root.title("MusicApp")
   
# Create Playlist Frame
playlist_frame = Frame(root)
playlist_frame.pack(pady=20, padx=20)

# Create Scrollbar for Listbox
scrollbar = Scrollbar(playlist_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# Create Playlist Box
song_box = Listbox(playlist_frame, bg="black", fg="white", width=60, selectbackground="gray", selectforeground="black", yscrollcommand=scrollbar.set)
song_box.pack(side=LEFT, fill=BOTH)

# Configure Scrollbar
scrollbar.config(command=song_box.yview)

# Define Create Player Control button
back_btn_img = PhotoImage(file='./Images/back50.png')
forwad_btn_img = PhotoImage(file='./Images/forward50.png')
play_btn_img = PhotoImage(file='./Images/play50.png')
pause_btn_img = PhotoImage(file='./Images/pause50.png')
stop_btn_img = PhotoImage(file='./Images/stop50.png')
volume_up_img = PhotoImage(file='./Images/volume_up50.png')
volume_down_img = PhotoImage(file='./Images/volume_down50 .png')

# Create Player Control Frames 
contrls_frame = Frame(root)
contrls_frame.pack()

#  Create Player Control button

back_btn =     Button(contrls_frame,image=back_btn_img,borderwidth=0,command=previous_song)
forwad_btn = Button(contrls_frame,image=forwad_btn_img ,borderwidth=0,command=next_song)
play_btn = Button(contrls_frame,image=play_btn_img,borderwidth=0,command=play)  
pause_btn = Button(contrls_frame,image=pause_btn_img,borderwidth=0,command=lambda: pause(paused))
stop_btn =  Button(contrls_frame,image=stop_btn_img,borderwidth=0,command=stop)
volume_up_btn = Button(contrls_frame, image=volume_up_img, borderwidth=0, command=volume_up)
volume_down_btn = Button(contrls_frame, image=volume_down_img, borderwidth=0, command=volume_down)

back_btn.grid(row=0,column=0,padx=10,pady=10)
forwad_btn.grid(row=0,column=1,padx=10,pady=10)
play_btn.grid(row=0,column=2,padx=10,pady=10)
pause_btn.grid(row=0,column=3,padx=10,pady=10)
stop_btn.grid(row=0,column=4,padx=10,pady=10)
volume_up_btn.grid(row=0, column=6, padx=10, pady=10)
volume_down_btn.grid(row=0, column=7, padx=10, pady=10)


# Create and place volume label
volume_label = Label(root, text=f"Volume: {current_volume:.1f}",fg="red")
volume_label.pack(pady=20)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist",command=add_song)
# Add Many Songs to Playlist
add_song_menu.add_command(label="Add Many Songs To Playlist",command=add_many_songs)

# Create Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove songs",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist",command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist",command=delete_all_songs)

root.mainloop()