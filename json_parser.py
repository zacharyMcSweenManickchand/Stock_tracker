import json

url_list = []
name_list = []
def parse_json():
    with open("Url.json", "r") as json_file:
        x = json.load(json_file)
    for y in x["Sites"]:
        #print(x["Sites"][str(y)]["url"])
        url_list.append(str(x["Sites"][str(y)]["url"]))
        name_list.append(str(x["Sites"][str(y)]["name"]))
    json_file.close()