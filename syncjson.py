import json

# read file
with open('servoPos.json', 'r') as servoPos:
    data = servoPos.read()

# parse file
obj = json.loads(data)

print(obj)
obj['servoOne'] = 60
obj['servoTwo'] = 0
obj['servoThree'] = 0
obj['servoFour'] = 0
obj['servoFive'] = 0
obj['servoSix'] = 0
with open('servoPos.json', 'w') as servoPos:
    json.dump(obj, servoPos)
