class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        person_instance = Person(person.get("name"), person.get("age"))
        result.append(person_instance)
        Person.people[person_instance.name] = person_instance

    for person in people:
        if person.get("wife") is not None:
            Person.people.get(person.get("name")).wife\
                = Person.people.get(person.get("wife"))
        if person.get("husband") is not None:
            Person.people.get(person.get("name")).husband\
                = Person.people.get(person.get("husband"))
    return result
