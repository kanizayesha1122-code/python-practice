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


