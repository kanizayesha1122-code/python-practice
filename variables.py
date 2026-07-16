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
introduction='hey.nice t meet u.'.format( )
print(introduction)
introduction2='hey'+ ' nice to meet u.'
print(introduction2)

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
print("i am enjoying it a lot" )   
"""end is used to print the next line in the same line 
or putting the next line in the same line with a space 
or any other character we want to put in between the two lines.
sep is used to put any character we want to put in between the two lines."""


"""for converting the string in title format"""
book="python crash course"
favourite_anime="fullmetal alchemist brotherhood"
print(book)
print(book.title())
print(favourite_anime)
print(favourite_anime.title()) 

"""for converting the string in title format and combining strings"""
print(" my current is:",book.title() ," and my favourite anime is:", favourite_anime.title())
print(f"my current book is:  {book} and my favourite anime is: {favourite_anime}")
print(f"my current book is:  {book.lower()} and my favourite anime is: {len(favourite_anime)} characters long")
print(f"my current book is:  {book.title()} and my favourite anime is: {favourite_anime.title( )}")


"""adding whitespace to strings"""
print("book:\t"+ book.title())
print('my favourate animes are:\n\t'+favourite_anime)
print("the students in group are:\n\tsarah\n\tali\n\tnaina")
print("my best friends are:\n\tali\n\thumaira\n\tsarah ")

"""for stripping the whitespace in a string"""
friend='    ali  '
print(friend.rstrip())  #for removing the right whitespace temporarily
print(friend.lstrip()) #for removing the left whitespace temporarily
 
 #for permenently removing the white space simply store the value back into a new variable with this method
new_friend=friend.rstrip()
new_friend=friend.lstrip() 
print(new_friend)
print("  ali   ".rstrip())  
print("  ali   ".strip())  



# ==========================
# INTERGERS AND FLOAT
# ==========================


"""printing an int and float"""
num1=3
num2=11
num_1=30.9
num_2=20.5
print(num1)
print(num2)
print(num_1)
print(num_2)
 
"""===OPERATONS==="""
#addition
print(num1+num2)
print('the answer of addition is:',num1+num2)
print('the answer of  float addition is:',num_1+num_2)
#subtraction
print('the answer of subtraction is:',num1-num2)
print('the answer of float subtraction is:',num_1-num_2)
#multiplcation
print('the answer of multiplication is:',num1*num2)
print('the answer of float multiplication is:',num_1*num_2)
#division
print('the answer of division is:',num1/num2)
print('the answer of  float division is:',num_1/num_2)
#floor division
print('the answer of floor division is:',num1//num2)
print('the answer of floot floor division is:',num_1//num_2)
#exponents
print('the answer of exponents is:',num1**num2)
print('the answer of float exponents is:',num_1**num_2)
#modulus
print('the answer of modulus is:',num1%num2)
print('the answer of float modulus is:',num_1%num_2)

"""number of operations together"""
print(num1+num2-num_2)
print(num1*num_2/num2)
print(num1+(num2-num_2))
print((num1+num_2)/num2)
print(num1*(num_2/num2))