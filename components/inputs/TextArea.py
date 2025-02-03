import tkinter as tk

class TextArea(tk.Frame):
    def __init__(self, parent, label, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # Заголовок для ввода текста
        self.label = tk.Label(self, text=label, font=("Arial", 14), bg=self["bg"])
        self.label.pack(anchor="w", pady=(5, 0))

        # Поле для ввода многострочного текста (аналог textarea)
        self.text_area = tk.Text(self, font=("Arial", 14), width=40, height=5, wrap="word", 
                                 bd=0, highlightthickness=0)
        self.text_area.pack(padx=10, pady=10, fill="both", expand=True)

    def get_text(self):
        """Возвращает введённый текст"""
        return self.text_area.get("1.0", tk.END).strip()

    def set_text(self, text):
        """Устанавливает текст в поле ввода"""
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", text)
