# components/custom_button.py

import tkinter as tk
from tkinter import ttk

class CustomButton(ttk.Button):
    def __init__(self, parent, text, command, **kwargs):
        """
        Инициализация кастомной кнопки.
        :param parent: Родительский виджет.
        :param text: Текст кнопки.
        :param command: Функция, вызываемая при нажатии.
        :param kwargs: Дополнительные аргументы для ttk.Button.
        """
        super().__init__(parent, text=text, command=command, **kwargs)
        self.configure(style="Custom.TButton")
        # Здесь можно добавить дополнительные настройки (например, обработчики событий)
