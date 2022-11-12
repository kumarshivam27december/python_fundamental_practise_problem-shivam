def display_student(name, group):
    print(name, group)

# call using original name
display_student("cypher","school")

# assign new name
showStudent = display_student
# call using new name
showStudent("shivam","student")