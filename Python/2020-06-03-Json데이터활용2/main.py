import json

with open("./base1.json") as json_file:
    base1Json = json.load(json_file)
with open("./base2.json") as json_file:
    base2Json = json.load(json_file)

for i in base1Json:
    for j in base2Json:
        if base1Json[i][0]["students"][0]["info"]["personal"]["name"] == base2Json[j]["students"][0]["id"]:
            base2Json[j]["students"][0]["age"] = base1Json[i][0]["students"][0]["info"]["personal"]["age"]

with open("base2.json", "w", encoding="utf-8") as make_file:
    json.dump(base2Json, make_file, ensure_ascii=False, indent="\t")