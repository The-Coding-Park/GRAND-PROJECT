# author Gunjan Paul(@gunjan_mimo)
#March 13, 2020



#importing libraries
import tkinter as tk 
class NAVBAR:
    def __init__(self,parent):
        font_size=("ubunut",18)
        navbar=tk.Menu(parent.master,font=font_size)
        parent.master.config(menu=navbar)

class COMMANDLINE:
    def  __init__(self,master):
        master.title("Untitled - COMMANDLINE Editor")
        master.geometry("1200x700")
        #fontsize
        font_size=("ubunut",14)
        # text area 
        self.master=master
        self.textinputArea=tk.Text(master,font=font_size)
        self.yScrollBar=tk.Scrollbar(master, command=self.textinputArea.yview)
        self.textinputArea.configure(yscrollcommand=self.yScrollBar.set)
        self.textinputArea.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        self.yScrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.navbar=NAVBAR(self)
        
        



if __name__ == "__main__":
    master = tk.Tk()
    pt=COMMANDLINE(master)
    master.mainloop()