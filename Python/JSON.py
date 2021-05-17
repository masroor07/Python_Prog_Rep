import json
#converting to python json by creating a dictionary
'''person= '{"Name": "Ritik", "Class": 10}'
peron_dict= json.loads(person)
print(peron_dict)'''

# opening a Java Script dictionary
with open("Data.json") as f:
    data= json.load(f)

    print(json.dumps(data, indent= 4, sort_keys=True))