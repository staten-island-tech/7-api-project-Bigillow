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

import requests
def getFact(number_of_facts, type_random_or_today):
    response = requests.get(f"https://uselessfacts.jsph.pl/api/v2/facts/{type_random_or_today.lower()}")

    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()

    for i in range(number_of_facts):
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print(type_random_or_today.capitalize() + "'s Fun Fact: " + data['text'])
        print("Source: " + data['source'])
        print("Source Link: " + data['source_url'])
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

getFact(1, "random")