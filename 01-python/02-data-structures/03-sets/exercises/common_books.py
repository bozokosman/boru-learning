programming_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}
computer_science_books = {
    "Python101",
    "Algorithms",
    "Computer Science"
}
def find_common_books(set1,set2):
    return set1 & set2
print(find_common_books(programming_books,computer_science_books))