#Week2Lecture1 
#3.1

inventory = {"apples": 50, "bananas": 30, "oranges": 25}

for fruit in inventory:
    print(fruit)

total = sum(inventory.values())
print(total)

for fruit, quantity in inventory.items():
    print(f"{fruit}: {quantity}")


prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

for product in sorted(prices):
    print(product, prices[product])

for product in sorted(prices, key=prices.get):
    print(product, prices[product])

most_expensive = max(prices, key=prices.get)
print(f"The most expensive product is {most_expensive} at ${prices[most_expensive]}")

temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}
average = sum(temps.values()) / len(temps.values())
print(f"Average temperature: {average:.1f}")

hottest_day = 0
coldest_day = 0

hottest_temp = 0
coldest_temp = 1000000000
for day, temp in temps.items():
    if temp > hottest_temp:
        hottest_temp = temp
        hottest_day = day
    if temp < coldest_temp:
        coldest_temp = temp
        coldest_day = day

print(f"Hottest day: {hottest_day} with {hottest_temp}°F")
print(f"Coldest day: {coldest_day} with {coldest_temp}°F")

above_average_count = 0
for temp in temps.values():
    if temp > average:
        above_average_count += 1
    
print(f"Number of days above average: {above_average_count}")


#3.2
products = {
"laptop": {"price": 999, "stock": 15},
"phone": {"price": 699, "stock": 50}
}

print(products["laptop"]["price"])

for name, details in products.items():
    print(f"{name}: {details['stock']} in stock")

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = dict(zip(countries, capitals))
print(country_capitals)

products["tablet"] = {"price": 449, "stock": 30}
print(products)

for name in list(products.keys()):
    if products[name]["stock"] < 20:
        del products[name]
print(products)

company = {
"Engineering": {"Alice": 95000, "Bob": 85000},
"Marketing": {"Carol": 75000, "Dave": 70000}
}
for department, employees in company.items():
    for name, salary in employees.items():
        print(f"{department} - {name}: ${salary}")

for department, employees in company.items():
    avg_salary = sum(employees.values()) / len(employees.values())
    print(f"{department} average: ${avg_salary:.2f}")

highest_name = None
highest_dept = None
highest_salary = 0
for department, employees in company.items():
    for name, salary in employees.items():
        if salary > highest_salary:
            highest_salary = salary
            highest_name = name
            highest_dept = department

print(f"Highest salary: {highest_name} from {highest_dept} with ${highest_salary}")



#3.3
the_cube = {n: n**3 for n in range(1, 6)}
print(the_cube)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}
celsius = {day: (f - 32) * 5/9 for day, f in temps.items()}
print({day: round(c, 1) for day, c in celsius.items()})


sales = [
    ("North", "Alice", 5000), ("South", "Bob", 4500),
    ("North", "Carol", 6000), ("South", "Alice", 3500)
]

sales_region = {}
for region, person, amount in sales:
    sales_region[region] = sales_region.get(region, 0) + amount


sales_per_person = {}
for region, person, amount in sales:
    sales_per_person[person] = sales_per_person.get(person, 0) + amount

print(sales_per_person)


nested_sales = {}
for region, person, amount in sales:
    if region not in nested_sales:
        nested_sales[region] = {}
    nested_sales[region][person] = nested_sales[region].get(person, 0) + amount

print(nested_sales)



#set1
vowels = {"a", "e", "i", "o", "u"}
print(vowels)

nums = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(nums)         
print(len(nums)) 


#3
#it fails because it creates an empty dictionary not a set

text = "mississippi"
unique_characters = set(text)
print(unique_characters)        
print(len(unique_characters)) 


emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = list(set(emails))
print(unique_emails)

#3
#it fails because lists are mutable and are not able to be hashed so python gives a type error


import time

bigset = set(range(1000000))
biglist = list(range(1000000))

start = time.perf_counter()
999999 in bigset
set_time = time.perf_counter() - start

start = time.perf_counter()
999999 in biglist
list_time = time.perf_counter() - start

print(f"Set: {set_time:.8f}")
print(f"List: {list_time:.8f}")

frozen = frozenset(["a", "b", "c"])
my_dict = {frozen: "some value"}
print(my_dict)


edged = [(1, 2), (2, 3), (1, 3), (3, 4)]
nods = {n for edge in edged for n in edge}
print(nods)  

#set2
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) 
print(a & b)
print(a - b) 

morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

all_shifts = morning_shift & evening_shift & weekend_shift
print(all_shifts)

ashift = morning_shift | evening_shift | weekend_shift
print(ashift) 

morning = morning_shift - evening_shift - weekend_shift
print(morning)

in_dos_plus = ((morning_shift & evening_shift) |
                   (morning_shift & weekend_shift) |
                   (evening_shift & weekend_shift))
uno = ashift - in_dos_plus
print(uno)

prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

eligible = prereqs_met & has_space & paid_tuition
print(eligible)

prereqs_no_payment = prereqs_met - paid_tuition
print(prereqs_no_payment)

missing_a_ting = (prereqs_met | paid_tuition) - (prereqs_met & paid_tuition)
print(missing_a_ting)

#set3

s = {1, 2, 3}
s.add(4)
s.remove(1)
print(s) 

evens = {n for n in range(21) if n % 2 == 0}
print(evens)

s = {1, 2, 3}
s.discard(99)  
try:
    s.remove(99)  
except KeyError:
    print("remove() raised KeyError, discard() did not")



lst = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
seen = set()
result = []
for item in lst:
    if item not in seen:
        seen.add(item)
        result.append(item)
print(result)

sentence = "To be or not to be that is the question"
unique_words = {word.lower() for word in sentence.split()}
print(unique_words)


expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}
missing = expected - actual
print(missing)

def find_duplicates(lst):
    seen = set()
    duplikate = set()
    for item in lst:
        if item in seen:
            duplikate.add(item)
        else:
            seen.add(item)
    return duplikate
print(find_duplicates([1, 2, 2, 3, 3, 3, 4])) 

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

all_trios = alice & bob & carol
print(f"All three have: {all_trios}")            

alice_only = alice - bob - carol
print(f"Only Alice has: {alice_only}")            

all_unique = alice | bob | carol
print(f"All unique skills: {all_unique}")

def common_characters(s1, s2):
    return set(s1) & set(s2)

print(common_characters("hello", "world")) 