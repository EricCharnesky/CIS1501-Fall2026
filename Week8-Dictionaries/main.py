gradebook = { "Jeb" :
                  {'Test1' :
                       { 'Points Possible' : 25,
                         'Points Earned': 25 },
                   'Project1' :
                       {'Points Possible' : 15,
                         'Points Earned': 12 }},
              'Vivi' :{'Test1' :
                       { 'Points Possible' :25,
                         'Points Earned': 20 },
                   'Project1' :
                       {'Points Possible' : 15,
                         'Points Earned': 15 }}}

for student in gradebook:
    for assignment in gradebook[student]:
        print(
            f"{student}'s score on {assignment} "
            f"is: {gradebook[student][assignment]['Points Earned'] 
                   / gradebook[student][assignment]['Points Possible'] 
                   * 100}%")

athletes = {
    "Tom Brady" : 12,
    "Michael Jordan" : 23,
    "Messi" : 11
}

# update if the key exists
athletes["Messi"] = 10

# add if the key doesnt' exist
athletes["Ronaldo"] = 7

for name in athletes:
    print(f"{name} wears jersey #{athletes[name]}")

name = 'Ronado'

# instead of crashing like this
# print(f"Ronadlo's number is {athletes[name]}")


print(f"Ronadlo's number is {athletes.get(name,"not found")}")

# in only looks for keys in dictionaries
if name in athletes:
    print(f"Ronadlo's number is {athletes[name]}")

athletes.pop("Messi")

print(athletes)

for name, number in athletes.items():
    print(f'{name} wears #{number}')


