import requests 
import json
import re


def user_input():
    x = input("Enter Artist: ")
    return x
    
def song_input():
    s = input("Song Name: ")
    return s

def general_search(x):
    url = "https://spotify23.p.rapidapi.com/search/"
    querystring =  {"q": x, "type":"multi","offset":"0","limit":"5","numberOfTopResults":"1"}
    headers = {
        "X-RapidAPI-Key": "5323acd73amsh02c6afc0f59936fp19ba04jsn7a1b59a8f515",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()
    
def get_artist(x):
    url = "https://spotify23.p.rapidapi.com/artists/"
    
    querystring = {"ids": re.split(':|=', x )[-1]}
    headers = {
        "X-RapidAPI-Key": "5323acd73amsh02c6afc0f59936fp19ba04jsn7a1b59a8f515",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()
    
def get_album(x):
    url = "https://spotify23.p.rapidapi.com/albums/"
    querystring = {"ids": re.split(':|=', x )[-1]}
    headers = {
        "X-RapidAPI-Key": "5323acd73amsh02c6afc0f59936fp19ba04jsn7a1b59a8f515",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def get_tracks(s):
    url = "https://spotify23.p.rapidapi.com/tracks/"

    querystring = {"ids": s }

    headers = {
        "X-RapidAPI-Key": "5323acd73amsh02c6afc0f59936fp19ba04jsn7a1b59a8f515",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

def specefic_search():
    x = user_input()
    s = song_input()
    w = x + " " + s
    print(w)
    c = general_search(x)
    albums = general_search(w)
    #print(general_search(x))
    print(albums)
    print("Artist:", c["users"]["items"][0]["data"]["displayName"])
    print("Username:", c["users"]["items"][0]["data"]["username"])
    #print("3", c["albums"]["items"][0]["data"]["uri"])
    id = c["albums"]["items"][0]["data"]["artists"]["items"][0]["uri"]
    re.split(':|=', id)[-1]
    g = get_artist(id)
    print("Artist Account:", g["artists"][0]["external_urls"]["spotify"])
    print("Total Followers:", g["artists"][0]["followers"]["total"])
    print("Genres:", g["artists"][0]["genres"])
    
    r = c["tracks"]["items"][0]["data"]["id"]
    print(c["tracks"]["items"][0]["data"])
    ida = c["albums"]["items"][0]["data"]["uri"]
    h = get_album(ida)
    #print(h)
    #print("", h["albums"][0]["type"])
    print("Album Name:", h["albums"][0]["name"])
    b = get_tracks(r)
    #print(b)
    print("Song:", b["tracks"][0]["name"])
    
    print("Album Link:", h["albums"][0]["external_urls"]["spotify"])
    #print("Album id:", h["albums"][0]["id"])
    print("Song Link:", b["tracks"][0]["external_urls"]["spotify"])
specefic_search()



    
    
    


