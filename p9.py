details={
    "Name": "Darshan",
    "sem": 3,
    "branch": "AIML"
}
print(details.get("Loaction","Not found"))

#addinnd laocation
details["Loaction"] = "Karnataka"
print(details)


#updating location
details["Loaction"]="Bengaluru"


#delating name using pop() function
details.pop("Name")
print(details)


#dealting the name using del() function
del details["branch"]
print(details)

# clrering the all the function using clear() function
details.clear()
print(details)


#creating two function and adding into one function using update() function
country={
    "country1":"India",
    "capital1":"New Delhi"
    
}
state={
    "state1":"Karnataka",
    "capital2":"Bengaluru"
}
print(country.update(state))