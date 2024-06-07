from tkinter import Tk, mainloop
from tkinter.ttk import Label
import pandas as pd

def loading(str):
    def destroy():
        try: 
            global d
            d=pd.read_csv(str)
            root.quit()
            root.destroy()
        except FileNotFoundError:
            d="rip"
            root.quit()
            root.destroy()
        
    root=Tk()
    root.title("Loading")
    root.geometry("400x200")
    label=Label(root,
                font=("arial", 15),
                text="Waiting for File to Load .....")
    label.pack(padx=10,pady=5)
    root.after(10,destroy)
    root.mainloop()
    return d
                
def loading_multi(str):
    def destroy():
        try: 
            try:
                global d
                d_intial=pd.concat((pd.read_csv(f) for f in str), ignore_index=True)
                d=d_intial.sort_values('/timestamp', ascending=True)
            except KeyError or NameError or ValueError:
                root.destroy()
                wrong_csv()
        
            root.quit()
            root.destroy()
        except FileNotFoundError:
            d="rip"
            root.quit()
            root.destroy()

    root=Tk()
    root.title("Loading")
    root.geometry("400x200")
    label=Label(root,
                font=("arial", 15),
                text="Waiting for Files to Load .....")
    label.pack(padx=10,pady=5)
    root.after(10,destroy)
    root.mainloop()
    return d

def wrong_csv():
    root=Tk()
    root.title("Wrong CSV")
    root.geometry("600x200")
    label=Label(root,
                font=("arial", 15),
                text="This Application does not support choosen CSV")
    label.pack(padx=5, pady=20)
    root.mainloop()