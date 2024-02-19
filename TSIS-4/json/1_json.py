import json 

with open("TSIS-4/json/sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("="*80)
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  -----")
for elements_data in data['imdata'] :
   DN = elements_data['l1PhysIf']['attributes']["dn"]
   Description = elements_data["l1PhysIf"]['attributes']['descr'] 
   Speed = elements_data["l1PhysIf"]['attributes']['speed']
   MTU = elements_data["l1PhysIf"]['attributes']['mtu']
   if len(DN) == 42 :
       print(DN , Description ,"                            " , Speed , MTU)
   else:
       print(DN , Description ,"                             " , Speed , MTU)
  