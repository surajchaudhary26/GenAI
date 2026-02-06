from typing import TypedDict
"""
Class person is inheriting TypedDict class 
    - TypedDict class gives hint or suggestion about data types 
    - it dosn't intrrupt while execution of code at runtime
    - if you keep your cursor on age variable in new_person object
    it will show the suggestion
    - using this debuging is easy
"""
class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
        'name':'nitish',
        'age':23
    }

print(new_person)