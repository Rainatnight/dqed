import tkinter as tk
import json
import os
from tkinter import ttk
from PIL import Image, ImageTk  

bgcolor = '#A6A6A6'
class RightPanel(tk.Frame):
    def __init__(self, parent, controller,left_panel):
        super().__init__(parent, bg=bgcolor)
        
        self.controller = controller
       
        self.left_panel = left_panel
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.current_filename = None

        button_frame = tk.Frame(self, bg=bgcolor)
        button_frame.pack(side="top", pady=10)
        
        add_button = ttk.Button(button_frame, text="Редактор", command=lambda: controller.show_frame("Editor"))
        add_button.pack(side="left", padx=5)
        
        self.delete_button = ttk.Button(button_frame, text="Удалить", command=self.delete_file)
        self.delete_button.pack(side="left", padx=5)
        self.delete_button.pack_forget()  # Изначально скрываем кнопку
        
        # Верхний фрейм
        self.top_frame = tk.Frame(self, bg=bgcolor)
        self.top_frame.pack(side="top", fill="x", pady=10)

        # Добавляем Canvas для прокрутки
        self.canvas = tk.Canvas(self, bg=bgcolor)
        self.canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Добавляем Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Создаем фрейм внутри канваса для отображения содержимого
        self.content_frame = tk.Frame(self.canvas, bg=bgcolor)
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Обновляем размеры канваса, когда контент меняется
        self.content_frame.bind("<Configure>", self.on_frame_configure)

        # Привязываем событие прокрутки колесика мыши
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def on_frame_configure(self, event):
        """Обновляет прокрутку, чтобы фрейм правильно отображался в канвасе"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mouse_wheel(self, event):
        """Обрабатывает прокрутку колесика мыши для канваса"""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def display_selected_file(self, filename):
        """Обновляет текст в правом блоке при выборе файла и отображает его содержимое."""
        self.current_filename = filename
        
        # Очищаем содержимое фрейма, если оно было
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Путь к файлу
        file_path = os.path.join("data", f"{filename}.json")
        self.toggle_delete_button(True if os.path.exists(file_path) else False)

        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            try:
                # Открываем и парсим JSON
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                # Пройдемся по ключам в том порядке, как они идут в JSON
                for key in data:
                    if key.startswith("title"):
                        title_label = tk.Label(self.content_frame, text=data[key], 
                                               font=("Arial", 16, "bold"), bg=bgcolor, anchor="w")
                        title_label.pack(pady=10, anchor="w")
                    elif key.startswith("textarea"):
                        textarea_label = tk.Label(self.content_frame, text=data[key], font=("Arial", 12), bg=bgcolor, anchor="w", justify="left")
                        textarea_label.pack(pady=5, anchor="w")
                    elif key.startswith("text"):
                        text_label = tk.Label(self.content_frame, text=data[key], font=("Arial", 12), bg=bgcolor, anchor="w", justify="left")
                        text_label.pack(pady=5, anchor="w")
                    elif key.startswith("image"):
                        img_path = data[key]
                        if os.path.exists(img_path):
                            # Загружаем изображение с помощью PIL
                            img = Image.open(img_path)
                            img = img.resize((700, 400), Image.Resampling.LANCZOS)

                            img_tk = ImageTk.PhotoImage(img)

                            # Создаем метку для отображения изображения
                            image_label = tk.Label(self.content_frame, image=img_tk, bg=bgcolor)
                            image_label.image = img_tk  # Сохраняем ссылку на изображение
                            image_label.pack()

            except json.JSONDecodeError:
                error_label = tk.Label(self.content_frame, text="Ошибка при разборе JSON.", font=("Arial", 12), bg=bgcolor, fg="red")
                error_label.pack(pady=5)
        else:
            error_label = tk.Label(self.content_frame, text="Файл не найден.", font=("Arial", 12), bg=bgcolor, fg="red")
            error_label.pack(pady=5)

    def toggle_delete_button(self, show):
        """Показывает или скрывает кнопку удаления"""
        if show:
            self.delete_button.pack(side="left", padx=5)
        else:
            self.delete_button.pack_forget()

    def delete_file(self):
        """Функция удаления файла"""
        if self.current_filename:
            file_path = os.path.join("data", f"{self.current_filename}.json")
            if os.path.exists(file_path):
                os.remove(file_path)
                self.toggle_delete_button(False)
                for widget in self.content_frame.winfo_children():
                    widget.destroy()
                error_label = tk.Label(self.content_frame, text="Файл удален.", font=("Arial", 12), bg=bgcolor, fg="red")
                error_label.pack(pady=5)
                self.left_panel.refresh()
