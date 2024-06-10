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
    root.after(20,destroy)
    root.mainloop()
    return d
                
def loading_multi(str):
    def destroy():
        try: 
            global d
            try:
                d_intial=pd.concat((pd.read_csv(f) for f in str), ignore_index=True)
            except KeyError or NameError or ValueError:
                root.destroy()
                wrong_csv()
            except NameError:
                root.destroy()
                wrong_csv()
            except ValueError:
                root.destroy()
        
            d=d_intial.sort_values('/timestamp', ascending=True)
            
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
    root.after(20,destroy)
    root.mainloop()
    return d

def wrong_csv():
    root=Tk()
    root.title("Wrong CSV")
    root.geometry("600x200")
    label=Label(root,
                font=("arial", 15),
                text="This Application does not support choosen CSV\nMake sure to choose newest Toka 5 CSV")
    label.pack(padx=5, pady=20)
    root.mainloop()

def connect_wifi():
    root=Tk()
    root.title("Connect to wifi")
    root.geometry("600x200")
    label=Label(root,
                font=("arial", 15),
                text="Connect to WIFI")
    label.pack(padx=5, pady=20)
    root.mainloop()

def file_upload():
    root=Tk()
    root.title("File Uploaded")
    root.geometry("600x200")
    label=Label(root,
                font=("arial", 15),
                text="File has been uploaded!")
    label.pack(padx=5, pady=20)
    root.mainloop()