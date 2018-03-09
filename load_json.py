import json

# Create demo json
text_json = '''{
   "demo": "Demo data for JSON in Python",
   "author": "Ardian",
   "date": 2018
}'''

# Print the type of the demo JSON and the content
print(type(text_json), text_json)

# Convert JSON to a Python dict
data = json.loads(text_json)

# Print type of data and content, now as a dict
print(type(data), data)

# Getting the value of the key author and saving it to a variable
# author, if empty use 'Da Vinci'
author = data.get('author', 'Da Vinci')

# Print author
print("Your instructor is {}".format(author))

# Change the value of the dict
data['author'] = 'Mike'

# Convert from dict to JSON
new_json = json.dumps(data)

# Print the type of the new_json and the content
print(type(new_json), new_json)
