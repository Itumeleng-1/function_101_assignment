

#Creating square-root function and calculating differences with the in-built math functions

def  mysqrt( a, x , e):
	""" Estimates the square root of a selected number 'a' from an initial estimate 'x', that is within an epsilon 'e' error margin"""
	while True:
		print(x)
		y = ( x + a/x)/2
		if  abs(y -x) < e:
			break
		x = y
	Difference = x - math.sqrt(a)
	print('square root estimate is ', x)
	print('square-root is ', math.sqrt(a))
	print('Difference is ', Difference)





    
