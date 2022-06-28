course = 'Python for Beginners'
print(len(course)) # 20
print(course.upper()) # PYTHON FOR BEGINNERS
print(course.lower()) # python for beginners
print(course.capitalize()) # Python for Beginners
print(course.isdigit()) # False
print(course.isalpha()) # False # contains a space
print(course.count("o")) # 2
print(course.find('Beginners')) # 11
print(course.replace('Beginners', 'Absolute Beginners')) # Python for Absolute Beginners
print('Python' in course) # True
print('python' in course) # False