from tkinter import *
from datetime import date

t = str(date.today())
making_code = ""
code_arret = ""

for i in range(len(t)):
    if t[i] != "-":
        making_code += t[i]

for j in range(0, 8, 2):
    code_arret += making_code[j]

def disable_event():
    pass

def get_code():
    code_given = zone_texte.get()
    if code_given == code_arret:
        screen.destroy()
    else:
        label = Label(screen, text="ERREUR MON AMI ! REESSAYE")
        label.pack()
        screen.after(2000,lambda:label.destroy())

screen = Tk()
screen.geometry(f"{screen.winfo_screenwidth()}x{screen.winfo_screenheight()}")
# screen.eval('tk::PlaceWindow . center')
screen.resizable(False, False)
screen.attributes("-topmost", True)

texte = Label(screen, text="code d'arrêt")
zone_texte = Entry(screen, show="*", width=4)
zone_texte.focus()
submit = Button(screen, text="submit", command=get_code)


texte.pack()
zone_texte.pack()
submit.pack()

screen.overrideredirect(True)

screen.bind('<Return>',lambda event:get_code())

screen.protocol("WM_DELETE_WINDOW", disable_event)
screen.mainloop()