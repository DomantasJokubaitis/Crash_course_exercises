people = ["Mom", "Dad", "Girlfriend", "Best friend"]

print(f"Hi {people[0].lower()}, I am inviting you to dinner tomorrow. ")
print(f"Hi {people[1].lower()}, I am inviting you to dinner tomorrow. ")
print(f"Hi {people[2].lower()}, I am inviting you to dinner tomorrow. ")
print(f"Hi {people[3].lower()}, I am inviting you to dinner tomorrow. ")

print(f"\nHello all, unfortunately the table is too small for us all, I can only invite two of you!\n ")

popped1 = people.pop(-1)
popped2 = people.pop(-1)

print(f"I'm very sorry {popped1}, but since the table is too small for us all, I have to uninvite you. ")
print(f"I'm very sorry {popped2}, but since the table is too small for us all, I have to uninvite you. ")

print(f"\nHi {people[0].lower()}, you are still invited to dinner tomorrow. ")
print(f"Hi {people[1].lower()}, you are still invited to dinner tomorrow. ")

del people[0]
del people[0]
print(people)