from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_pay(self):
        # TODO: Make this abstract
        pass

    @abstractmethod
    def description(self):
        pass

    def pay_stub(self):
        return f"{self.name} (ID: {self.employee_id}): ${self.calculate_pay():.2f}"
    
    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        else:
            raise ValueError(f"{name} has a value error")
    
class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 24

    def description(self):
        return (f"Salaried:[{self.name}]")
    
class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        else:
            regular_pay = 40 * self.hourly_rate
            overtime_pay = (self.hours_worked - 40) * self.hourly_rate * 1.5
            return regular_pay + overtime_pay

    def description(self):
        return (f"Hourly:[{self.name}]")
class CommissionEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, sales, commission_rate):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate
        self.validate_positive(base_salary, "base_salary")
        self.validate_positive(sales, "sales")
        self.validate_positive(commission_rate, "commission_rate")
        if commission_rate > 1.0:
            raise ValueError("Commission rate must be between 1.0 and 0")

        
    def calculate_pay(self):
        return self.base_salary + (self.sales * self.commission_rate)
    def description(self):
        return (f"Commission: [{self.name}]")
class Payroll:
    def __init__(self):
        self.employees = []
   
    def add_employee(self, employee):
        self.employees.append(employee)



    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in self.employees)
    
    def print_all_stubs(self):
        for emp in self.employees:
            print(emp.pay_stub())

if __name__ == "__main__":
# Create employees
    alice = SalariedEmployee("Alice Johnson", "E001", 84000)
    bob = HourlyEmployee("Bob Smith", "E002", 25.00, 45)
    carol = CommissionEmployee("Carol Davis", "E003", 2000, 50000, 0.05)
# Test individual employees
print("Employee Descriptions:")
for emp in [alice, bob, carol]:
    print(f" {emp.description()}")

print("\nPay Stubs:")
for emp in [alice, bob, carol]:
    print(f" {emp.pay_stub()}")
# Test payroll (polymorphism!)
payroll = Payroll()
payroll.add_employee(alice)
payroll.add_employee(bob)
payroll.add_employee(carol)
print(f"\nTotal Payroll: ${payroll.total_payroll():.2f}")
# Test validation
print("\nTesting validation:")
try:
    bad = SalariedEmployee("Bad", "E999", -50000)
except ValueError as e:
    print(f" Caught: {e}")
try:
    bad = CommissionEmployee("Bad", "E999", 1000, 5000, 1.5)
except ValueError as e:
    print(f" Caught: {e}")


#Problem 2
class Song:
    total_songs = 0


    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
        Song.total_songs += 1

    def display(self):
        return f"{self.title} - {self.artist} ({self.format_duration(self.duration_seconds)})"

    @classmethod
    def from_string(cls, s):
        title, artist, duration = s.split(" | ")
        return cls(title, artist, cls.parse_duration(duration))
    @classmethod
    def get_total_songs(cls):
        return cls.total_songs
    @staticmethod
    def format_duration(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02d}"
    @staticmethod
    def parse_duration(duration_str):
        minutes, seconds = duration_str.split(":")
        return int(minutes) * 60 + int(seconds)
class Playlist:
    total_playlists = 0
    def __init__(self, name):
        Playlist.total_playlists += 1
        self.playlist_id = f"PL_{Playlist.total_playlists:03d}"
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        return sum(song.duration_seconds for song in self.songs)
    
    def display(self):
        return f"Playlist: {self.name} ({len(self.songs)} songs, {Song.format_duration(self.total_duration())})"

    
    @classmethod
    def get_total_playlists(cls):
        return cls.total_playlists

class LibraryManager:
    @staticmethod
    def create_playlist_from_strings(name, song_strings):
        playlist = Playlist(name)
        for s in song_strings:
            playlist.add_song(Song.from_string(s))
        return playlist

    @staticmethod
    def format_library_report(playlists):
        report = ["=== Library Report ==="]
        total = 0
        for pl in playlists:
            report.append(pl.display())
            for i, song in enumerate(pl.songs, start=1):
                report.append(f"  {i}. {song.display()}")
            report.append(f" Duration:{Song.format_duration(pl.total_duration())}")
            total += len(pl.songs)
        report.append(f"Total songs in library: {total}")
        report.append(f"====================")
        return "\n".join(report)

# Test your code
if __name__ == "__main__":
# Test Song creation
    s1 = Song("Bohemian Rhapsody", "Queen", 354)
    s2 = Song("Imagine", "John Lennon", 187)
    print("Individual Songs:")
    print(f" {s1.display()}")
    print(f" {s2.display()}")
# Test factory method
    s3 = Song.from_string("Hotel California | Eagles | 6:31")
    print(f" {s3.display()}")
# Test static methods
    print(f"\nFormat 245 seconds: {Song.format_duration(245)}")
    print(f"Parse '4:05': {Song.parse_duration('4:05')} seconds")
# Test Playlist
    playlist = Playlist("Classic Rock")
    playlist.add_song(s1)
    playlist.add_song(s2)
    playlist.add_song(s3)
    print(f"\n{playlist.display()}")
# Test LibraryManager
    chill_songs = [
    "Weightless | Marconi Union | 8:09",
    "Electra | Airstream | 5:51",
    "Mellomaniac | DJ Shah | 7:34"
    ]
    chill = LibraryManager.create_playlist_from_strings("Chill Vibes",
    chill_songs)
    print(f"{chill.display()}")
    # Test report
    print(f"\n{LibraryManager.format_library_report([playlist, chill])}")
    # Test counts
    print(f"Total songs created: {Song.get_total_songs()}")
    print(f"Total playlists created: {Playlist.get_total_playlists()}")


#problem 3
class GradeBook:
    def __init__(self, course_name):
        self.course_name = course_name
        self.grades = {}
# --- Display Methods ---
    def __str__(self):
        return f"GradeBook: {self.course_name} ({len(self.grades)} students)"
    
    def __repr__(self):
        return f"GradeBook('{self.course_name}')"

    
# --- Container Protocol ---
    def __len__(self):
        return len(self.grades)
    def __getitem__(self, student):
        if student not in self.grades:
            raise KeyError(student)
        return self.grades[student]
    def __setitem__(self, student, grade):
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades[student] = grade
    def __contains__(self, student):
        return student in self.grades
    
    def __iter__(self):
        return iter(self.grades)
    
    def __bool__(self):
        return len(self.grades) > 0
# --- Property ---
    @property
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
 #Operators ---
    def __add__(self, other):
        if not isinstance(other, GradeBook):
            return NotImplemented
        result = GradeBook(f"{self.course_name} + {other.course_name}")
        for student in self:
            result[student] = self[student]
        for student in other:
            if student not in result or other[student] > result[student]:
                result[student] = other[student]
        return result
    def __iadd__(self, other):
        if not isinstance(other, GradeBook):
            return NotImplemented
        for student in other:
            if student not in self or other[student] > self[student]:
                self[student] = other[student]
        return self
    def __mul__(self, factor):
        if not isinstance(factor, (int, float)):
            return NotImplemented
        result = GradeBook(f"{self.course_name} (curved)")
        for student in self:
            result[student] = min(100, round(self[student] * factor, 2))
        return result
 
# --- Comparison Operators (compare by average) ---
    def __eq__(self, other):
        if not isinstance(other, GradeBook):
            return NotImplemented
        return abs(self.average - other.average) < 0.01
    def __lt__(self, other):
        if not isinstance(other, GradeBook):
            return NotImplemented
        return self.average < other.average
    def __le__(self, other):
        if not isinstance(other, GradeBook):
            return NotImplemented
        return self.average <= other.average


if __name__ == "__main__":
# === Part A: Display and Container ===
    print("=== Part A: Container Protocol ===")
cs101 = GradeBook("CS 101")
# __setitem__
cs101["Alice"] = 92
cs101["Bob"] = 78
cs101["Carol"] = 88
cs101["David"] = 95
# __str__ and __repr__
print(cs101) # GradeBook: CS 101 (4 students)
print(repr(cs101)) # GradeBook('CS 101')
# __getitem__
print(f"Alice's grade: {cs101['Alice']}") # 92
# __contains__
print(f"Bob enrolled? {'Bob' in cs101}") # True
print(f"Eve enrolled? {'Eve' in cs101}") # False
# __len__
print(f"Class size: {len(cs101)}") # 4
# __iter__
print("Students:")
for student in cs101:
    print(f" {student}: {cs101[student]}")
# __bool__
empty = GradeBook("Empty")
print(f"cs101 has students? {bool(cs101)}") # True
print(f"empty has students? {bool(empty)}") # False
# Validation
print("\nValidation test:")
try:
    cs101["Eve"] = 150
except ValueError as e:
    print(f" Caught: {e}")
# === Part B: Arithmetic ===
print("\n=== Part B: Arithmetic ===")
math201 = GradeBook("Math 201")
math201["Alice"] = 85
math201["Bob"] = 90
math201["Eve"] = 76
# __add__ — merge (keep higher grade)
combined = cs101 + math201
print(f"\n{combined}")
print("Merged grades:")
for student in combined:
    print(f" {student}: {combined[student]}")
# Alice: 92 (higher of 92, 85)
# Bob: 90 (higher of 78, 90)
# Carol: 88 (only in cs101)
# David: 95 (only in cs101)
# Eve: 76 (only in math201)
# __mul__ — curve
curved = math201 * 1.1
print(f"\n{curved}")
print("Curved grades:")
for student in curved:
    print(f" {student}: {curved[student]}")
# Alice: 93.5, Bob: 99.0, Eve: 83.6
# Test cap at 100
big_curve = math201 * 1.5
print(f"\nBig curve — Bob's grade: {big_curve['Bob']}") # 100 (capped)
# === Part C: Comparisons ===
print("\n=== Part C: Comparisons ===")
print(f"CS 101 average: {cs101.average:.2f}")
print(f"Math 201 average: {math201.average:.2f}")
print(f"CS 101 == Math 201? {cs101 == math201}")
print(f"Math 201 < CS 101? {math201 < cs101}")
print(f"Math 201 <= CS 101? {math201 <= cs101}")
# Sorting
classes = [math201, cs101, curved]
classes.sort()
print("\nSorted by average:")
for gb in classes:
    print(f" {gb} — avg: {gb.average:.2f}")