import os
import tkinter as tk
from tkinter import ttk
from components.inputs.TextInput import TextInput
from components.inputs.TextArea import TextArea
from components.inputs.ImageInput import ImageInput  
from functions.savefiles import save_inputs_to_json

from styles.vars import bgcolorSecondary

class Editor(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg=bgcolorSecondary)

        self.inputs = []  # List of all input fields

        # Top container for header and "Home" button
        header_frame = tk.Frame(self, bg=bgcolorSecondary)
        header_frame.pack(fill="x", padx=20, pady=10)

        button = ttk.Button(
            header_frame, text="Главная",
            command=lambda: controller.show_frame("MainPage")
        )
        button.pack(side="left")

        label = tk.Label(header_frame, text="Редактор", font=("Arial", 24), bg=bgcolorSecondary)
        label.pack(side="left", padx=10)

        # Scrollable container
        scroll_frame = tk.Frame(self, bg=bgcolorSecondary)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.canvas = tk.Canvas(scroll_frame, bg=bgcolorSecondary)
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=self.canvas.yview)
        self.input_container = tk.Frame(self.canvas, bg=bgcolorSecondary)

        self.input_container.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.window_frame = self.canvas.create_window((0, 0), window=self.input_container, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Buttons for adding fields and saving
        add_button = ttk.Button(self, text="Добавить поле", command=self.show_add_menu)
        add_button.pack(pady=10)

        save_button = ttk.Button(self, text="Сохранить", command=lambda: self.save_and_go_to_main())
        save_button.pack(pady=10)

        # Create 'data/' folder if it doesn't exist
        os.makedirs("data", exist_ok=True)
        
    def clear_inputs(self):
        """Удаляет все виджеты из контейнера ввода и очищает список inputs."""
        for widget in self.input_container.winfo_children():
            widget.destroy()
        self.inputs.clear()     

    def save_and_go_to_main(self):
        """Saves inputs, clears the frame, and switches to the MainPage."""
        save_inputs_to_json(self.inputs)  # Сохранение данных в JSON
        self.clear_inputs()  # Очистка фрейма
        self.controller.show_frame("MainPage") 

    def show_add_menu(self):
        """Creates the input type selection menu."""
        self.menu = tk.Toplevel(self)
        self.menu.title("Выберите тип ввода")
        self.menu.geometry("300x200")  # Adjusted height to fit the image option
        self.menu.config(bg=bgcolorSecondary)

        tk.Label(self.menu, text="Выберите тип поля:", font=("Arial", 14), bg=bgcolorSecondary).pack(pady=10)

        # Add buttons for different input types
        btn_text_input = ttk.Button(self.menu, text="Однострочное поле", command=lambda: self.add_input("text"))
        btn_text_input.pack(pady=5)

        btn_text_area = ttk.Button(self.menu, text="Многострочное поле", command=lambda: self.add_input("textarea"))
        btn_text_area.pack(pady=5)

        btn_image_input = ttk.Button(self.menu, text="Изображение", command=self.add_image_input)
        btn_image_input.pack(pady=5)

    def add_input(self, input_type):
        """Adds the chosen input field and updates scroll area."""
        if input_type == "text":
            input_component = TextInput(self.input_container, "Заголовок:", bg=bgcolorSecondary)
        else:
            input_component = TextArea(self.input_container, "Текст:", bg=bgcolorSecondary)

        input_component.pack(pady=10, fill="x")
        self.inputs.append(input_component)  # Save reference to the input

        self.input_container.update_idletasks()
        self.menu.destroy()

    def add_image_input(self):
        """Adds an image input field to the editor."""
        image_input_component = ImageInput(self.input_container, "Изображение:", bg=bgcolorSecondary)
        image_input_component.pack(pady=10, fill="x")
        self.inputs.append(image_input_component)  # Save reference to the image input

        self.input_container.update_idletasks()
        self.menu.destroy()
