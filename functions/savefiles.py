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
    image_count = 1  # Счётчик изображений
    text_count = 1   # Счётчик полей text
    textarea_count = 1  # Счётчик полей textarea
    
    for i, input_component in enumerate(inputs):
        # Проверяем, является ли компонент изображением
        if isinstance(input_component, ImageInput):
            image_path = input_component.image_path  # Нужно получить путь к изображению в ImageInput
            if image_path:
                # Копируем изображение в папку 'imgs'
                img_filename = os.path.basename(image_path)
                img_dest = os.path.join(img_directory, img_filename)
                os.makedirs(img_directory, exist_ok=True)
                shutil.copy(image_path, img_dest)  # Копируем изображение
                data[f"image{image_count}"] = img_dest  # Сохраняем путь с порядковым номером
                image_count += 1  # Увеличиваем счётчик изображений
            continue  # Пропускаем этот компонент, так как это не текстовый

        # Для текстовых компонентов, таких как TextInput или TextArea
        text = input_component.get_text().strip()

        if i == 0:  # Первый компонент — это заголовок
            data[f"title{image_count}"] = text
            filename = text or "untitled"
        elif isinstance(input_component, TextArea):  # Если это textarea
            data[f"textarea{textarea_count}"] = text
            textarea_count += 1
        else:  # Для обычных текстовых полей
            data[f"text{text_count}"] = text
            text_count += 1

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
