#My_info Dictionary beginner
my_info = {"name": "Noah Bradbury", "age": 19, "major": "Cybersecurity"}

#menu dictionary and course_Credits dictionary
menu = {"Burger": 9.99, "Fries": 3.99, "Pop": 1.00, "Salad": 6.99, "Chicken Sandwich": 9.99}

course_Credits = {"CS1350": 3, "CJ1100": 3, "CS2500": 3, "PSY1700": 3}

#weekly_temps dictionary using () instead of[]
weekly_temps = dict(monday=74, tuesday=78, wednesday=80, thursday=79, friday=79, saturday=80, sunday=75)

#printing the pets name and age
pet = {"name": "Buddy", "type": "dog", "age": 3}

print(pet["name"])
print(pet["age"])

#get
print(pet.get("color", "Unknown"))

grades = {"Matt": 90, "Stephanie": 83, "Tyler": 54}

def check_if_pass(name, grade, passing_grade=60):
    grade = grades.get(name, "Unknown")
    
    if grade == "Unknown":
        return f"{name} is not enrolled in the course."
    elif grade >= passing_grade:
            return f"{name} passed with a grade of {grade}."
    else:
        return f"{name} failed with a grade of {grade}."

print(check_if_pass("Matt", grades))
print(check_if_pass("Tyler", grades))
print(check_if_pass("Noah", grades))

#1.3 
inventory = {}

inventory ["Apples"] = 10
inventory ["Bread"] = 8
inventory ["Milk"] = 5

scores = {"Team A": 45, "Team B": 38}

scores["Team B"] = 52

scores ["Team C"] = 41

blew = scores.pop("Team A")

#cartdictionary
cart = {}

cart["Shirt"] = 15
cart["Pants"] = 20
cart["Shoes"] = 50

cart["Shirt"] = 17

removed_item = cart.pop("Pants")
print(f"Item removed: {removed_item}")

print(cart)

#2.1
#a) "student_name"   valid (reason: it is a string)  
#b) [1, 2, 3]  not valid (reason: this is because it is a list)  
#c) 100     valid (reason: it is a integer)    
#d) ("x", "y")     valid (reason: it is a tuple)    
#e) {"a": 1}       not valid (reason: this is because it is a dictionary)      
#f) frozenset({1,2})  # valid (reason: because it is a frozenset)


locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}

# I think It will print a with 3 and b with 4 because they are the last interation of the items in the dictionary and it will also print 2 because they have the same 2 names
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data))

print(hash("Noah Bradbury"))
print(hash(100))

high_scores = {("Noah", "pacman"): 3332360, ("Noah", "tetris"): 560000, ("Noah", "snake"): 20000}

print(high_scores[("Noah", "pacman")])

import time

giant_list = list(range(100000))
giant_dict = {i: i for i in range(100000)}

start = time.time()
result = 99999 in giant_list
list_end = time.time() - start

start = time.time()
result = 99999 in giant_dict
dict_end = time.time() - start

print(f"List search time: {list_end:.6f} seconds")
print(f"Dictionary search time: {dict_end:.6f} seconds")
print(f"Dictionary search is faster than list search by {list_end / dict_end:.2f} times.")

#2.2
import sys
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(temps.items())

print(max(temps.values()), min(temps.values()))
print(f"Friday" in temps)

temps.setdefault("Thursday", 70)
print(temps)

temps_look = temps.keys()
print("Before:", temps_look)

temps["Friday"] = 67
print("After:", temps_look)

prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
#advanced 1
total = sum(prices.values())
average = total / len(prices)
print(f"Total: {total}")
print(f"Average: {average}")
#advanced 2
most_expensive = max(prices, key=prices.get)
least_expensive = min(prices, key=prices.get)
print(f"Most expensive: {most_expensive} at {prices[most_expensive]}")
print(f"Least expensive: {least_expensive} at {prices[least_expensive]}")
#advanced 3
import sys
keys_view = prices.keys()
keys_list = list(prices.keys())
print(f"Size of price key view: {sys.getsizeof(keys_view)}")
print(f"Size of price key list: {sys.getsizeof(keys_list)}")
#advanced 4
prices.update({"headphones": 199, "monitor": 349, "keyboard": 89})
print(prices)

#2.3
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
     print(f"The {fruit} is {color}.")

## It will give me both the key and value of the key and value of the dictionary.

new_menu = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}

for item, price in new_menu.items():
     with_tax = price * 1.10
     print(f"{item}: ${with_tax:.2f}")

count = 0
for item, price in new_menu.items():
    if price > 4.00:
        count += 1

print(f"Number of items in the menu over 4.00: {count}")

x = 10
y = 20 
x, y = y, x 

print(x, y)

nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print(first)
print(middle)
print(last)

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

top_student = max(scores.items(), key=lambda x: x[1])
print(f"Top student: {top_student[0]} with a score of {top_student[1]}")

passed = {}
failed = {}
for name, grade in scores.items():
     if grade >= 60:
         passed[name] = grade
     else:
         failed[name] = grade
print(f"Passed: {passed}")
print(f"Failed: {failed}")

average = sum(scores.values()) / len(scores)

print(f"Average score: {average}")

deviations = {name: round(grade - average, 2) for name, grade in scores.items()}
print(deviations)

import time

big_scores = {f"Student{i}": i for i in range(50000)}

start = time.time()
total1 = 0 

for name, score in big_scores.items():
    total1 += score

items_end = time.time() - start

start = time.time()
total2 = 0
for name in big_scores.keys():
    total2 += big_scores[name]
values_end = time.time() - start

print(f"Total from items(): {total1}")
print(f"Total from keys(): {total2}")
print(f"Time taken for items(): {items_end}")
print(f"Time taken for keys(): {values_end}")



