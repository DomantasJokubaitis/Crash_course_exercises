MyList = ["Lietuva", "Lenkija", "Vokietija", "Prancuzija", "Ispanija"]

MyList.append("Portugalija")
print(MyList)
MyList.remove("Lietuva")
print(MyList)
del MyList[-1]
print(MyList)
Mein = MyList.pop(0)
print(f"I removed {Mein} from this list. The list currently has {len(MyList)} items. ")
MyList.sort()
print(MyList)
MyList.reverse()
print(MyList)