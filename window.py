import tkinter as tk
from tkinter import ttk

from pages.main import MainPage
from pages.editor import Editor

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("dqed")
        self.geometry("1200x800")
        self.resizable(True, True)

        # Контейнер для всех страниц (фреймов)
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Словарь для хранения страниц
        self.frames = {}

        # Создаем экземпляры страниц и размещаем их в одном контейнере
        for PageClass in (MainPage, Editor):
            page_name = PageClass.__name__  
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Показываем первую страницу по умолчанию
        self.show_frame("MainPage")

    def show_frame(self, page_name):
        """Поднимает страницу с именем page_name."""
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == '__main__':
    app = App()
    app.mainloop()

