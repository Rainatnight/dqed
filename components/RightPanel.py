import tkinter as tk
from tkinter import ttk

class RightPanel(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="lightgreen")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        top_frame = tk.Frame(self, bg="lightgreen")
        top_frame.pack(side="top", fill="x", pady=10)
        
        right_label = tk.Label(top_frame, text="Текст", font=("Arial", 14), bg="lightgreen")
        right_label.pack(side="left", padx=10)
        
        button = ttk.Button(top_frame, text="Редактор", command=lambda: controller.show_frame("Editor"))
        button.pack(side="right", padx=10)