import requests
people = []
def getMC(mc):
    response = requests.get(f"https://api.mcsrvstat.us/3/{mc.lower()}")

    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    # print(f"Status: {data["online"]}")
    # print(f"PLayer count: {data["players"]["online"]}")
    # print(f"Ip: {data["ip"]}")
    # print(f"Port: {data["port"]}")
    for player in data["players"]["list"]:
        print(player["name"])
        people.append(player["name"])


def getAvatar(name):
    answer = requests.get(f"https://playerdb.co/api/player/minecraft/{name.lower()}")

    if answer.status_code != 200:
        print("Error fetching data!")
        return None
    
    playerinfo = answer.json()

    for info in playerinfo["data"]["player"]: mavatar




getMC("donutsmp.net") 
