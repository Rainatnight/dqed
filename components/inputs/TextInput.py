import tkinter as tk

class TextInput(tk.Frame):
    def __init__(self, parent, label, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Заголовок для ввода текста
        self.label = tk.Label(self, text=label, font=("Arial", 14),bg="beige")
        self.label.pack(pady=5)

        # Поле для ввода текста
        self.text_entry = tk.Entry(self, font=("Arial", 14), width=30, highlightthickness=0)
        self.text_entry.pack(padx=10, pady=10)

    def get_text(self):
        """Возвращает введённый текст"""
        return self.text_entry.get()

    def set_text(self, text):
        """Устанавливает текст в поле ввода"""
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, text)
