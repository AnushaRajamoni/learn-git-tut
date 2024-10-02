import datetime
print("welcome to age calculator program") 
age = int(input("enter year of birth: ")) 
years = datetime.datetime.now().year - age
print(f"current age: {years} years")
