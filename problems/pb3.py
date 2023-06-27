
def youngest_student(students):
    # Get the maximum age from the values in the dictionary
    min_age = min(students.values())
    # Find the student(s) with the maximum age
    youngest_student = [name for name, age in students.items() if age == min_age]
    # Return the name of the first student in the list (assuming there is only one oldest student)
    return youngest_student[0]














    pass # TODO:


# students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
# print(youngest_student(students))  # Expected output: "Alice"
