'''Difference Between List and Array in Python
S.No.	List	                                                              Array
1	 List is used to collect items that usually consist of elements      An array is also a vital component that collects several
     of multiple data types.	                                            items of the same data type.
    
2	 List cannot manage arithmetic operations.	                        Array can manage arithmetic operations.
3	 It consists of elements that belong to the different data types.	It consists of elements that belong to the same data type.
4	 When it comes to flexibility, the list is perfect as                When it comes to flexibility, the array is not suitable
     it allows easy modification of data.                                as it does not allow easy modification of data.
	
5	 It consumes a larger memory.	                                    It consumes less memory than a list.
6	 In a list, the complete list can be accessed without                In an array, a loop is mandatory to access the 
     any specific looping.                                               components of the array.
               	
7	 It favors a shorter sequence of data.	                            It favors a longer sequence of data.'''



class A:
	def add(self, a, b):
		return a + b
class B(A):
	def add(self, a, b):
		o = super() or super(B, self)
		print(o)
		print(o.add(a, b))
		return a * b
obj = B()
print(obj.add(10, 20))
