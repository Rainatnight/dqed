import tkinter as tk
from tkinter import ttk
from components.inputs.TextInput import TextInput
from components.inputs.TextArea import TextArea

class Editor(tk.Frame): 
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="beige")

        # Верхний контейнер для заголовка и кнопки "Главная"
        header_frame = tk.Frame(self, bg="beige")
        header_frame.pack(fill="x", padx=20, pady=10)

        # Кнопка "Главная"
        button = ttk.Button(
            header_frame, text="Главная",
            command=lambda: controller.show_frame("MainPage")
        )
        button.pack(side="left")

        # Заголовок "Редактор"
        label = tk.Label(header_frame, text="Редактор", font=("Arial", 24), bg="beige")
        label.pack(side="left", padx=10)

        # ======= Контейнер с прокруткой =======
        scroll_frame = tk.Frame(self, bg="beige")
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)

        canvas = tk.Canvas(scroll_frame, bg="beige")
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        self.input_container = tk.Frame(canvas, bg="beige")

        # Привязываем прокрутку к canvas
        self.input_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        window_frame = canvas.create_window((0, 0), window=self.input_container, anchor="nw")

        # Настройки canvas и scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Кнопка "Добавить поле"
        add_button = ttk.Button(self, text="Добавить поле", command=self.show_add_menu)
        add_button.pack(pady=10)

    def show_add_menu(self):
        """Создаёт окно выбора типа ввода."""
        self.menu = tk.Toplevel(self)
        self.menu.title("Выберите тип ввода")
        self.menu.geometry("300x150")
        self.menu.config(bg="beige")

        tk.Label(self.menu, text="Выберите тип поля:", font=("Arial", 14), bg="beige").pack(pady=10)

        btn_text_input = ttk.Button(self.menu, text="Однострочное поле", command=lambda: self.add_input("text"))
        btn_text_input.pack(pady=5)

        btn_text_area = ttk.Button(self.menu, text="Многострочное поле", command=lambda: self.add_input("textarea"))
        btn_text_area.pack(pady=5)

    def add_input(self, input_type):
        """Добавляет выбранное поле и обновляет прокрутку."""
        if input_type == "text":
            input_component = TextInput(self.input_container, "Заголовок:", bg="beige")
        else:
            input_component = TextArea(self.input_container, "Текст:", bg="beige")
        
        input_component.pack(pady=10, fill="x")

        # Обновляем область прокрутки
        self.input_container.update_idletasks()
        self.menu.destroy()
