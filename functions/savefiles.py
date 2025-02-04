import json
import os

from components.inputs.TextInput import TextInput
from components.inputs.TextArea import TextArea 

def save_inputs_to_json(inputs, directory="data"):
    """Сохраняет данные в формате JSON с корректными полями."""

    if not inputs:
        print("Нет полей для сохранения!")
        return

    data = {}
    filename = "untitled"

    for i, input_component in enumerate(inputs):
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
