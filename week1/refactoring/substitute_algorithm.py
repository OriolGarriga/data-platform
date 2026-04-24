def foundPerson(people):
    for i in range(len(people)):
        if people[i] == "Don":
            return "Don"
        if people[i] == "John":
            return "John"
        if people[i] == "Kent":
            return "Kent"
    return ""

def foundPerson(people):
    for person in people:
        if person in ["Don", "John", "Kent"]:
            return person
    return ""

def foundPerson(people):
    candidates = ["Don", "John", "Kent"]
    return people if people in candidates else ""