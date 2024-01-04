import json
with open('./Chatbot/database.json','r') as file:
    db = json.load(file)
with open('./Chatbot/intents.json','r') as file:
    intents = json.load(file)
with open('./Chatbot/state_vector.json','r') as file:
    states = json.load(file)

# res = intent['responses'][0].format(slots[1],db[slots[0]][slots[1]])
# print(intents['intents'][0]['responses'][0])

