#Розробіть систему для управління адресною книгою.

from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)


""" валідацію номера телефону (має бути перевірка на 10 цифр) """
class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
        super().__init__(phone)
        if not self.validate():
            raise ValueError

    def validate (self) -> bool:
         return bool(re.fullmatch(r'\d{10}', self.phone))
         

"""Реалізовано зберігання об'єкта Name в окремому атрибуті.
Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - 
edit_phone/пошуку об'єктів Phone - find_phone.
"""
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return "Phone removed."
        return "Phone not found."

    def edit_phone(self, old_phone: str, new_phone: str):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return "Phone updated."
        return "Phone not found."

    def find_phone(self, phone: str) -> str:
        for p in self.phones:
            if p.value == phone:
                return p.value
        return "Phone not found."


class AddressBook(UserDict):
    def add_record (self, record : Record):
        self.data[record.name.value] = record #,  додає запис до self.data.
    
    def find(self, name : str): #,  знаходить запис за ім'ям.
        return self.data.get(name, "Record not found.")

    def delete(self, name : str): # видаляє запис за ім'ям.
        if name in self.data:
            del self.data[name]
            return "Record deleted."
        return "Record not found."



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")