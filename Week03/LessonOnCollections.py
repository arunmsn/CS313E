"""Methods of Lists"""
my_list = [1, 50, 23, 12, 2]
my_list.sort()
my_list.reverse()
print(my_list)

my_list.pop(2)
print(my_list)


"""List Comprehension"""
new_list = [(i*5) for i in my_list]
print(new_list)

a = [1, 2, 3, 4, 5, 6]
b = [1, -2, 3, -6]

# The slower method
p = []
for item in b:
    if item in a:
        p.append(item)
    else:
        p.append(1000)
print(p)

# The faster method
c = [item if item in a else 1000 for item in b]
print(c)


"""Working with Tuples"""
# Tuples are the immutable (elements cannot be changed/updated) version of lists
coord = (7.3, 2.9)
employee_record = ('john', 'doe', '123 Any Street', 'Austin', 'TX')
print(employee_record)

new_list = list(employee_record)
print(new_list)


"""Working with Sets"""
# Sets are unordered, but will not allow any duplicates
# Sets are mutable
a = [1,2,1,4,3,2,4,3,1,2,3,4,1,2,3,4,3,2,4,1,2,3]
b = set(a)
print(b)

# Set Theory
d = set('aaabbbccddddeeffff')
f = set('bbccddff')
print(d.union(f))
print(d.intersection(f))


"""Working with Dictionaries"""
# This is a collection of key-value pairs
# While the Dictionary itself is mutable, the keys are not
phone_book = {}
phone_book['Mickey Mouse'] = '123-456-7890'
phone_book['Donald Duck'] = '987-654-3210'
for key in phone_book:
    print(key, phone_book[key])