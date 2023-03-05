d = {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6)}

print(type(d))                                                               # <class 'dict'>
print(id(d))                                                                 # 1969206309248

# accessing/ reading
# ..................

print(d['b'])                                                                # 10.5
print(d['f'])                                                                # (4, 5, 6)
print(d['d'][1])                                                             # 2


# updating an item
# .........

d['b'] = 20.5
print(d)                                                                   # {'a': 10, 'b': 20.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6)}


# deleting an item
# ...............

del d['c']
print(d)                                                                  # {'a': 10, 'b': 20.5, 'd': [1, 2, 3], 'f': (4, 5, 6)}

del d['d'][1]
print(d)                                                                 # {'a': 10, 'b': 20.5, 'd': [1, 3], 'f': (4, 5, 6)}

# insert an item
# ..............

d['g'] = 'welcome'
print(d)                                                                # {'a': 10, 'b': 20.5, 'd': [1, 3], 'f': (4, 5, 6), 'g': 'welcome'}


# keys()
# ......

d = {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6)}
print(d.keys())                                                         # dict_keys(['a', 'b', 'c', 'd', 'f'])

# values()
# ..........

print(d.values())                                                       # dict_values([10, 10.5, 'hello', [1, 2, 3], (4, 5, 6)])

# items()
# ........

print(d.items())                                                       # dict_items([('a', 10), ('b', 10.5), ('c', 'hello'), ('d', [1, 2, 3]), ('f', (4, 5, 6))])


# pop()
# ...........

d = {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6)}
print(d.pop('d'))                                                       # [1, 2, 3]
print(d)                                                                # {'a': 10, 'b': 10.5, 'c': 'hello', 'f': (4, 5, 6)}


# popitem()
# ..............

d = {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6)}
print(d.popitem())                                                       # ('f', (4, 5, 6))
print(d)                                                                 # {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3]}
# print(d.popitem('a'))                                                    # TypeError: dict.popitem() takes no arguments (1 given)


# get()
# ........

d = {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6)}
print(d.get('b'))                                                         # 10.5
print(d.get('x'))                                                         # None
print(d.get('x', 100))                                                    # 100
print(d)

# set default()
# ..............

d = {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6)}
print(d.setdefault('c'))                                                 # hello
print(d.setdefault('x'))                                                 # None
print(d.setdefault('y', 100))                                            # 100
print(d)                                                                 # {'a': 10, 'b': 10.5, 'c': 'hello', 'd': [1, 2, 3], 'f': (4, 5, 6), 'x': None, 'y': 100}



students = {'john': ['python', 'django', 'flask'], 'jakri':['java', 'javascript', 'spring'], 'jhonson':['dbs', 'sql', 'oracle']}
keys = students.keys()
for each_key in keys:
	print("courese are taken by", each_key, "are:")
	for each_course in students[each_key]:
		print(each_course)

students = {'john': ['python', 'django', 'flask'], 'jakri':['java', 'javascript', 'spring'], 'jhonson':['dbs', 'sql', 'oracle']}
values = students.values()
for each_value in values:
	print(each_value, "courses are taken by:")
	for each_key in students[each_value]:
		print(each_key)