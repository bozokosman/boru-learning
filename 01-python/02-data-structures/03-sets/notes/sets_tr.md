# Sets

> 🇹🇷 [Türkçe doküman için tıklayın](README.tr.md)

## 1. What is a Set?
A Set is a data type in Python used to store multiple values in a single structure.

The most important features of sets:
- Stores unique elements.
- Does not store the same element more than once.
- Does not support indexing.
- It is a mutable data structure.
- Supports mathematical set operations.

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

## 2. Creating a Set
Curly braces can be used to create a set.

```python
numbers = {10, 20, 30}
```
A set consisting of string values:
```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}
```

## 3. Duplicate Elements
A set does not store the same value more than once.

```python
numbers = {10, 20, 20, 30, 30, 30}

print(numbers)
```
As a result, each value is present only once. This feature is especially useful for cleaning up repetitive data.

## 4. Empty Set
You cannot use just `{}` to create an empty set.

```python
empty_set = set()
```
Because:
```python
empty = {}
```
creates an empty dictionary.

## 5. Adding Elements to a Set
To add a single element to a set, `add()` is used.

```python
books = {"Python101", "Clean Code"}

books.add("Computer Science")

print(books)
```

## 6. Adding Multiple Elements
To add multiple elements, `update()` can be used.

```python
books = {"Python101"}

books.update({
    "Clean Code",
    "Computer Science",
    "The Pragmatic Programmer"
})

print(books)
```
`update()` adds elements from an iterable to the set.

## 7. Removing Elements — remove()
To remove a specific element, `remove()` can be used.

```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}

books.remove("Clean Code")

print(books)
```
If the element is not in the set, `remove()` raises an error.

## 8. Removing Elements — discard()
`discard()` also removes an element. However, if the element is not in the set, it does not raise an error.

```python
books = {
    "Python101",
    "Clean Code"
}

books.discard("Computer Science")

print(books)
```
Therefore, the difference between `remove()` and `discard()` is important.

## 9. pop()
`pop()` removes an element from the set and returns the removed element.

```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}

removed_book = books.pop()

print(removed_book)
print(books)
```
Since sets are unordered and not indexed, you cannot rely on which element will be removed.

## 10. clear()
To remove all elements from a set, `clear()` is used.

```python
books = {
    "Python101",
    "Clean Code"
}

books.clear()

print(books)
```
Result:
```python
set()
```

## 11. len()
To find the number of elements in a set, `len()` can be used.

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

## 12. in
To check whether an element is present in a set, `in` can be used.

```python
books = {
    "Python101",
    "Clean Code"
}

print("Python101" in books)
print("C++" in books)
```

## 13. for Loop on a Set
A `for` loop can be used on a set.

```python
books = {
    "Python101",
    "Clean Code",
    "Computer Science"
}

for book in books:
    print(book)
```
Since the set is not indexed, a usage like this cannot be done:
```python
books[0]
```

## 14. Set Union
To combine all elements of two sets, the `union` operation can be used.

```python
python_books = {
    "Python101",
    "Python Advanced"
}

programming_books = {
    "Clean Code",
    "Python101"
}

result = python_books.union(programming_books)

print(result)
```
The `|` operator can also be used for the union operation.
```python
result = python_books | programming_books
```
Identical elements are present only once in the result.

## 15. Set Intersection
To find the common elements in two sets, `intersection` is used.

```python
python_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}

programming_books = {
    "Python101",
    "Clean Code",
    "C++"
}

result = python_books.intersection(programming_books)

print(result)
```
The `&` operator can also be used.
```python
result = python_books & programming_books
```

## 16. Set Difference
To find elements that are in one set but not in another, `difference` is used.

```python
python_books = {
    "Python101",
    "Clean Code",
    "Python Advanced"
}

programming_books = {
    "Python101",
    "C++"
}

result = python_books.difference(programming_books)

print(result)
```
The `-` operator can also be used.
```python
result = python_books - programming_books
```

## 17. Symmetric Difference
To find elements that are in either of the sets but not in both, `symmetric_difference` can be used.

```python
set1 = {
    1,
    2,
    3
}

set2 = {
    3,
    4,
    5
}

result = set1.symmetric_difference(set2)

print(result)
```
The `^` operator can also be used.
```python
result = set1 ^ set2
```
Result:
```python
{1, 2, 4, 5}
```

## 18. Set Comparisons
Sets can be compared with each other.

**issubset()**
Checks if a set is a subset of another set.
```python
small = {1, 2}
large = {1, 2, 3, 4}

print(small.issubset(large))
```

**issuperset()**
Checks if a set contains another set.
```python
large = {1, 2, 3, 4}
small = {1, 2}

print(large.issuperset(small))
```

**isdisjoint()**
Checks if two sets have a null intersection (no common elements).
```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}

print(set1.isdisjoint(set2))
```

## 19. Main Difference Between Set and List
**List:**
```python
books = [
    "Python101",
    "Clean Code",
    "Python101"
]
```
A list can store the same element more than once.

**Set:**
```python
books = {
    "Python101",
    "Clean Code",
    "Python101"
}
```
A set deduplicates repeating elements.

## 20. Creating a Set from a List
A set can be created from a list.

```python
numbers = [
    10,
    20,
    20,
    30,
    30,
    40
]

unique_numbers = set(numbers)

print(unique_numbers)
```
This method can be used to clear repetitive values.

## 21. Creating a List from a Set
A set can be converted back to a list.

```python
numbers = {10, 20, 30}

numbers_list = list(numbers)

print(numbers_list)
```

## 22. Difference Between Set and Dictionary
Because both can use `{}`, they can be confusing at first.

**Set:**
```python
books = {
    "Python101",
    "Clean Code"
}
```

**Dictionary:**
```python
book = {
    "name": "Python101",
    "author": "Osman Bozok"
}
```
A Set consists of values. A Dictionary consists of key: value pairs.

When creating an empty structure:
- `set()` creates an empty set,
- `{}` creates an empty dictionary.

## 23. Summary
**Set:**
- Stores unique elements.
- Removes duplicate values.
- Does not support indexing.
- Elements can be added with `add()`.
- Multiple elements can be added with `update()`.
- Elements can be removed with `remove()` and `discard()`.
- An element can be removed with `pop()`.
- `clear()` deletes all elements.
- `union()` combines two sets.
- `intersection()` finds common elements.
- `difference()` finds different elements.
- `symmetric_difference()` finds elements that are not common.
- `issubset()` checks for a subset.
- `issuperset()` checks for a superset.
- `isdisjoint()` checks for common elements.

Basic set creation:
```python
numbers = {1, 2, 3, 4}
```
Basic element addition:
```python
numbers.add(5)
```
Basic membership check:
```python
print(3 in numbers)
```
One of the most powerful use cases of sets is to clean repetitive values:
```python
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
```
