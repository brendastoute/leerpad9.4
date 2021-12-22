import yaml, os, json

import tkinter as tk
window = tk.Tk()
window.geometry("250x250")
window["background"] = "yellow"


def refresh():
    try:
        with open("key.yml", "r") as file:
            content = yaml.load(file, Loader=yaml.FullLoader)
            return content["IDs"]

    except:
        return "Err: could not Load key.yaml"

check  = True

def listreg():
    global registration,check
    if check :
        registration = tk.Label(text= refresh())
        registration.pack(ipady=5,ipadx=5)
        check = False
    else: 
        None
    


def destroyreg():
    global check
    check = True
    registration.destroy()

but = tk.Button(text="refresh",command=listreg)
but.pack(ipadx=5,ipady=5)
destroy = tk.Button(text="destroy reg",command =destroyreg)
destroy.pack(ipadx=5,ipady=5)

window.mainloop()