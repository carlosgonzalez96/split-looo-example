

import json

scorpions =  '{ "length":[0.9,21,1,10,21,5,18,4,15,2], "venom":[0.39,0.62,0.20,0.45,0.33,0.62,0.55,0.40,0.22,0.38]}'
scorpion_data = json.loads(scorpions)

def average_scorpion_length():
    average_length = reduce(lambda total,data: data+total, scorpion_data["length"])
    return average_length

def total_venom_extract():
    total_venom_amount = sum([i for i in scorpion_data["venom"] if i > 0.40])
    return total_venom_amount

print "Average length: " + str(average_scorpion_length()) + "cm" + "\n" + "Total amount of venom extracted: " + \
    str(total_venom_extract()) + "mg"
