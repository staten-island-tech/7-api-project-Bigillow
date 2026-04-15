# import requests
# people = []
# def getMC(mc):
#     response = requests.get(f"https://api.mcsrvstat.us/3/{mc.lower()}")

#     if response.status_code != 200:
#         print("Error fetching data!")
#         return None
    
#     data = response.json()
#     # print(f"Status: {data["online"]}")
#     # print(f"PLayer count: {data["players"]["online"]}")
#     # print(f"Ip: {data["ip"]}")
#     # print(f"Port: {data["port"]}")
#     for player in data['players']['list']:
#         print(player['name'])
#         people.append(player['name'])


# def getAvatar(name):
#     answer = requests.get(f"https://playerdb.co/api/player/minecraft/{name.lower()}")

#     if answer.status_code != 200:
#         print("Error fetching data!")
#         return None
    
#     playerinfo = answer.json()

#     print("User: " + playerinfo['data']['player']['username'])
#     print("Id: " + playerinfo['data']['player']['raw_id'])



# getAvatar("Bigillow")
import random

import requests

cats = [
    "animal",
    "career",
    "celebrity",
    "dev",
    "explicit",
    "fashion",
    "food",
    "history",
    "money",
    "movie",
    "music",
    "political",
    "religion",
    "science",
    "sport",
    "travel"
    ]

def getCNJ(number_of_chucknorris_jokes, type_of_chucknorris_jokes): #"animal" "career" "celebrity" "dev" "explicit" "fashion" "food" "history" "money" "movie" "music" "political" "religion" "science""sport" "travel" "random"
    
    
    for x in range(number_of_chucknorris_jokes): 
        if type_of_chucknorris_jokes.lower() == "random":
            num = random.randint(0, 15)
            response_1 = requests.get(f"https://api.chucknorris.io/jokes/random?category={cats[num]}")
        else:
            response_1 = requests.get(f"https://api.chucknorris.io/jokes/random?category={type_of_chucknorris_jokes.lower()}")
        
        if response_1.status_code != 200:
            print("Error fetching data!")
            return None

        data_1 = response_1.json()

        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("Joke number " + str(x+1) + ":")
        print(str(data_1['categories'][0]).capitalize() + " Joke: " + data_1['value'])
        print("Source Link: " + data_1['url'])
        if number_of_chucknorris_jokes == 0 or number_of_chucknorris_jokes == x+1:
            print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")


def getFact(number_of_facts, type_random_or_today): #random or today


    for i in range(number_of_facts): 
        response_2 = requests.get(f"https://uselessfacts.jsph.pl/api/v2/facts/{type_random_or_today.lower()}") 

        if response_2.status_code != 200:
            print("Error fetching data!")
            return None
    
        data_2 = response_2.json()
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("Fact number " + str(i+1) + ":")
        print(type_random_or_today.capitalize() + "'s Fun Fact: " + data_2['text'])
        print("Source: " + data_2['source'])
        print("Source Link: " + data_2['source_url'])
        if number_of_facts == 0 or number_of_facts == i+1:
            print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    

def getEntertainment(CNJ_or_Fact):
    if CNJ_or_Fact.lower() == "cnj":
        number = input("How many?")
        print("categories")
        for cat in cats:
            print(cat)
        type = input("What category?")
        getCNJ(number, type) #makestring
    elif CNJ_or_Fact.lower() == "fact":
        number = input("How many?")
        type = input("What category? Today or Random?")
        getFact(number, type)

getEntertainment("CNJ")