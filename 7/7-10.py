isactive = True

people = {}

while isactive:
    person = input("What is your name? ")
    vacation = input("What is your dream vacation spot? ")

    people[person] = vacation

    repeat = input("Will you let another user respond? ")

    if repeat == "no":
        isactive = False

for person, vacation in people.items():
    print(f"\n{person} would like to vacation in {vacation}")