# In this Day, Prof. Angela Yu describes the many other HTTPS module requests like GET , PUT , POST , and DELETE
import requests


# Constants 
FILE_PATH = "/Users/lovely/Documents/Udemy/SECRET_API_KEYS/pixela.txt"
USERNAME = "joel-lovely07"
 
USER = {
    'username' : USERNAME, 
    'agreeTermsOfService' : 'yes', 
    'notMinor' : 'yes', 
}

HEADER = {
    
}

GRAPH = {
    'id' : 'frosty-clover7',
    'name' : 'Udemy_Graph',
    'unit' : 'Days', 
    'type' : 'int',
    'color' : 'shibafu' 
}

API_ENDPOINT_CU = "https://pixe.la/v1/users"
API_ENDPOINT_G = f"{API_ENDPOINT_CU}/{USERNAME}/graphs"

def read_secret_token():
    """function to read token from secret path file"""
    global USER
    with open(FILE_PATH) as file:
        secret = file.read()
        USER['token'] = secret
        HEADER['token'] = secret
        return USER , HEADER
    
def create_user_acccount():
    """function for creating a user"""
    read_secret_token()
    with requests.post(url=API_ENDPOINT_CU, json=USER) as connection:
        print(connection.text)

def check(k , d):
    global GRAPH
    user_input = input(f"Please give me the feature - ({k}) of the graph dictonary ").lower()
    d[k] = user_input
    return GRAPH

def create_graph():
    global GRAPH
    read_secret_token()
    with requests.post(url=API_ENDPOINT_G, json=GRAPH, headers=HEADER) as connection:
        print(connection.text)
#create_user_acccount()       
#create_graph()
# Unfortunately this API isn't working with basic creation so I had to skip today! 
