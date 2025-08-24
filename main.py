import tkinter as tk
import time
root=tk.Tk()
root.geometry("500x180")
root.title("Digital Clock")
root.config(bg='black')
labl=tk.Label(root,text=(""),font=("Arial Rounded MT Bold",40,'bold'),fg="cyan",bg='black')
labl.pack()
lab2=tk.Label(root,text=(""),font=("Arial",40,'bold'),fg="yellow",bg='black')
lab2.pack()
def update():
    value = time.strftime("%I:%M:%S(%p),%a")
    labl.config(text=(value))
    date=time.strftime('%d-%m-%y')
    lab2.config(text=date)
    root.after(1000,update)
update()
root.mainloop()
