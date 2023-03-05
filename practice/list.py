l = [1, 2, 3, "hello"]
print(len(l))            # 4
# print(max(l))          # TypeError: '>' not supported between instances of 'str' and 'int'
print(l * 2)             # [1, 2, 3, 'hello', 1, 2, 3, 'hello']

l = [1, 2, 3, "hello"]
l1 = [1, 1.8, "string"]
print(l + l1)              # [1, 2, 3, 'hello', 1, 1.8, 'string']
# print(l * l1)            # TypeError: can't multiply sequence by non-int of type 'list'

l2 = [1, 10, 30.3]
l3 = [1.5, 20, 22]
# print(l2 * l3)            # TypeError: can't multiply sequence by non-int of type 'list'

l2 = [1, 10, 30]
l3 = [1, 20, 22]
# print(l2 * l3)           # TypeError: can't multiply sequence by non-int of type 'list'


l = [1, -1, 0, -3]
print(max(l))            # 1
print(min(l))            # -3
print(l[:])              # [1, -1, 0, -3]


# updating
# ..........

l = [1, 1.8, "string"]
l[1] = 2.0
print(l)                 # [1, 2.0, 'string']

# deleting
# .........

del l[1]
print(l)                 # [1, 'string']


# append()
# .........

l = [1, 2, "Hello", "Python", 3.0, 4.4]
l.append("5")
l.append(6.6)
l.append((1, 2))
print(l)             # [1, 2, 'Hello', 'Python', 3.0, 4.4, '5', 6.6, (1, 2)]


# extend()
# ..........

l = [1, 2, "Hello", "Python", 3.0, 4.4]
l.extend(("5", 6.6, (1, 2)))
print(l)                                   # [1, 2, 'Hello', 'Python', 3.0, 4.4, '5', 6.6, (1, 2)]
l.extend("world")
print(l)                                   # [1, 2, 'Hello', 'Python', 3.0, 4.4, '5', 6.6, (1, 2), 'w', 'o', 'r', 'l', 'd']


# insert()
# ...........

l = [1, 2, "Hello", "Python", 3.0, 4.4, (1, 2)]
l.insert(3, "welcome")
print(l)                                  # [1, 2, 'Hello', 'welcome', 'Python', 3.0, 4.4]

# pop()
# .......

l = [1, 2, "Hello", "Python", 3.0, 4.4]
print(l.pop(4))                          # 3.0
print(l)                                 # [1, 2, 'Hello', 'Python', 4.4]


# remove()
# .........

l = [1, 2, "Hello", "Python", 3.0, 4.4]
l.remove(4.4)
print(l)                                 # [1, 2, 'Hello', 'Python', 3.0]


# reverse()
# ..........

l = [1, 2, "Hello", "Python", 3.0, 4.4]
l.reverse()
print(l)                                  # [4.4, 3.0, 'Python', 'Hello', 2, 1]

'''l = [1, 2, Hello, "Python", 3.0, 4.4]
l.reverse()
print(l)'''                                  # NameError: name 'Hello' is not defined


# clear()
# .........

l = [1, 2, "Hello", "Python", 3.0, 4.4]
l.clear()
print(l)                                   # []


# copy()
# ........

l = [1, 2, "Hello", "Python", 3.0, 4.4]
l.copy()
print(l)                                   # [1, 2, 'Hello', 'Python', 3.0, 4.4]


# sort()
# ........

l = [1, 2, 9, -1, 5, -5, 0, 4]
l.sort()
print(l)                                  # [-5, -1, 0, 1, 2, 4, 5, 9]
l.sort(reverse = True)
print(l)                                  # [9, 5, 4, 2, 1, 0, -1, -5]

'''l = [1, 2, "Hello", "Python", 3.0, 4.4]
l.sort()
print(l)'''                                   # TypeError: '<' not supported between instances of 'str' and 'int'


# index()
# .......

l = [1, 2, "Hello", "Python", 3.0, 4.4]
print(l.index(3.0))                        # 4


# count()
# ........

l = [1, 2, "Hello", "Python", 3.0, 4.4, 5, 5]
print(l.count(3.0))                              # 1
print(l.count(5))                                # 2



# shallow copy:
# ------------

# The process of copying memory location from one variable to another variable known as shallow copy.
'''shallow copy provides two major properties they are:
   1) Multiple variable should share the same memory location.
   2) If the content of one variable has changed other will get modified.
   Note:
   Mutaable objects obeys the shallow copy properties completly but immutable objects obeys then partially'''

# shallow copy on mutable objects
l = [1, 2, 3]
print(id(l))
l = l1
print(id(l1))
l[1] = 100
print(l)
print(l1)

# shallow copy on immutable objects
t = (1, 2, 3)
print(id(t))
t1 = t
print(id(t1))
t = (1, 100 ,3)
print(t)
print(t1)
print(id(t))
print(id(t1))

# Deep Copy():
# -------------

# The process of copying the value from one variable to another variable is known as Deep Copy.
# When we perform deep copy the memory location of multiple variables will be different.
# To perform deep copy we can use slicing or copy function on mutable object but immutable objects doesnot support deep copy.
'''Deep copy provides two major properties they are
   1) The multiple variable should have same values but not their memory location'''

# on mutable objects:
# -------------------

l = [1, 2, 3]
l1 = l[::] or l.copy()
print(l1, id(l1))
print(l, id(l))
l[1] = 100
print(l, id(l), l1, id(l1))

# on immutable objects
# --------------------

t = (1, 2, 3)
t1 = (t[::])
print(t, id(t), t1, id(t1)) 