import tkinter as tk
import json
import os
from tkinter import ttk
class RightPanel(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent, bg="lightgreen")
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        add_button = ttk.Button(self, text="Редактор", command=lambda: controller.show_frame("Editor"))
        add_button.pack(side="top",pady=10)
        
        # Верхний фрейм
        self.top_frame = tk.Frame(self, bg="lightgreen")
        self.top_frame.pack(side="top", fill="x", pady=10)

        # Фрейм для отображения содержимого JSON
        self.content_frame = tk.Frame(self, bg="lightgreen")
        self.content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def display_selected_file(self, filename):
        """Обновляет текст в правом блоке при выборе файла и отображает его содержимое."""
     
        
        # Очищаем содержимое фрейма, если оно было
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Путь к файлу
        file_path = os.path.join("data", f"{filename}.json")

        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            try:
                # Открываем и парсим JSON
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                
                # Отображаем заголовок в центре сверху
                title_label = tk.Label(self.content_frame, text=data.get("title", "Без названия"), 
                                       font=("Arial", 16, "bold"), bg="lightgreen", anchor="center")
                title_label.pack(pady=10, anchor="center")

                # Отображаем содержимое textarea
                if "textarea" in data:
                    textarea_label = tk.Label(self.content_frame, text=data["textarea"], font=("Arial", 12), bg="lightgreen", anchor="w", justify="left")
                    textarea_label.pack(pady=5, anchor="w")

                # Отображаем содержимое text
                if "text" in data:
                    text_label = tk.Label(self.content_frame, text=data["text"], font=("Arial", 12), bg="lightgreen", anchor="w", justify="left")
                    text_label.pack(pady=5, anchor="w")

            except json.JSONDecodeError:
                error_label = tk.Label(self.content_frame, text="Ошибка при разборе JSON.", font=("Arial", 12), bg="lightgreen", fg="red")
                error_label.pack(pady=5)
        else:
            error_label = tk.Label(self.content_frame, text="Файл не найден.", font=("Arial", 12), bg="lightgreen", fg="red")
            error_label.pack(pady=5)
