import pprint
# dictionaries dont have an order unlike lists
# functions in dictionary, keys(), values(), items()
# get() returns default value if key doesn't exist
# setdefault() sets a value if key doesn't exist

message= "This is a Sample text to show functioning of Dictionaries."
count= {}

for char in message.upper():
    count.setdefault(char, 0)
    count[char]+=1
# pprint.pprint(count)

string_text= pprint.pformat(count)      # pformat is used to convert it to a string
print(string_text)

print(type(message))
print(type(count))
print(type(23))