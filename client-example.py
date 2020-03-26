import http.client
from tkinter import *

window = Tk()
conn = http.client.HTTPConnection("localhost", 8080)

window.title("Random Number Generator")
window.geometry('200x150')
v = StringVar()


def clicked():

    conn.request("GET", "/random-number")
    res = conn.getresponse()
    content = res.read().decode().splitlines()
    v.set(content[-1].strip())


btn = Button(window, text="Generate", bg="sky blue", command=clicked)
btn.pack()
lbl = Label(window, textvariable=v, fg="purple")
lbl.config(font=("Courier", 44))
lbl.pack()

window.mainloop()
