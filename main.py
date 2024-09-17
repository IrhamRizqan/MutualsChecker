import json

file = open("data/newestData/followers_1.json")

data = json.load(file)

follower = []

for i in data:
    for j in i["string_list_data"]:
        follower.append(j["value"])
        
file2 = open("data/newestData/following.json")

file2data = json.load(file2)

following = []

for i in file2data["relationships_following"]:
    for j in i["string_list_data"]:
        following.append(j["value"])
        
mutuals = []

for i in following:
    if i in follower:
        mutuals.append(i)

for i in following:
    if i not in mutuals:
        print("https://www.instagram.com/",i)