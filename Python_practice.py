counties = ["Arapahoe", "Denver", "Jefferson"]
counties.insert(1, "El Paso")
counties.pop(0)
counties[2] = "Denver"
counties[1] = "Jefferson"
counties.append("Arapahoe")
print(counties)
counties_tuple = ("Arapahoe", "Denver", "Jefferson")
len(counties_tuple)
counties_tuple[1]
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)    
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
len(counties_dict)
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")
counties_dict["Arapahoe"]
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1, {"county":"El Paso", "registered_voters":461149})
voting_data.remove({"county":"Arapahoe", "registered_voters":422829})
voting_data[2] = ({"county":"Denver", "registered_voters":463353})
voting_data[1] = ({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

for num in range(5):
    print(num)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)