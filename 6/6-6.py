favorite_languages = {"jen" : "python",
                      "sarah" : "c",
                      "edward" : "rust",
                      "phil" : "python"}

people = ["ben", "phil", "jennifer", "sarah"]

for person in people:

    if person in favorite_languages:
        print(f"{person}, thank you for responding. ")
    
    else:
        print(f"{person}, you are invited to take a poll. ")