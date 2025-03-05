import tkinter as tk
from datetime import date


def computeCode() -> str:
    """This function compute the code the user have to find"""
    return str(date.today()).replace("-", "")[::2]


code_arret = computeCode()


def disable_event():
    label = tk.Label(screen, text="TU N'ES PAS AUTORISÉ À FAIRE ÇA !")
    label.pack()
    screen.after(2000, lambda: label.destroy())


def checkGivenCode():
    given_code = text_area.get()
    if given_code == code_arret:
        screen.destroy()
    else:
        label = tk.Label(screen, text="ERREUR MON AMI ! REESSAYE")
        label.pack()
        screen.after(2000, lambda: label.destroy())


screen = tk.Tk()
screen.geometry(f"{screen.winfo_screenwidth()}x{screen.winfo_screenheight()}")
# screen.eval('tk::PlaceWindow . center')
screen.resizable(False, False)
screen.attributes("-topmost", True)

prompt = tk.Label(screen, text="code d'arrêt")
text_area = tk.Entry(screen, show="*", width=4)
text_area.focus()
submit = tk.Button(screen, text="submit", command=checkGivenCode)


prompt.place(relx=0.5, rely=0.45, anchor="center")
text_area.place(relx=0.5, rely=0.5, anchor="center")
submit.place(relx=0.5, rely=0.55, anchor="center")

screen.overrideredirect(True)

screen.bind("<Return>", lambda event: checkGivenCode())

screen.protocol("WM_DELETE_WINDOW", disable_event)
screen.mainloop()
