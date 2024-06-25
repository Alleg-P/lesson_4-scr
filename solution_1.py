# Задание 1: Школа музыки (Наследование от абстрактного класса)

from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(Instrument):
    def play(self):
        print("Strumming the guitar strings.")

class Piano(Instrument):
    def play(self):
        print("Playing a melody on the piano.")

class Flute(Instrument):
    def play(self):
        print("Blowing into the flute.")

if __name__ == "__main__":
    instruments = [Guitar(), Piano(), Flute()]
    for instrument in instruments:
        instrument.play()
