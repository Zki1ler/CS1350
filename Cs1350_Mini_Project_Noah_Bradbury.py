contact_book = {
"Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
"Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
"Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
"Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
"Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
"Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
"Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
"Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}
# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
"Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
"Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
"Sister": {"Jan": 80, "Mar": 70},
"Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
"Roommate": {"Feb": 15, "Mar": 25},
"Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
"Professor": {"Feb": 20, "Mar": 35},
"Dentist": {"Jan": 10},
}

print("Phase 1")
quick_contacts = {}
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-4321"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"

print("quick contacts:", quick_contacts)

print("Moms Number:", quick_contacts["Mom"])

quick_contacts["Dad"] = "555-4321"
quick_contacts["Dentist"] = "555-2222"

print(quick_contacts.get("Grandma", "Contact Not Found"))

print("quick contacts updated:", quick_contacts)

del quick_contacts["Pizza Place"]

old_work = quick_contacts.pop("Work")
print("old work", old_work)

print(len(quick_contacts))
print(list(quick_contacts.keys()))
print(list(quick_contacts.values()))

print("Phase 2")
total_minutes = {}

for contact, months in call_log.items():
    num_of_months = len(months)
    total = sum(months.values())
    average_minutes = total / num_of_months if num_of_months > 0 else 0

    busiest_month = None
    busiest_minutes = 0
    for month, minutes in months.items():
        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month

    total_minutes[contact] = total

    print(f"{contact}: {num_of_months} months, {total} total minutes, {average_minutes:.2f} average minutes per month, busiest month: {busiest_month} with {busiest_minutes} minutes")

print()
print ("Phase 3")
#partA
month_stats = {}


for contact, months in call_log.items():
    for month, minutes in months.items():
        if month not in month_stats:
            month_stats[month] = {"minutes": [], "total": 0, "average": 0, "contacts": 0}
        month_stats[month]["minutes"].append(minutes)

for month, stats in month_stats.items():
    stats["total"] = sum(stats["minutes"])
    stats["contacts"] = len(stats["minutes"])
    stats["average"] = stats["total"] / stats["contacts"] 

for month, stats in sorted(month_stats.items()):
    print(f"{month}: minutes={stats['minutes']}, total = {stats['total']}, "
        f"average = {stats['average']:.2f}, contacts = {stats['contacts']}")

print()
#partB

minutes_categories = {}
minutes_by_city = {}
contacts_each_city = {}

for contact, total in total_minutes.items():
    dets = contact_book[contact]
    category = dets["category"]
    city = dets["city"]

    minutes_categories[category] = minutes_categories.get(category, 0) + total
    minutes_by_city[city] = minutes_by_city.get(city, 0) + total
    contacts_each_city[city] = contacts_each_city.get(city, 0) + 1

print("minutes by category:", minutes_categories)
print("minutes by city:", minutes_by_city)
print("contacts per city:", contacts_each_city)


print()
print("Phase 4")

phone_book = {name: details["phone"] for name, details in contact_book.items()}

local_contacts = {name: details for name, details in contact_book.items() if details["city"] == "Fort Wayne"}

activity_level = {name: "Frequent" if total >= 200 else "Occasional" for name, total in total_minutes.items()}

print()
print("phone book:", phone_book)
print()
print("local contacts:", local_contacts)    
print()
print("activity level:", activity_level)

print()
print("Phase 5")
def get_contact_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "inactive"



for contact, total in total_minutes.items():
    tier = get_contact_tier(total)
    print(f"{contact}: {total} minutes, {tier} tier")

plat_count = 0
gold_count = 0 
silver_count = 0 
bronze_count = 0
inactive_count = 0

for contact, total in total_minutes.items():
    tier = get_contact_tier(total)
    if tier == "Platinum":
        plat_count += 1
    elif tier == "Gold":
        gold_count += 1
    elif tier == "Silver":
        silver_count += 1
    elif tier == "Bronze":
        bronze_count += 1
    else:
        inactive_count += 1


print(f"Platinum: {plat_count}")
print(f"Gold: {gold_count}")
print(f"Silver: {silver_count}")
print(f"Bronze: {bronze_count}")
print(f"Inactive: {inactive_count}")


most_contact = None
most_minutes = -1
least_contact = None
least_minutes = None
tots_amount = 0

for contact, total in total_minutes.items():
    tots_amount += total
    if total > most_minutes:
        most_minutes = total
        most_contact = contact
    if least_minutes is None or total < least_minutes:
        least_minutes = total
        least_contact = contact

average_min = tots_amount / len(total_minutes) 

print(f"Most contated: {most_contact} with {most_minutes} minutes")
print(f"Least contacted: {least_contact} with {least_minutes} minutes")
print(f"Big Total: {tots_amount} minutes, average: {average_min:.2f} minutes")

print("Above average")

for contact, total in total_minutes.items():
    if total > average_min:
        print(f"{contact}: {total} minutes")

#phase 6
print("=== Phase 6: Contact Hub Report ===")
print(f"{'Name':<12}{'Category':<10}{'City':<14}{'Minutes':>8}  {'Tier'}")
print("-" * 57)

sorted_contacts = sorted(total_minutes.items(), key=lambda pair: pair[1], reverse=True)

for name, total in sorted_contacts:
    details = contact_book[name]
    category = details["category"]
    city = details["city"]
    tier = get_contact_tier(total)
    print(f"{name:<12}{category:<10}{city:<14}{total:>8}  {tier}")

print("-" * 57)
print(f"{len(total_minutes)} contacts | {sum(total_minutes.values())} total minutes |"
        f"{sum(total_minutes.values()) / len(total_minutes):.2f} average")