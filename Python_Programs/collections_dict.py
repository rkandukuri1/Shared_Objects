cars_dict = {
    "brand" : "Toyota",
    "model" : "Camry",
    "year" : "2025",
    "color" : "Gray",
    "year" : "2021"
}

#print(cars_dict)
#print(cars_dict["model"])

students_dict = {
    "s1": {
        "id" : "101",
        "name" : "John",
        "Grade" : "9"
    },
    "s2" : {
        "id" : "102",
        "name" : "Smith",
        "Grade" : "11"
    },
    "s3" : {
        "id" : "103",
        "name" : "Steve",
        "Grade" : "9"
    }
}

print(students_dict)
print(students_dict["s2"] ["name"])
print("")

print ("======================")
for x, rcrd in students_dict.items():
    print(x)
    for y in rcrd:
        print("   " + y + " : " + rcrd[y])
print ("======================")

