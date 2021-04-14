# Identify information given
i = 0.05         # Annual effective interest rate, assume compound
i_12 = 12*(((1+i)**(1/12))-1 )      # Nominal monthly interest rate
prop = 0.1      # proportion of salary set aside each month
salary_monthly = 12000
n = 2    # term in years

# At end of two years:

Savings = 12*(salary_monthly*prop)* (1-(1+i)**(-n))/(i_12)

#****************************************************************************


#Debugging process: Error was valuing present value of savings, not future value

Savings = 12*(salary_monthly*prop)*((1+i)**n - 1)/i_12     #re-define the funtion from being present value to being future value; savings made at end of each month

>>> print(Savings)
30190.540722808935

