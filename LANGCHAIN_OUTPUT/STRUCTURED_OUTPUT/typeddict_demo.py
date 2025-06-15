from typing_extensions import TypedDict


class Person(TypedDict):
    name: str
    age: int

# Example usage
new_person: Person = {
    'name': 'Alice',
    'age': 30,
}

print(new_person)