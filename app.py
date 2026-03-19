import requests

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

getMC("donutsmp.net")