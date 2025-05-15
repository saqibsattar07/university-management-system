from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @abstractmethod
    def get_info(self):
        pass
