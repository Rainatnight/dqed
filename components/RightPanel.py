import tkinter as tk

class RightPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="lightgreen")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Верхний фрейм
        self.top_frame = tk.Frame(self, bg="lightgreen")
        self.top_frame.pack(side="top", fill="x", pady=10)

        # Метка для отображения выбранного файла
        self.selected_file_label = tk.Label(self.top_frame, text="Выберите файл", font=("Arial", 14), bg="lightgreen")
        self.selected_file_label.pack(side="left", padx=10)

    def display_selected_file(self, filename):
        """Обновляет текст в правом блоке при выборе файла."""
        self.selected_file_label.config(text=f"Выбран: {filename}")
