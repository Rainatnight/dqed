import tkinter as tk
from tkinter import ttk
from components.inputs.TextInput import TextInput 

class Editor(tk.Frame): 
    def __init__(self, parent, controller):
        """
        :param parent: Родительский контейнер, в котором размещается страница.
        :param controller: Ссылка на основной класс приложения для переключения страниц.
        """
        super().__init__(parent)
        self.controller = controller

       
        self.config(bg="beige")  
        
        button = ttk.Button(
            self, text="Главная",
            command=lambda: controller.show_frame("MainPage"),
        )
        button.pack(pady=20, padx=20, side="top") 

        # Заголовок страницы (используем tk.Label для правильной настройки фона)
        label = tk.Label(self, text="Редактор", font=("Arial", 24), bg="beige") 
        label.pack(pady=20, padx=20, side="top") 
        
        text_input_component = TextInput(self, "Заголовок:")
        text_input_component.pack(pady=20)

        print(text_input_component.get_text())  # Вывод текста, введённого в поле
        text_input_component.set_text("") 

  
      
