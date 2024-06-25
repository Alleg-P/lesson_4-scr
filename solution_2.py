# Задание 2: Работа с файлами (Использование протоколов)

from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: str):
        pass

class TextFileHandler(FileHandler):
    def read(self):
        print("Текстовый файл прочитан.")

    def write(self, data: str):
        print(f"Текстовые данные {data} записаны.")

class BinaryFileHandler(FileHandler):
    def read(self):
        print("Бинарный файл прочитан.")

    def write(self, data: str):

        print(f"Бинарные данные {data} записаны.")

def save_data(handler: FileHandler, data: str):
    if not isinstance(handler, FileHandler):
        raise ValueError("handler должен быть объектом, реализующим протокол FileHandler.")
    handler.write(data)

text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

save_data(text_handler, "'Пример текста для сохранения'")

save_data(binary_handler, "'Пример бинарных данных для сохранения'")
