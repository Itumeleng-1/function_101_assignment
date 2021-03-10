#Creating a fruitful function

>>> def Savings_function(term, interest_rate, proportion_saved, monthly_salary):
	salary_saved = proportion_saved*monthly_salary
	monthly_eff_rate = (1+ interest_rate)**(1/12)-1
	Savings = salary_saved*((1+ interest_rate)**term -1)/monthly_eff_rate
	print(Savings)

	
>>> Savings_function(2, 0.05, 0.1, 12000)
30190.540722808935
