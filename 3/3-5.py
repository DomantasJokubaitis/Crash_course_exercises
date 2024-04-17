people = ["Mom", "Dad", "Girlfriend"]

print(f"Hi {people[0].lower()}, I am inviting you to dinner tomorrow. ")
print(f"Hi {people[1].lower()}, I am inviting you to dinner tomorrow. ")
print(f"Hi {people[2].lower()}, I am inviting you to dinner tomorrow. ")

print(f"\n{people[2]} can't make it to dinner.\n ")

del people[2]
people.append("Best friend")

print(f"Hi {people[0].lower()}, I am inviting you to dinner tomorrow. ")
print(f"Hi {people[1].lower()}, I am inviting you to dinner tomorrow. ")
print(f"Hi {people[2].lower()}, I am inviting you to dinner tomorrow. ")