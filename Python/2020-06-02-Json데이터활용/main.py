import os
import json

with open("./first.json") as json_file:
    firstJson = json.load(json_file)
with open("./second.json") as json_file:
    secondJson = json.load(json_file)

if firstJson["id"] == secondJson["name"]:
    secondJson["age"] = firstJson["age"]
    with open("second.json", "w", encoding="utf-8") as make_file:
        json.dump(secondJson, make_file, ensure_ascii=False, indent="\t")