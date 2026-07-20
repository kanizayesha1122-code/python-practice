"""===LISTS==="""

"""for assigning values to a list"""
num= [10,4,23,1,0,6,4,7,9,2,1]
courses=['biology','physics','chemistry','zoology','maths']
 
"""for printing values of a list"""
print(num)
print(courses)

"""for finding the length of a list"""
print(len(num))
print(len(courses))

"""for accessing the value at a certin index of the list+grabbing a range of values in a list+for grabbing the last value in a list"""
print(num[2])
print(num[0:])
print(num[2:])
print(num[:-1])
print(num[-1])
print(courses[2])
print(courses[0:])
print(courses[2:])
print(courses[:-1])
print(courses[-1])

"""modifying list using methods"""
 
"""for adding items to a list"""
 
 #AT THE END OF A LIST
courses.append('art')
print(courses)   #cant directly use this method in print function instead 1st append the value u want to and then print it.

courses.append('english')
num.append(100)
print(num)
print(courses) #useful for only adding one value at a time
courses2=['literature','sociology']
courses.append(courses2)
print(courses)
#if we want to add a number of items by dding 2nd list to 1st list it gives us a list within a list where these end one addded are on same index and doesnt act as individual items
#so append is best for adding ne element as an individual item to a list

#FOR INSERTING ITEMS ANYWHERE IN A LIST
courses.insert(0,'ls')
print(courses)
courses.insert(0,['library science','history'])
 #can even insert a list since it takes only 2 arguments one place other the value here these 2 values in the list are place on one index that is zero
num.insert(7,[28,33]) 
print(num)
num2=[29,34]
num.insert(0,num2)
print(num)

#FOR EXPANDING A LIST
courses_2=['education','cs']
courses.extend(courses_2)
print(courses)
#for printing the 2nd list as individual items

"""for removing values from a list"""
courses.remove(courses2)
print(courses)
#courses.remove(courses_2)
#print(courses)   gives us error because the items of courses_2 are added to list original using extend method which make these items individual elements of origial list so to remove them mention the separately 
#where the insert and extend nes must me mention separately only.while in append even mentioning the whole list makes the remove
courses.remove(['library science', 'history'])
print(courses) 
num.remove(num2)
print(num)
#bcz the 2nd list was initialized before insert so i simply wote the variable name savin that 2nd list and emove it
#however if a value is inserted directing within a list using method be it 2 or 3 together in a list as one argument i must then mention each separately or the ehole list if not declared separately
 
"""using pop"""
#for removing last item
courses.pop()
print(courses) #for removing the last item n a list.it pops it simply and prints the remainng elements
#now if we want to find the elements what is being popped simply declare a variable and save that pop walue to it
popped=num.pop()
print(num)
print(popped)

"""for reversing a list """
courses.reverse() #reverses the index number the last item become 1st
print(courses)
num.reverse()
print(num)

"""for sorting a list acc to alphabet and ascending order"""
courses.sort()
print(courses)

#num.sort()
#print(num)
#the raeason why i am getting this error is because my list contains another lst so it donts know were to put that inner second list in the main list
#  File "c:\Users\kaniz\pythonselfpractice\lists.py", line 93, in <module>
#    num.sort()
 #   ~~~~~~~~^^
#TypeError: '<' not supported between instances of 'list' and 'int'

#only a normal list can be sorted [1, 2, 9, 7, [28, 33], 4, 6, 0, 1, 23, 4, 10] this wrong
numb=[22,3,66,13,0,90,66,45,44,1,4,7]
numb.sort()
print(numb)
 
"""for sorting in descending"""
#1st sort then reverse
numb.sort()
numb.reverse()
print(numb)
"""===method 2==="""
#sorting without affecting original items seqesnce of list
#use sort function and return its value to a variable rather than directly using method on a list and altering original data
courses3=['bio','geo','zoology','arts']
sorted_courses3=sorted(courses3)
print("sorted using function for courses3",sorted_courses3)
#pint original to check if original is affected
print("the orignal courses3",courses3)

"""using build in functions"""
"""===max,sum,min==="""
print(min(numb))
print(max(numb))
print(sum(numb))

"""looping"""
