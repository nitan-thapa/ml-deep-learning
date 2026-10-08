#defining dictionary
info  = {
    "name":"ram",
    "name" : "nitan",
    "age":31,
    "gender":"male",
    "is_married":False

}

#accessing dictionary 
print(info["name"])

#accessing other than define keys
#print(info["country"]) #it throw  an error because country is not define
print(info.get("country")) #it does not throw an error rather it gives None

#adding new key value pair
info["address"] = "kathmandu"
print(info)

#finding length of dictionlayr
print(len(info))

#converting to list 
print(list(info.keys()))#["name","age","gender","is_married","address"]
print(list(info.values()))#["nitan",31,"male",False,"kathmandu"]
print(list(info.items()))#[("name","nitan"),(...),(..)]


#duplicate key does not exist 
#order does not matter in dictionary
#it does not have inex concept


#updating multiple dictinary
info1 = {
    "name":"nitan"
}

info1.update({"age":31,"gender":"male"})
print(info1)