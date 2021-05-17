#adding to Json file
import json

Dict= {"Name": "Bob",
       "Surname": "BUilder",
       "Age": 57}
with open("new.ext", "w") as json_file:
    json.dump(Dict, json_file)