import tkinter as tk
from tkinter import ttk



class MainPage(ttk.Frame):
    def __init__(self, parent, controller):
        """
        :param parent: Родительский контейнер, в котором размещается страница.
        :param controller: Ссылка на основной класс приложения для переключения страниц.
        """
        super().__init__(parent)
        self.controller = controller

        # Заголовок страницы
        label = ttk.Label(self, text="Это страница 1", font=("Arial", 24))
        label.pack(pady=20, padx=20)

        # Кнопка для перехода на страницу 2
        button = ttk.Button(
            self, text="Перейти на страницу 2",
            command=lambda: controller.show_frame("Editor")
        )
        button.pack()
