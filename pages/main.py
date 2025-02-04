import tkinter as tk


from components.LeftPanel import LeftPanel
from components.RightPanel import RightPanel

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)
        
        self.right_panel = RightPanel(self)
        self.right_panel.grid(row=0, column=1, sticky="nsew")

        self.left_panel = LeftPanel(self, self.right_panel)
        self.left_panel.grid(row=0, column=0, sticky="nsew")
