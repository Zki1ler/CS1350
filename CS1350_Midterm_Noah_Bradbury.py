

#Problem 1: Course Gradebook

from sys import audit


class Gradebook:
    def __init__(self):
        self.Grades = {}
    
    def add_score(self, student, assignment, score):
        self.Grades.setdefault(student, {})[assignment] = score
    
    def student_average(self, student):
        scores = self.Grades.get(student, {}).values()
        return sum(scores) / len(scores) if scores else None
    
    def assignment_average(self, assignment):
        assignment_scores = [inner[assignment] for inner in self.Grades.values() if assignment in inner]
        return sum(assignment_scores) / len(assignment_scores) if assignment_scores else None
    
    def top_students(self, n):
        top_dog = sorted(self.Grades, key=self.student_average, reverse=True)
        return top_dog[:n]
    
    def missing(self, assignment):
        return sorted(student for student, inner in self.Grades.items() if assignment not in inner)


gb = Gradebook()
gb.add_score("Alice", "hw1", 90)
gb.add_score("Alice", "hw2", 80)
gb.add_score("Bob", "hw1", 70)
gb.add_score("Bob", "hw2", 60)
gb.add_score("Carol", "hw1", 100)
gb.add_score("Bob", "hw2", 75) # overwrite
print(gb.student_average("Alice")) # 85.0
print(gb.student_average("Bob")) # 72.5
print(gb.student_average("Zed")) # None
print(gb.assignment_average("hw1")) # 86.66666666666667
print(gb.assignment_average("hw9")) # None
print(gb.top_students(2)) # ['Carol', 'Alice']
print(gb.missing("hw2")) # ['Zed']


#Problem 2: Access Control with Sets

class Door:
    def __init__(self, name):
        self.name = name
        self.keycards = set()

    def grant(self, card_id):
        self.keycards.add(card_id)

    def revoke(self, card_id):
        self.keycards.discard(card_id)

    def can_open(self, card_id):
        return card_id in self.keycards


def master_cards(doors):
    if not doors:
        return set()
    result = set(doors[0].keycards)
    for door in doors[1:]:
        result &= door.keycards
    return result


def single_door_cards(doors):
    the_count = {}
    for door in doors:
        for keycard in door.keycards:
            the_count[keycard] = the_count.get(keycard, 0) + 1
    return {keycard for keycard, n in the_count.items() if n == 1}


def unused_cards(all_cards, doors):
    used = set().union(*(door.keycards for door in doors))
    return all_cards - used


def audit(doors):
    for door in doors:
        print(f"{door.name}: {len(door.keycards)} cards")
    print(f"Master cards: {master_cards(doors)}")

lobby = Door("Lobby")
for c in [101, 102, 103, 104]:
    lobby.grant(c)
lab = Door("Lab")
for c in [101, 103, 105]:
    lab.grant(c)
server = Door("Server Room")
for c in [101, 105]:
    server.grant(c)
lab.revoke(105)
lab.revoke(999) # no error
print(lab.can_open(103), lab.can_open(105)) # True False
doors = [lobby, lab, server]
print(master_cards(doors)) # {101}
print(single_door_cards(doors)) # {102, 104}
print(unused_cards({101, 102, 105, 200}, doors)) # {200}
audit(doors)
# Lobby: 4 cards
# Lab: 2 cards
# Server Room: 2 cards
# Master cards: {101}



# Problem 4: shipping
from abc import ABC, abstractmethod

class Shipment(ABC):
    def __init__(self, tracking_id, weight_kg):
        Shipment.validate_weight(weight_kg)
        self.tracking_id = tracking_id
        self.weight_kg = weight_kg
    @abstractmethod
    def cost(self):
        pass
    def label(self):
        return f"{self.tracking_id} ({self.weight_kg} kg): ${self.cost():.2f}"
    @staticmethod
    def validate_weight(weight_kg):
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")

class StandardShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00):
        super().__init__(tracking_id, weight_kg)
        self.rate_per_kg = rate_per_kg
    def cost(self):
        return self.weight_kg * self.rate_per_kg

class ExpressShipment(StandardShipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00, surcharge=10.00):
        super().__init__(tracking_id, weight_kg, rate_per_kg)
        self.surcharge = surcharge
    def cost(self):
        return super().cost() + self.surcharge

class InternationalShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, country, customs_pct=0.15):
        super().__init__(tracking_id, weight_kg)
        self.country = country
        self.customs_pct = customs_pct
    def cost(self):
        return self.weight_kg * 5.00 * (1 + self.customs_pct)
def manifest(shipments):
    total = 0
    for s in shipments:
        print(s.label())
        total += s.cost()
    print(f"Total: ${total:.2f}")
    return total


shipments = [
StandardShipment("S100", 4.0),
ExpressShipment("E200", 2.5),
InternationalShipment("I300", 3.0, country="Canada"),
]
total = manifest(shipments)
# S100 (4.0 kg): $8.00
# E200 (2.5 kg): $15.00
# I300 (3.0 kg): $17.25
# Total: $40.25
try:
    Shipment.validate_weight(-1)
except ValueError as e:
    print("Caught:", e)
# Caught: Weight must be positive