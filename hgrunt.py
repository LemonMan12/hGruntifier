from pygame import mixer
import time
from pydub import AudioSegment as AS
from tkinter import *
from tkinter import ttk
import os
mixer.init()
sent=""

def Speak(*args):
    voicevar = voice.get()
    sent = sentence_entry.get()
    sent = sent.split()
    if os.path.isfile(f"Outputs/{voicevar}/" + ' '.join(sent) + ".wav"):
        mixer.music.load(f"Outputs/{voicevar}/" + ' '.join(sent) + ".wav")
        mixer.music.play()
        print("File already exists, playing file")
        return
    combined = AS.from_wav(f"{voicevar}/" + sent[0] + ".wav")
    for wavword in (sent[1:]):
        combined += AS.from_wav(f"{voicevar}/" + wavword + ".wav")
    combined.export(f"Outputs/{voicevar}/" + ' '.join(sent) + ".wav", format="wav")
    mixer.music.load(f"Outputs/{voicevar}/" + ' '.join(sent) + ".wav")
    mixer.music.play()
    print("Creating and playing file")
root = Tk()
root.title("hGruntifier")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


sentence = StringVar()
sentence_entry = ttk.Entry(mainframe, width=60, textvariable=sentence)
sentence_entry.grid(column=1, columnspan=4, sticky=(W, E))


voice = StringVar()

hgrunt = ttk.Radiobutton(mainframe, text="hgrunt",variable=voice, value="hgrunt")
hgrunt.grid(column=1, row=2, sticky=(W, E))

vox = ttk.Radiobutton(mainframe, text="vox", variable=voice, value="vox")
vox.grid(column=1, row=3, sticky=(W, E))


speakbutton = ttk.Button(mainframe, text="Speak", command=Speak)
speakbutton.grid(column=2, row=3, sticky=(W, E))

root.bind("<Return>",Speak)
root.mainloop()