# w.a.p to convert given list elements into string 

l = [1, 2, 3, 4]

# method 1
op = []
for i in l:
    op.append(str(i))
print(op)

# method 2
print([str(i) for i in l])

# method 3
print(list(map(str, l)))

# w.a.p to print vowels available in given string.

s = "Hello world"

# method 1
op = []
for i in s:
	if i in "aeiouAEIOU":
		op.append(str(i))
print(op)

# method 2
print([str(i) for i in s if i in "aeiouAEIOU"])

# method 3
def vowels(s):
	for i in s:
		if i in "aeiouAEIOU":
			return i

print(list(filter(vowels, "Hello world")))

# w.a.p to get employees salory with 10% hike 

s = '''E1 IBM 15000 Banglore
       E2 hp 16000 Chennai
       E3 IBM 17000 Hyderabad'''

# method 1
op = []
for i in s.split():
	if i.isdigit():
		op.append(i)
print(op)
for m in range(len(op)):
	d = int(op[m])
	d += int(d/10)
	op[m] = str(d)
print(op)
	



l = [15000, 16000, 17000]
for i in range(len(l)):
	l[i] += int(l[i]/10)
print(l)

l = ['15000', '16000', '17000']
for i in range(len(l)):
	d = int(l[i])
	d += int(d/10)
	l[i] = str(d)
print(l)


	
# w.a.p to reverse a list without using "reverse" function
l = [1, 2, 3, 4, 5, 6, 7]
def reverse(l):
	if (len(l) == 1):
		return l
	return reverse (l[1:]) + (l[0:1])
print(reverse(l))


print(str(l[::-1]))


# w.a.p to get salaries and employee names who are working
data = ''' Name1 Banglore 15000
           Name2 Chennai 12000
           Name3 Hyderabad 16000
           Name4 Banglore 20000
           Name5 Chennai 30000
           Name6 Banglore 40000'''
op = []

for i in data.split():
	if i.isdigit():
		op.append(i)
print(op)
for i in range(len(op)):
	d = int(op[i])
	d += int(d/30)
	op[i] = str(d)
print(op)


op = []
def get_employee(data, location):
	for i in data.splitlines():
		if location in i:
			op.append(i)
	return op

print(get_employee(data, 'chennai'))

res=data.splitlines()
print(res)



def get_employee(data, location):
	op = [row.split() for row in data.splitlines() if location in row]
	return op
print(get_employee(data, "chennai"))



# w.a.p to get adjacent numbers in the given string
s = "A1234b56cd789x100"
def adjacent(s):
	op = []
	for i in s.split('b'):
		if i.isalnum():
			op.append(i)
	return op
print(adjacent(s))



# w.a.p to read the above json(JavaScriptObjectNotation) file and print emp_name and age of them

'''import json

data.json
{'Ravi':{'age':20, 'salary':1000},
 'kiran':{'age':25, 'salary':2000},
 'Raju':{'age':27, 'salary':3000},
 'Manoj':{'age':28, 'salary':4000}}
emp = json.loads(data.json)
print(emp('Ravi'))


# read the given "URL" and print all image names it(webscrapping) URL:www.python.org

import requests
from bs4 import BeautifulSoup

def getdata(url):
	r = requests.get(url)
	return r.text
htmldata = getdata("https://www.python.org/")
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    print(item['src'])


# w.a.p. to find square root of given number

x = int(input("Enter a number:"))
z = x * x
print(z)'''


# w.a.p to print the current date, time and day of the week

from datetime import date
today = date.today()
print(today)

from datetime import datetime
now = datetime.now()
print(now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)



# w.a.p to print the combination where sum is 11


from itertools import combinations

l = [1, 8, 4, 6, 7, 2, 9, 3]
def pairs(l):
	op = []
	for m in combinations(l, 2):
		if m[0] + m[1] == 11:
			op.append((m[0], m[1]))
	return op
print(pairs(l))


from itertools import combinations

l = [1, 8, 4, 6, 7, 2, 9, 3]
k = 11
def pairs(l, k):
	op = []
	for m in combinations(l, 2):
		if m[0] + m[1] == k:
			op.append((m[0], m[1]))
	return op
print(pairs(l, k))


from itertools import combinations

def pairs(l, k):
	op = []
	for m in combinations(l, 2):
		if m[0] + m[1] == k:
			op.append((m[0], m[1]))
	return op

l = [1, 8, 4, 6, 7, 2, 9, 3]
k = 11
print(pairs(l, k))


# method2

from itertools import combinations
def pairs(l, k):
	op = [m for m in combinations(l, 2) if sum(m) == k]
	return op

l = [1, 8, 4, 6, 7, 2, 9, 3]
k = 11

print(pairs(l, k))










