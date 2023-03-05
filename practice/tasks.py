# w.a.p to get adjacent numbers in the given string
'''s = "A1234b56cd789x100"
op = []
for i in range(len(s)):
	res=''
	if s[i].isdigit():
		res+=s[i]
		op.append(i)
print(op)'''


from itertools import combinations

l = [1, 8, 4, 6, 7, 2, 9, 3]
def pairs(l):
	op = []
	for m in combinations(l, 2):
		if m[0] + m[1] == 11:
			op.append((m[0], m[1]))
	return op
print(pairs(l))



# w.a.p to get adjacent numbers in the given string

s = "A1234 b56cd789x100"

def adjacent(s):
	op = []
	for m in s:
		if m.isdigit():
			op.append(m)
	return op
print(adjacent(s))

s = "A1234b56cd789x100"

def adjacent(s):
	op = []
	prev = s[0]                                  # previous
	sub = s[0] if s[0].isdigit() else ''

	for m in s[1:]:
		if prev.isdigit() and m.isdigit():
			sub += m

		else:
			if sub.isdigit():
				op.append(sub)
			prev = m
			sub = m
	op.append(sub)

	return op

print(adjacent(s))



# w.a.p to get the adjacent number combinations, where sum is 11
s = '13748326543'
op = []
for m in range(len(s)-1):
	if int(s[m]) + int(s[m+1]) == 11:
		op.append(tuple(s[m]) + tuple(s[m+1]))
	
print(op)

# method2

op = [tuple(s[m]) + tuple(s[m+1]) for m in range(len(s) -1 ) 	if int(s[m]) + int(s[m+1]) == 11]
print(op)


# method3
def adjacent(s, k):
	op = []
	for m in range(len(s) - 1):
		if int(s[m]) + int(s[m + 1]) == k:
			op.append(list(s[m:m+2]))
	return op
s = '13748326543'
k = 11
print(adjacent(s, k))


def adjacent(s, k):
	op = []
	for m in range(len(s) - 1):
		if int(s[m]) + int(s[m + 1]) == k:
			op.append((int(s[m]) , int(s[m + 1])))
	return op
s = '13748326543'
k = 11
print(adjacent(s, k))



# Read "valuesequence_new.csv" using either csv/pandas module 
# create a new csv, with records which are having "status == 1"
# create a new csv, with records which have the fine greater than "1000Bs"

# w.a.p. to convert a python file into executable file

'''import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("tasks.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
    name = "Tasks",
    options = {"build_exe": {"packages":["tkinter"], "include_files":["icon.ico"]}},
    version = "3.10.7",
    description = "YourAppDescription",
    executables = executables
)'''





# w.a.p to list the country names which have morethan 3 characters

countries = ["India", "Russia", "China", "USA", "PAK", "UK"]
print(len(countries))
print(countries[0].count('I'))



op = []
length = 3

for i in countries:
	if len(i) > length:
		op.append(i)

print(op)


# w.a.p to create a dictionary which contains country names as keys and length of the name as value 

print({i: len(i) for i in countries})






from datetime import datetime, date

today = date.today()

print(today)

now = datetime.now()
print(now)


l = [1, 2, 3, 4]
op = []
for i in l:
	op.append(str(i))
print(op)


data = '''PRODUCT_ID  @  BATCH_CODE  @  NAME        @  PRICE
          12345I      @  2348        @  SHAMPOO     @  52.8
          A867        @  1234        @  CLINICPLUS  @  2.8
          N215        @  8123        @  COLGATE     @  26.5
          28X2        @  6200        @  SANTOOR     @  30.0'''


# w.a.p to print the product details of given batch_code
batch_code = input("Enter BATCH_CODE: ")

data_split = data.split('\n')
header = data_split[0].split(' @ ')
details = {}

for i in data_split[1:]:
	data_split_1 = i.split(' @ ')

	product_id, bat_code, name, price = fields
	details[bat_code.strip()] = {'PRODUCT_ID' : product_id.strip(),
	                             'NAME': name.strip(),
	                             'PRICE': price.strip()}

if bat_code in details:
	print("The header part is:", bat_code)
	print("The PRODUCT_ID is:", PRODUCT_ID)
	print("Name is:", NAME)
	print("Price is:", PRICE)

else:
	print("The BATCH_CODE is not in range")











