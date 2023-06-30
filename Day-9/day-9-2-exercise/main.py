travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

#🚨 Do NOT change the code above


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visted, visits_visted, cities_visted):
  new_travel_log = {}
  new_travel_log["country"]=country_visted 
  new_travel_log["visits"]=visits_visted
  new_travel_log["cities"]=cities_visted
  print(
        f"You've visited {new_travel_log['country']} {new_travel_log['visits']} times."
    )
  print(
        f"You've been to {new_travel_log['cities'][0]} and {new_travel_log['cities'][1]}"
    )

  travel_log.append(new_travel_log)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
