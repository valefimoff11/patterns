from dataclasses import dataclass

class Person():
    def __init__(self, name, age, height, email):
        self.name = name
        self.age = age
        self.height = height
        self.email = email

@dataclass
class Person1():
    name: str
    age: int
    height: float
    email: str

@dataclass
class Person2():
    name: str = 'Joe'
    age: int = 30
    height: float = 1.85
    email: str = 'joe@dataquest.io'

print(Person2())

person = Person2('Peter', 25, 1.85, 'joe@dataquest.io')
print(person.name)

from typing import List

@dataclass
class People():
    people: List[Person]

joe = Person('Joe', 25, 1.85, 'joe@dataquest.io')
mary = Person('Mary', 43, 1.67, 'mary@dataquest.io')

print(People([joe, mary]))

@dataclass
class Person3():
    name: str = 'Joe'
    age: int = 30
    height: float = 1.85
    email: str = 'joe@dataquest.io'

print(Person3() == Person3())