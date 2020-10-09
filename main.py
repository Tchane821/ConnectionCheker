import os
import datetime as dt
from tkinter import *

def pinging():
    res = [1, 1, 1, 1]
    #google.fr
    hostname1 = "216.58.206.227"
    #Wikipedia.org
    hostname2 = "91.198.174.192"
    #Youtube.com
    hostname3 = "216.58.204.142"
    #Twitch.tv
    hostname4 = "151.101.194.167"
    reponseGo = os.system("ping -n 1 " + hostname1)
    reponseWi = os.system("ping -n 1 " + hostname2)
    reponseYo = os.system("ping -n 1 " + hostname3)
    reponseTw = os.system("ping -n 1 " + hostname4)
    if reponseGo == 0:
        res[0] = 0
    if reponseWi == 0:
        res[1] = 0
    if reponseYo == 0:
        res[2] = 0
    if reponseTw == 0:
        res[3] = 0
    return res

def update():
    reponses = pinging()
    if reponses == [0, 0, 0, 0]:
        label['text'] = 'Ping Done'
    else:
        label['text'] = 'Ping Fail'
        outerror()
    label.after(3000, update)

def outerror():
    retourErr = open("./errPing.log","a")
    retourErr.write( str(dt.datetime.now()) +" -> Erreur de connection\n")
    retourErr.close()

fene = Tk()
fene.title('Connection ?')
label = Label(fene,text='Ping in progress ...',font=('calibri', 34, 'bold'),bg ='gray',fg='black')
label.pack()
update()
fene.mainloop()