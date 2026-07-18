"""
===========================================
        PYTHON CRASH COURSE EXERCISES
===========================================

📚 Book: Python Crash Course (3rd Edition)
👨‍💻 Chapter: Variables and Simple Data Types
📝 File: variables_exercises.py
🎯 Purpose: Solutions to the "Try It Yourself" exercises.

Author: Kaniz Ayesha
Date Started: July 15, 2026

===========================================
"""

'''TRY IT YOURSELF EXERCISES'''
"""===2-1==="""
name='kaniz ayesha'
print(name)
message='hello world' 

"""===2-2==="""
print(message)
message="my nam is ayesha"
print(message)
  
"""===2-3==="""
name="eric"
message="hello"+ "," +name.title() + "." +"would u like to learn some python today?"
print(message)
"""other methods"""
print(f"hello,{name.title()}.would u like to learn soe python today?")
name="eric".title()
print("hello.", name , ".would u like to learn some python today?")

"""===2-4==="""
person="ALi"
print(person.title())
print(person.lower())
print(person.upper())

"""===2-5==="""
print("Might Guy  once said:  'All the effort is pointless, if you don't believe in yourself'")
"""other methods"""
print("Might Guy  once said: \"All the effort is pointless, if you don't believe in yourself\"")

"""===2-6==="""
famous_person="Might Guy"
quote="All the effort is pointless, if you don't believe in yourself"
print(famous_person, " once said: ", quote)
"""other methods"""
print("{} once said: {}".format(famous_person,quote))
print("{} once said: {}".format(famous_person,quote.upper()))

"""===2-7==="""
person="  itachi uchiha  "
print(person)
print(person.lstrip() )
print(person.rstrip())
print(person.strip())

"""===2-8==="""
print("the answer of addition is:",5+3)
print("the answer of subtraction is:",12-4)
print("the answer of multiplication is:",2*4)
print("the answer of division is:",16/2)

"""===2-9==="""
favnum=56
message="my fav number is:" +  str(favnum)
print(message)
print("my fav number is:" + str(favnum))