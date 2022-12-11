import random
import string
import uuid
from typing import Optional

class Person:
    name: str = 'John'
    surname: str = 'Doe'
    age: int = 30
    _username: Optional[str] = None
    # _username: str | None

    @classmethod
    def generate_username(cls, length: int = 8):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    @staticmethod
    def generate_user_name(length: int = 8):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def get_full_name(self) -> str:
        return f'{self.name} {self.surname}'

    def set_username(self, username)->None:
        if len(username) > 8:
            print('Invalid')
            return
        self._username = username

    @property
    def username(self):
        return self._username

    def __repr__(self) ->str :
        return self.get_full_name()

person = Person()
print(Person.generate_username(7))

person.id = uuid.uuid1()
person.group = 'SE-2006'
print(person.group)