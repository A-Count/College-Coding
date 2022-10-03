keys = ["Ten", "Twenty", "Thirty"]
values = [10,20,30]
dictionary = dict(zip(keys, values))
print(dictionary)

sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])

NewDict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New York"

}
NewDict.pop("salary")
NewDict.pop("name")
NewDict["location"] = NewDict.pop("city")
print(NewDict)
