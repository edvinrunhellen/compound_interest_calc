# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Compound Interest Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)
starting_amount = col1.number_input("Starting Ammount (in SEK)", min_value=0, value=10000)
average_return = col1.number_input("Average Return (in %)", min_value=0, value=8)
years = col2.number_input("Years", min_value=0, value=10)
monthly_savings = col2.number_input("Monthly Savings (in SEK)", min_value=0, value=100)

growth = []
total_savings = starting_amount

for year in range(int(years) + 1):
    growth.append([year, total_savings])
    total_savings += monthly_savings * 12
    total_savings += total_savings * (average_return / 100) ##Add compound

df = pd.DataFrame(growth, columns=["Year", "Total Value"])

st.write("### Growth Over Time")
st.line_chart(df.set_index("Year"))

total_deposits = starting_amount + (monthly_savings * 12 * years)
total_interest = total_savings - total_deposits

st.write("### Earnings")
col1, col2, col3, = st.columns(3)
col1.metric(label="Total Value", value=f"{total_savings:,.0f} SEK".replace(",", "."))
col2.metric(label="Total Deposits", value=f"{total_deposits:,.0f} SEK".replace(",", "."))
col3.metric(label="Interest Earned", value=f"{total_interest:,.0f} SEK".replace(",", "."))
