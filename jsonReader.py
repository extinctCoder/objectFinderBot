import json

# read file
with open('servoPos.json', 'r') as servoPos:
    data = servoPos.read()

# parse file
obj = json.loads(data)

# show values
print("usd: " + str(obj['servoOne']))
print("eur: " + str(obj['servoTwo']))
print("gbp: " + str(obj['servoThree']))

obj["servoOne"] = 50
with open('servoPos.json', 'w') as servoPos:
    json.dump(obj, servoPos)
