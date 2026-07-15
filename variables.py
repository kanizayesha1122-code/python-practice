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
name="kaniz ayesha"
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
print(name[6])
print(message[10])

"""for changing the format of a strig"""
print(message.lower())
print(message.upper())
print(name.upper())
print(name.lower())

"""for changng characters in a string"""
new_message= message.replace('world','universe')
new_name=name.replace('kaniz ayesha','sohaib inam')
print(new_message)
print(new_name)
print(message)
print(name)
 
"""for connecting number of variables together"""
greeting="hey,how u doing?"
GUEST='humaira'
print(greeting+ ' ' +GUEST+ "  I AM SO HAPPY TO SEE YOU.I AM " + name )

introduction= greeting+" "+ GUEST+" i am happy to meet u today.i am "+ name
print(introduction)
introductin2=  '{} {}  i am happy to meet u today.i am  {}' .format(greeting,GUEST,name)
print(introductin2)
print(introduction)
print('{} {} i am {}.'.format(greeting,GUEST,name))
print(f'{greeting} {GUEST} i am {name}.it is so nice to meet u today')

"""for printing a strin with more quotations"""
print("hey.how u doing? john's friend is here")
print('hey how u doing ?john \'s family is over here too')
  

"""for  finding the number of methods we can apply on a string"""
print(dir(name))
print(dir(message))

"""for finding the way hw a method works on a string"""
print(help(str))


"""for finding one secific method and how it works"""
print(help(str.find))
print(help(str.format))
print(help(str.replace))
print(help(str.lower))
print(help(str.upper))
  

"""parameters that tells the print function how to display the output"""  
print("hell0","world",sep=' ..... ') 
print("hell0","friend",end= ',ali\n') 
print(' how are u?')

print("hello","jules",sep="\n")
print("ohh im am studing python lately",end=' ')
print("i am enjoying it a lot")