import pandas as pd



data = pd.read_csv(finCSV)
    
amount = data.iloc[:, 2]
#print(amount)

total = 0
amountMade = 0
amountSpent = 0

for i in range(len(amount)):
    #total += amount[i]
    if amount[i] > 0:
        amountMade += amount[i]
    if amount[i] < 0:
        amountSpent += abs(amount[i])
        
currentBalance = amountMade - amountSpent     
        
        
#print('total: ', total)
print('Amount Made: ', amountMade)
print('Amount Spent: ', amountSpent)
print('Current Balance: ', currentBalance)