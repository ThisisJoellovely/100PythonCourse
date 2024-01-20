import requests

PARAMETERS = {
    "amount" : 10,
    "category" : 9,
    "diffuculty" : "medium",
    "type" : "boolean"
}


# Implementation of the Open-Triva Database
with requests.get("https://opentdb.com/api.php",params=PARAMETERS) as connection:
    connection.raise_for_status()
    data = connection.json()
    question_data = data["results"]
    
