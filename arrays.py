courses =["MIT","Cybersecurity","Datascience"]
print(courses)

#Accessing an element

print(courses[2])


# Looping through an array
for x in courses :
    print("Course is",x)

# Adding an new element into an array
courses .append("Laravel")
print(courses)

# Removing an element to an array
courses.remove("Cybersecurity")