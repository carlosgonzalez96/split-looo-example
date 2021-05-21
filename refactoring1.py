import json

# length: cm, venom: mg
scorpions =  '{ "length":[0.9,21,1,10,21,5,18,4,15,2], "venom":[0.39,0.62,0.20,0.45,0.33,0.62,0.55,0.40,0.22,0.38]}'
scorpion_data = json.loads(scorpions)

total_venom_amount = 0
average_length = 0

for data in range(10):
    average_length += scorpion_data["length"][data]
    if scorpion_data["venom"][data] > 0.40:
        total_venom_amount += scorpion_data["venom"][data]

average_length = average_length / len(scorpion_data["length"])

print "Average length: " + str(average_length) + "cm"
print "Total amount of venom extracted: " + str(total_venom_amount) + "mg"
