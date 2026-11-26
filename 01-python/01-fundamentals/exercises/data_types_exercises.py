name = "Osman" 
age = "32" 
print(age, type(age)) #32 <class 'str'>
age = 32
height = 95.5
is_learning = True
books = ["python101", "computer science", "developer101"]
coordinates = (123.321, 456.654)
book = {"name" : "Python101",
        "author" : "Osman Bozok",
        "page" : 5000}
result = None

print(name, type(name)) #Osman <class 'str'>
print(age, type(age)) #32 <class 'int'>
print(height, type(height)) #95.5 <class 'float'>
print(is_learning, type(is_learning)) #True <class 'bool'>
print(books, type(books)) #['python101', 'computer science', 'developer101'] <class 'list'>
print(coordinates, type(coordinates)) #(123.321, 456.654) <class 'tuple'>
print(book, type(book)) #{'name': 'Python101', 'author': 'Osman Bozok', 'page': 5000} <class 'dict'>
print(result, type(result)) #None <class 'NoneType'>