import json
import os

from components.inputs.TextInput import TextInput

def save_inputs_to_json(inputs, directory="data"):
    """Сохраняет данные в формате JSON с полями и текстом."""
    if not inputs:
        print("Нет полей для сохранения!")
        return

    data = {}

    for i, input_component in enumerate(inputs, 1):
        text = input_component.get_text()
        data[f"Поле {i}"] = text

    # Получаем название первого поля (если оно есть)
    first_text_input = next((inp for inp in inputs if isinstance(inp, TextInput)), None)
    filename = first_text_input.get_text().strip() if first_text_input else "untitled"

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
