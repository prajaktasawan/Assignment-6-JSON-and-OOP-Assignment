import json

states = {
    "Andhra Pradesh": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Maharashtra": "Mumbai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}

with open('states.json', 'w') as file:
    json.dump(states, file)
