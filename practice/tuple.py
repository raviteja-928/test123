t = (1, 2.5, 'hello', [4, 6])
print(list(t))
print(t[0])
print(t[-1])
print(t[:])

# t[1] = 2
# print(t)                     # TypeError: 'tuple' object does not support item assignment


# index()
# .......

t = (1, 2.5, 'hello', [4, 6])
print(t.index(2.5))

# count()
# .........

t = (1, 2.5, 'hello', [4, 6], 2.5, 1, 2.5)
print(t.count(2.5))

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)
print(t1 * 3)
print(len(t1))
print(max(t1))
print(3 in t1)
del t1
 
# print(t1)