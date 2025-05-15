# How to Connect to an APIs using Python
# Website APIs => https://pokeapi.co/
# For Example => https://pokeapi.co/api/v2/pokemon/pikachu

print()
import requests
# Note : >> Jika tidak ada di <python 3.8 (Your Version Python)> => Lib => site-packages library install from Terminal :
#        pip install requests

Base_URL = "https://pokeapi.co/api/v2/"

def Get_Pokemon_Info (name) :
    URL = f"{Base_URL}/pokemon/{name}"
    Response = requests.get(URL)
    print(Response)

    if Response.status_code == 200 :
        # print("Data Retrieved!")              # For Test 1
        Pokemon_Data = Response.json()
        # print(Pokemon_Data)                   # For Test 2
        return Pokemon_Data
    else :
        print(f"Failed to Retrieve Data {Response.status_code}")

Pokemon_Name = "pikachu"
# Get_Pokemon_Info(Pokemon_Name)                # For Test 2
Pokemon_Info = Get_Pokemon_Info(Pokemon_Name)

if Pokemon_Info :
    # print(f"Name : {Pokemon_Info['name']}")           # OR
    print(f"Name : {Pokemon_Info['name'].capitalize()}")
    print(f"ID : {Pokemon_Info['id']}")
    print(f"Height : {Pokemon_Info['height']}")
    print(f"Weight : {Pokemon_Info['weight']}")

print()
Pokemon_Name = "squirtle"
# Get_Pokemon_Info(Pokemon_Name)                # For Test 2
Pokemon_Info = Get_Pokemon_Info(Pokemon_Name)

if Pokemon_Info :
    # print(f"Name : {Pokemon_Info['name']}")           # OR
    print(f"Name : {Pokemon_Info['name'].capitalize()}")
    print(f"ID : {Pokemon_Info['id']}")
    print(f"Height : {Pokemon_Info['height']}")
    print(f"Weight : {Pokemon_Info['weight']}")