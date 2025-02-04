import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageInput(tk.Frame):
    def __init__(self, parent, label_text, **kwargs):
        super().__init__(parent, **kwargs)
        self.label = tk.Label(self, text=label_text, font=("Arial", 12), bg=kwargs.get("bg", "beige"))
        self.label.pack(anchor="w", padx=10)

        # Placeholder for the image
        self.image_label = tk.Label(self, text="No image selected", bg=kwargs.get("bg", "beige"))
        self.image_label.pack(pady=5, padx=10)

        # Button to select image
        self.select_button = tk.Button(self, text="Выбрать изображение", command=self.select_image)
        self.select_button.pack(pady=5)

        self.image_path = None  # Path to store the selected image file

    def select_image(self):
        """Открывает диалог для выбора изображения и отображает его."""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        
        if file_path:
            self.image_path = file_path  # Save the file path
            # Load the image and display it
            image = Image.open(file_path)
            image.thumbnail((200, 200))  # Resize the image to fit
            self.img = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.img, text="")  # Update the image label
