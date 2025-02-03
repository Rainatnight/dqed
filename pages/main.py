import tkinter as tk
from tkinter import ttk

class MainPage(tk.Frame):  # Используем tk.Frame для главного контейнера
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Настроим сетку для главного фрейма с 2 столбцами
        self.columnconfigure(0, weight=1)  # 20% (условно)
        self.columnconfigure(1, weight=4)  # 80% (условно)
        self.rowconfigure(0, weight=1)

        # Левый столбец (20% ширины) с фоновым цветом
        left_frame = tk.Frame(self, bg="lightblue")  # Левый фрейм с фоном
        left_frame.grid(row=0, column=0, sticky="nsew")

        # Используем tk.Label для левого столбца, так как ttk.Label не поддерживает фон
        left_label = tk.Label(left_frame, text="Содержание", font=("Arial", 14), bg="lightblue")
        left_label.pack(anchor="n", padx=10, pady=10) 

        # Правый столбец (80% ширины) с фоновым цветом
        right_frame = tk.Frame(self, bg="lightgreen")  # Правый фрейм с фоном
        right_frame.grid(row=0, column=1, sticky="nsew")

        # Создадим вспомогательный фрейм для текста и кнопки в правом блоке
        top_frame = tk.Frame(right_frame, bg="lightgreen")
        top_frame.pack(side="top", fill="x", pady=10)

        # Используем tk.Label для правого столбца, задаем фон
        right_label = tk.Label(top_frame, text="Текст", font=("Arial", 14), bg="lightgreen")
        right_label.pack(side="left", padx=10)  # Текст слева

        # Кнопка для перехода на страницу 2 внутри правого столбца
        # button = ttk.Button(
        #     top_frame, text="To main",
        #     command=lambda: controller.show_frame("Editor")
        # )
        # button.pack(side="right", padx=10)  
