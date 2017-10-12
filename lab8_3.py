#! python
# coding: utf-8

def avg(a):
	return sum(a) / len(a)
	
def med(a):
	
	if len(a)%2 == 0:
		return ((a[int(len(a)/2)]-1) + (a[int(len(a)/2)])/2)
	else:
		return a[int(len(a)/2)]
		
listOne = [8,13,5,7,3,4,9,7,5,5,10,3,2]

listOne = sorted(listOne)
print(listOne)

print(avg(listOne))
print(med(listOne))