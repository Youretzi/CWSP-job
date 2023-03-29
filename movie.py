import requests
import json

def num_location():
    n = input("Number of locations: ")
    return n
    
def landitude_input():
    id = input("Laditude ; Longitude(Latitude must be between -90 and 90): ")
    w = len(id.split(","))
    if w != 2:
        id = (input("Enter new input: "))
        print(id)
    elif id == "":
        id = (input("Enter new input: "))
        print(id)
    elif id.isalpha() is True:
        id = (input("Enter new input: "))
        print(id)
    floats = [float(x) for x in id.split(",")]
    if (90 < floats[1] or floats[1] < -90):
        id = (input("Enter new input: "))
        print(id)
    return id
    
def base_maps(id):
    Blitz = "access_token=pk.eyJ1IjoieWFyaTEyMyIsImEiOiJjbGVxMXk3YWcwMDA4NDNxNjNlbWlkM3YyIn0.yZzDMMojbDVqUP9X2Fe_JA"

    url = "https://api.mapbox.com/directions/v5/mapbox/driving/" + str(id) + "?" + Blitz + "&steps=true" + "&overview=simplified"
   
    response = requests.request("GET", url)
    return response.json()
    
def length_list(id, b):
    if (b["routes"]) == []:
        print("Route to destination does not exit")
        raise SystemExit
    g = (len(b["routes"][0]["legs"][0]["steps"]))
    print(len(b["routes"][0]["legs"][0]["steps"]))
    return g
        
def clean_up():
    n = num_location()
    n = int(n)
    id = ""
    for x in range(n):
        c = landitude_input()
        id = id + c + ";"
    id = str(id[:-1])
    print(id)
    b = base_maps(id)
    f = length_list(id, b)
    f = int(f)
    for x in range(n):
        print("Location name", x ,": ", b["waypoints"][x]["name"])
        print("Cordinates" , x , ": ", b["waypoints"][x]["location"])
    for x in range(n-1):
        print("Duration: ", x , ": ",  b["routes"][0]["legs"][x]["duration"])
        print("Distance: " , x , ": ",  b["routes"][0]["legs"][x]["distance"])
    for x in range(f):
        print("Step", x , ": ", b["routes"][0]["legs"][0]["steps"][x]["maneuver"]["instruction"])
print(clean_up())
    
 #-118.7724595,34.0461816
 #-116.7101469,33.8330735
 #-122.4628686,37.4976533
 
#-121.9169323,37.3597369
#-121.8637957,37.3493242
