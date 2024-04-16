from random import choice

x = 4
y = 1
lucky_simbs = []
all_symbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]

while x > 0:
    my_ticket = [2, 4, 9, "d"]
    chosen = choice(all_symbs)
    lucky_simbs.append(chosen)
    all_symbs.remove(chosen)
    x -= 1

    if x == 0:
        check = True

        for item in my_ticket:

            if item not in lucky_simbs:
                check = False
                print(f"\nWomp womp\n")
                y += 1
                x = 4
                all_symbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]
                lucky_simbs = []
                break
            
        if check == True:
            print(f"\n\n\nYou won after {y} tries! \n\n\n")
            print(lucky_simbs)
            break
