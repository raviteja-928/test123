# indexing
# ..........

s = "hello welcome to my world"
print(s[1])                        # e
print(s[5])                        #  
print(s[-1])                       # d


# slicing
# ..........

s = "hello welcome to my world"
print(s[1: 25: 2])                # el ecm om ol
print(s[: : -1])                  # dlrow ym ot emoclew olleh


# len
# .......

s = "hello welcome to my world"
print(len(s))                      # 25


# capitalize()
# ............

s = "hello welcome to my world"
print(s.capitalize())                   # Hello welcome to my world


# upper()
# .......

s = "hello welcome to my world"
print(s.upper())                        # HELLO WELCOME TO MY WORLD


# lower()
# .......

s = "hElLo wElcome to my world"
print(s.lower())                       # hello welcome to my world


# title()
# .......

s = "hello welcome to my world"
print(s.title())                        # Hello Welcome To My World


# swapcase()
# ..........

s = "helLo WElcomE To My WORLd"
print(s.swapcase())                     # HELlO weLCOMe tO mY worlD


# isalpha()
# ............

s = "Hello Welcome To My World"
print(s.isalpha())                      # False


# isdigit()
# .......

s = "12345.678"
print(s.isdigit())                     # False


# isalnum()
# .........

s = "hello welcome to my world 123"
print(s.isalnum())                     # False

s = "hellowelcometomyworld123"
print(s.isalnum())                     # True


# isspace()
# ..........

s = " "
print(s.isspace())    # True
s = "\n"
print(s.isspace())    # True
s = "\t"
print(s.isspace())    # True
s = "hello welcome"
print(s.isspace())    # False


# istitle()
# .........

s = "hello welcome to my world"
print(s.istitle())                 # False
s = "Hello Welcome To My World"
print(s.istitle())                 # True


# islower()
# .........

s = "hello welcome to my world"
print(s.islower())                 # True


# isupper()
# .........

s = "hello welcome to my world"
print(s.isupper())                 # False


# zfill()
# .......

s = "hello welcome to my world"
print(s.zfill(30))                  # 00000hello welcome to my world


# center()
# ..........

s = "hello welcome to my world"
print(s.center(30))                #   hello welcome to my world   
print(s.center(30, '@'))           # @@hello welcome to my world@@@
print(s.center(20,'@'))                # hello welcome to my world


# ljust()
# .......

s = "hello welcome to my world"
print(s.ljust(30, '@'))           # hello welcome to my world@@@@@


# rjust()
# .......

s = "hello welcome to my world"
print(s.rjust(30, '@'))           # @@@@@hello welcome to my world


# count()
# .......

s = "hello welcome to my world"
print(s.count('l'))               # 4
print(s.count('l', 1, 10))        # 3


# replace()
# .........

s = "hello welcome to my world"
print(s.replace('l','@'))         # he@@o we@come to my wor@d
print(s.replace('l', '@', 2))     # he@@o welcome to my world


# index()
# .......

s = "hello welcome to my world"
print(s.index('l'))               # 2
print(s.index('l', 5, 20))        # 8
# print(s.index('@'))               # ValueError: substring not found


# rindex()
# ........

s = "hello welcome to my world"
print(s.rindex('l'))              # 23
print(s.rindex('l', 5, 20))       # 8


# find()
# ......

s = "hello welcome to my world"
print(s.find('l'))               # 2
print(s.find('l', 5 , 20))       # 8
print(s.find('@'))               # -1


# rfind()
# .......

s = "hello welcome to my world"
print(s.rfind('l'))              # 23
print(s.rfind('l', 5, 20))       # 8


# startswith()
# ............

s = "hello welcome to my world"
print(s.startswith('h'))          # True
print(s.startswith('@'))          # False
print(s.startswith('w', 7, 10))   # False


# endswith()
# ...........

s = "hello welcome to my world"
print(s.endswith('d'))            # True
print(s.endswith('e', 0, 10))     # False


# split()
# .......

s = "hello welcome to my world"
print(s.split(' '))               # ['hello', 'welcome', 'to', 'my', 'world']
print(s.split('e'))               # ['h', 'llo w', 'lcom', ' to my world']
print(s.split('e', 2))            # ['h', 'llo w', 'lcome to my world']


# rsplit()
# --------

s = "apple, banana, mango"
print(s.rsplit(", "))             # ['apple', 'banana', 'mango']
print(s.split(", ", 1))           # ['apple', 'banana, mango']


# splitlines()
# ...........

s = "hello\n welcome to my world"
print(s.splitlines())               # ['hello', ' welcome to my world']
print(s.splitlines(True))           # ['hello\n', ' welcome to my world']


# join()
# .............

l = ['hello', '1223', 'welcome']
print("@".join(l))                  # hello@1223@welcome
# l = ['hello', 1223, 'welcome']
# print("$".join(l))                  # TypeError: sequence item 1: expected str instance, int found


# strip()
# .........

s = "hello welcome to my world"
print(s.strip('h'))                # ello welcome to my world
print(s.strip('d'))                # hello welcome to my worl
print(s.strip())                   # hello welcome to my world

s = "@@hello welcome to @ my world@@"
print(s.strip('@'))                    # hello welcome @ to my world


# lstrip()
# .........

s = "@@hello welcome to @ my world@@"
print(s.lstrip("@"))                    # hello welcome to @ my world@@


# rstrip()
# ........

s = "@@hello welcome to @ my world@@"
print(s.rstrip("@"))                   # @@hello welcome to @ my world


# format()
# .........

s = "hello my name is {fname}, i am {age}"
print(s.format(fname = "RaviTeja", age = '29'))     # hello my name is RaviTeja, i am 29

s = "hello my name is {0}, i am {1}"
print(s.format("RaviTeja", 29))                     # hello my name is RaviTeja, i am 29

s = "hello my name is {}, i am {}"
print(s.format("RaviTeja", 29))                     # hello my name is RaviTeja, i am 29

s = "{0} is an integer and {1} is an float"
print(s.format(10, 10.8))

# encode()
# ...........

s = "hello welcome to my world"
print(s.encode())                     # b'hello welcome to my world'

s_en = s.encode("utf-32")
print(s_en)

# decode()
# ...............

print(s_en.decode("utf-32"))         # hello welcome to my world


# basic operations
# ................

s1 = "Hello Python"
s2 = "Welcome To WORLd"

print(s1 + s2)             # Hello PythonWelcome To WORLd
print(s1 * 2)              # Hello PythonHello Python

print(max(s1))             # y
print(min(s2))             #  
print(s1[6])               # P
print('P' in s1)           # True
for letter in s1:
	print(letter)
	print(letter, end=' ')
for i in range(len(s1)):
	print(s1[i])


print(s.startswith('w', 6, 10))   # True