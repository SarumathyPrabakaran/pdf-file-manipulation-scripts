from utils import merge,imgTopdf,pdfToimg,split
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Pdf Tools")
        #self.geometry("300x100")
        self.resizable(False, False)

        self.selected_option = tk.IntVar()
        options = (
            ("Merge",0),
            ("Split",1),
            ("Img to PDF",2),
            ("PDF to Img",3)
        )

        self.title_label = ttk.Label(self, text = "Select what you want: ")
        self.title_label.grid(row=0,column=0, padx = 10, pady = 10, columnspan= len(options), sticky= tk.W)
        
        self.radio_buttons = []
        for i,option in enumerate(options):
            self.radio_buttons.append(ttk.Radiobutton(
                self,
                text = option[0],
                value = option[1],
                variable= self.selected_option
            ))
            self.radio_buttons[i].grid(row = 1, column = i, padx = 10, pady = 10)
        
        self.execute_button = ttk.Button(
            self,
            text = "Execute",
            command = self.execute_option
        )
        self.execute_button.grid(row = 2, column = 0, columnspan=len(self.radio_buttons), sticky= tk.EW, padx = 10, pady = 10)
    
    def execute_option(self):
        option = self.selected_option.get()
        funcs = [merge,split,imgTopdf,pdfToimg]
        code,msg = funcs[option]()

        if code:
            showinfo(
                title="Success",
                message=msg
            )
        else:
            showerror(
                title="Error",
                message=msg
            )

app = App()
app.mainloop()
