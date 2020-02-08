
import json

i=0
with open('msdhoni_followers.json',encoding="utf8") as f: 
      obj = json.load(f)


for objs in obj: 
    i+=1
    print(str(i)+" "+objs['screen_name'])
    if i==100:
        breakword
