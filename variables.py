"""
Topic: Variables
Source:
- Python Crash Course
- Corey Schafer

 starting Date: July 13, 2026
"""



# ==========================
# Strings
# ==========================

message='hello world'
print(message)
name=" kaniz ayesha "
print(name)


""" now for length of a string"""
print(len(message))
print(len(name))

"""for countig the number of characters in a string"""
print(message.count('m'))
print(message.count('l'))
print(message.count('w'))
print(message.count('hello'))
print(name.count('a'))
print(name.count('kaniz'))
print(name.count('khan'))

"""for finding the index of a character in a string"""
print(message.find('h'))
print(name.find('a'))
print(name.find('k'))
print(message.find ('universe'))
  
"""for accessing  the index number of character in a string"""
print(message[0:20])
print(name[0:8])
print(name[:14])
print(name[0: ])
print(message[0: ])

