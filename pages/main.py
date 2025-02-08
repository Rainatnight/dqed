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

        # Создаем left_panel сначала
        self.left_panel = LeftPanel(self, None)  # Временно передаем None

        # Создаем right_panel и передаем ссылку на left_panel
        self.right_panel = RightPanel(self, controller, self.left_panel)
        self.right_panel.grid(row=0, column=1, sticky="nsew")

        # Теперь обновляем ссылку в left_panel
        self.left_panel.right_panel = self.right_panel
        self.left_panel.grid(row=0, column=0, sticky="nsew")
