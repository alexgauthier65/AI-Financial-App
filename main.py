import streamlit as st
import pandas as pd
import time


st.title('AI Financial Planner')
prompt = st.chat_input("Enter your prompt: ")
finCSV = st.file_uploader('Upload your financial csv', type=["csv"])
#st.write('Thinking...')
#time.sleep(5)
#st.write('Data Parsed Successfully!')

if finCSV and prompt is not None:
    data = pd.read_csv(finCSV)
    st.write(prompt)
    
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
#print('Current Balance: ', currentBalance)