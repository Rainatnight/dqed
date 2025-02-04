import tkinter as tk
import os

class LeftPanel(tk.Frame):
    def __init__(self, parent, data_directory="data"):
        super().__init__(parent, bg="lightblue")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.data_directory = data_directory

        # Заголовок
        self.left_label = tk.Label(self, text="Содержание", font=("Arial", 14), bg="lightblue")
        self.left_label.pack(anchor="n", padx=10, pady=10)

        # Фрейм для списка файлов
        self.file_list_frame = tk.Frame(self, bg="lightblue")
        self.file_list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Кнопка обновления
        self.refresh_button = tk.Button(self, text="🔄 Обновить", command=self.refresh, bg="lightgray")
        self.refresh_button.pack(pady=5)

        self.display_file_names()

    def display_file_names(self):
        """Очищает и обновляет список файлов."""
        # Удаляем старые виджеты
        for widget in self.file_list_frame.winfo_children():
            widget.destroy()

        # Проверяем, есть ли папка
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

        # Получаем список файлов без расширения `.json`
        files = [f[:-5] for f in os.listdir(self.data_directory) if f.endswith(".json")]

        if not files:
            tk.Label(self.file_list_frame, text="Нет файлов", font=("Arial", 12), bg="lightblue").pack(pady=5)
        else:
            for file in files:
                tk.Label(self.file_list_frame, text=file, font=("Arial", 12), bg="lightblue").pack(anchor="w", pady=2)

    def refresh(self):
        """Метод для ручного обновления списка файлов."""
        self.display_file_names()
