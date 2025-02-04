import tkinter as tk
import os

class LeftPanel(tk.Frame):
    def __init__(self, parent, right_panel, data_directory="data"):
        super().__init__(parent, bg="lightblue")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.data_directory = data_directory
        self.right_panel = right_panel  # Ссылка на правый блок
        self.selected_file = None  # Храним выбранный файл

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
        for widget in self.file_list_frame.winfo_children():
            widget.destroy()

        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

        files = [f[:-5] for f in os.listdir(self.data_directory) if f.endswith(".json")]

        if not files:
            tk.Label(self.file_list_frame, text="Нет файлов", font=("Arial", 12), bg="lightblue").pack(pady=5)
        else:
            for file in files:
                bg_color = "lightblue" if file != self.selected_file else "lightgreen"  # Цвет для выбранного файла
                file_label = tk.Button(
                    self.file_list_frame, text=file, font=("Arial", 12),
                    bg=bg_color, relief="flat", command=lambda f=file: self.on_file_click(f)
                )
                file_label.pack(anchor="w", pady=2, fill="x")

    def on_file_click(self, filename):
        """Вызывается при нажатии на файл."""
        self.selected_file = filename  # Обновляем выбранный файл
        self.right_panel.display_selected_file(filename)
        self.refresh()  # Обновляем список файлов, чтобы изменить цвет

    def refresh(self):
        """Метод для ручного обновления списка файлов."""
        self.display_file_names()
