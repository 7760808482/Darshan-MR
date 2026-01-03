
1------>.  Basic Dictionary Operations:

Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary.

# creating a dictionary with 5 cities and thier famous dieshes
dieshes={
    "Bengaluru":"Bisi Bele Bath",
    "Mysuru":"Mysore Pak",
    "Udupi":"Masala Dosa",
    "Hubli":"Jolad Roti",
    "Davangere":"Davangere Benne Dose"
}
#adding a new city and its dish to the dictionarry
dieshes["Ramanagara"]="Ragi Mudde"
print(dieshes)
#updating the dish for BEngaluru
dieshes["Bengaluru"]="Vangi Bath"
print(dieshes)
#removing the city from the dictionary
dieshes.pop("Mysuru")
print(dieshes)
#using keys() method to print all city names in the dictiorynary
print(dieshes.keys())
#using values() method to print all the dishes in the dictiory
print(dieshes.values())




