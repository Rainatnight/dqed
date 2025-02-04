import json
import os
import shutil

from components.inputs.TextInput import TextInput
from components.inputs.TextArea import TextArea
from components.inputs.ImageInput import ImageInput  # Assuming ImageInput exists

def save_inputs_to_json(inputs, directory="data", img_directory="imgs"):
    """Сохраняет данные в формате JSON с корректными полями, включая путь к изображению."""

    if not inputs:
        print("Нет полей для сохранения!")
        return

    data = {}
    filename = "untitled"
    image_path = None  # Initialize the image path

    for i, input_component in enumerate(inputs):
        # Check if the component is an ImageInput
        if isinstance(input_component, ImageInput):
            # Assuming get_image_path() returns the image file path
            image_path = input_component.image_path  # You will need to set the image_path in ImageInput
            if image_path:
                # Ensure the image is copied to the 'imgs' folder
                img_filename = os.path.basename(image_path)
                img_dest = os.path.join(img_directory, img_filename)
                os.makedirs(img_directory, exist_ok=True)
                # Copy the image to the imgs folder
                shutil.copy(image_path, img_dest)  # Copy the image to the destination folder
                data["image"] = img_dest  # Save the image path in the JSON
            continue  # Skip this component, as it's not text-based

        # For text-based components like TextInput or TextArea
        text = input_component.get_text().strip()

        if i == 0:  # Первый компонент — это заголовок
            data["title"] = text
            filename = text or "untitled"
        else:
            key = "textarea" if isinstance(input_component, TextArea) else "text"
            data[key] = text

    # Очищаем имя файла
    filename = "".join(c if c.isalnum() or c in " _-" else "_" for c in filename)
    filename = filename or "untitled"

    # Путь к файлу
    filepath = os.path.join(directory, f"{filename}.json")

    # Создаём папку, если её нет
    os.makedirs(directory, exist_ok=True)

    # Сохраняем данные в файл
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"✅ Данные сохранены в {filepath}")
