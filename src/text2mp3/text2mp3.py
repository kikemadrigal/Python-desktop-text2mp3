'''
audio creator
@Tipolisto.es
'''
# Otros programas son: https://ttsreader.softonic.com/?ex=DINS-635.1
# https://talk-it.softonic.com/?ex=DINS-635.1

import os
import subprocess
#https://pyttsx3.readthedocs.io/en/latest/engine.html#the-engine-factory
import pyttsx3
from tkinter import Tk, Label, Button, Text, Frame
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo






def openFile(textArea):
    print("Leyendo archivo e insertandolo en campo de texto")
    file=askopenfile(filetypes=[('Text Files','*.txt'),('Word Files','*.docx'),('Pdf Files','*.pdf')])
    # if file is not None:
    if file is None:
        print("No se obtuvo el archivo a convertir")
        showinfo("Error","No se obtuvo el archivo")
    else:
        print(file.name)
        string = open(file.name, "r", encoding="utf_8")
        text=string.read()
        textArea.insert('1.0', text)
        #showinfo("Done","File successfully converted.")



def createWindow():
    print("creando ventana")
    window= Tk()
    window.title("Tipolisto-text2MP3")
    window.geometry("895x600")
    frame = Frame(window)
    frame.grid(row=3,column=4)
    #window.iconbitmap("data\icon.ico")
    lbl=Label(window, text="Paste the text")
    lbl.grid(row=0,column=0,columnspan=4)
    #textArea=Text(window, bg='white', fg='black', bd=5, font=('consolas', 15, 'bold'), width=70, height=20)
    textArea=Text(window, bg='white', fg='black', bd=5, font=('Helvetica', 15, 'bold'), width=70, height=20)
    textArea.grid(row=1,column=0,columnspan=4)

    button=Button(window,text="Convert to mp3 with sound", width=30, command=lambda:convertToMP3(textArea, True))
    button.grid(row=2,column=0)

    button=Button(window,text="Convert to mp3 without sound", width=30, command=lambda:convertToMP3(textArea, False))
    button.grid(row=2,column=1)

    buttonPlaySound=Button(window,text="Play mp3", width=30, command=play_music)
    buttonPlaySound.grid(row=2,column=2)

    buttonPasteFromFile=Button(window,text="Paste from file", width=30, command=lambda:openFile(textArea))
    buttonPasteFromFile.grid(row=2,column=3)


    window.mainloop()
    #window.quit()




def convertToMP3(textArea, sound):
    if sound:
        print("Convirtiendo a MP3 hablando Helena ")
    else:
        print("Convirtiendo a MP3 sin hablar")
    text=textArea.get("1.0",'end-1c')
    if len(text)!=0:
        narrador=pyttsx3.init()
        #para ver los tipos de voz instalados ejecutar el comando
        voice_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
        #voide_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        narrador.setProperty('voice', voice_id)
        narrador.setProperty('rate', 140) #1 muy despacio, 150 normal , 300 rápido
        #string = open("archivo.txt", "r", encoding="utf_8")
        #text=string.read()
        
        ##os.system("cls")
        #print("****************************")
        print("valor de text:"+text)
        if sound:
            narrador.say(text)
        narrador.save_to_file(text, 'text.mp3')
        #narrador.say("OK")
        narrador.runAndWait()
        print('\n',"La lectura termino")
 


def play_music():
    #os.system('copy text.mp3 vlc')
    #os.system('start /wait vlc\vlc-portable.exe text.mp3')
    cmd="start /wait vlc\vlc-portable.exe text.mp3"
    #cmd=['start','/wait','vlc\\vlc-portable.exe','text.mp3']
    pl = subprocess.Popen(cmd, shell=True)  # returns the exit code in unix
    pl.wait()
    if pl.returncode==0:
        print('success')
    else:
        print("failure")



def convert():
    createWindow()


convert()