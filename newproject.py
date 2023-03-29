import requests
import json
import collections
'''
def send_requests():
    url = "https://catfact.ninja/fact"
    request = requests.get(url)
    return request.json()
    
#print(send_requests())
def store_facts_length():
    sample = send_requests()
    return [sample["fact"], sample["length"]]
#store_facts_length()
my_list = []
my_list2 = []
for i in range(3):
    t = store_facts_length()
    #print(t)
    my_list.append(t[0])
    my_list2.append(t[1])
print(my_list)
print(my_list2, sum(my_list2)/len(my_list2))
'''

names = ["Citlali", "Emily", "Arlene","Brianna", "Anthony","Alisson"]
def send_requests(name):
    url = "https://api.nationalize.io?name=" + name
    print(url)
    request = requests.get(url)
    return request.json()
    
#def process_response(y):
    #print(y["country"])
    #print(process_response(y))
    
t = collections.Counter()
r = {}
for x in range(len(names)):
    y = send_requests(names[x])
    for z in range(len(y["country"])):
        c = (y["country"][z]["country_id"])
    #print(y.keys())
   # print(y["country"][0].keys())
        print(c)
        t[c] += 1
        print(t)


 


