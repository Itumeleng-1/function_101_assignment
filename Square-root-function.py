

#Creating square-root function and calculating differences with the in-built math functions

def  mysqrt( a, x , e):
	""" Estimates the square root of a selected number 'a' from an initial estimate 'x', that is within an epsilon 'e' error margin"""
	while True:
		print(x)
		y = ( x + a/x)/2
		if  abs(y -x) < e:
			break
		x = y

	#Rest of table values (non-tabular form)	
	Difference = x - math.sqrt(a)
	print('square root estimate is ', x)
	print('actual square-root is ', math.sqrt(a))
	print('Difference is ', Difference)



#Static Prototype of the real deal

def  table():
        header = 'a\t|\tmysqrt(a, x, e)\t|\tmath.sqrt(a)\t|\tDifference'
        print(header)
        print('---' * len(header))
        print('1.0' + '\t|\t' + '1.0' + '\t\t|\t' + '1.0' + '\t\t|\t' + '0.0')
        print('2.0' + '\t|\t' + '1.41421356237' + '\t|\t' + '1.41421356237' + '\t|\t' + '2.22044604925e-16')
        print('3.0' + '\t|\t' + '1.73205080757' + '\t|\t' + '1.73205080757' + '\t|\t' + '0.0')
        print('4.0' + '\t|\t' + '2.0' + '\t\t|\t' + '2.0' + '\t\t|\t' + '0.0')
        print('5.0' + '\t|\t' + '2.2360679775' + '\t|\t' + '2.2360679775' + '\t|\t' + '0.0')
        print('6.0' + '\t|\t' + '2.44948974278' + '\t|\t' + '2.44948974278' + '\t|\t' + '0.0')
        print('7.0' + '\t|\t' + '2.64575131106' + '\t|\t' + '2.64575131106' + '\t|\t' + '0.0')
        print('8.0' + '\t|\t' + '2.82842712475' + '\t|\t' + '2.82842712475' + '\t|\t' + '4.4408920985e-16')
        print('9.0' + '\t|\t' + '3.0' + '\t\t|\t' + '3.0' + '\t\t|\t' + '0.0')


#Attempt at Dynamic working prototype
        

import math
def  table():
        header = 'a\t|\tmysqrt(a, x, e)\t|\tmath.sqrt(a)\t|\tDifference'
        print(header)
        print('---' * len(header))
        x=5
        e = 0.0000000000000001
        a = 9
        while a > 0:
                print(str(a) + '\t|\t' + str(mysqrt( a, x , e)) + '\t\t|\t' + str(math.sqrt(a)) + '\t\t|\t' + str(mysqrt( a, x , e) - math.sqrt(a)))
                break
                a = a -1






    
