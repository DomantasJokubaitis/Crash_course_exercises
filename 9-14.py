from random import choice

all_symbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
lucky_simbs = []

x = 4
while x > 0:
    chosen = choice(all_symbs)
    lucky_simbs.append(chosen)
    all_symbs.remove(chosen)
    x -= 1

print(f"The lucky symbols are: ")
for element in lucky_simbs:
    print(element)
