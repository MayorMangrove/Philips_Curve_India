import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

# Load your data
df1 = pd.read_excel("unemployment_india.xls")  
df2 = pd.read_excel("inflation_india.xlsx") 
df = pd.merge(df1, df2, on="year")
X = sm.add_constant(df["unemployment"])
y = df["inflation"]

model = sm.OLS(y, X).fit()
print(model.summary())

# Plot
plt.scatter(df["unemployment"], df["inflation"])
plt.plot(df["unemployment"], model.fittedvalues, color="red")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Inflation Rate (%)")
plt.title("Phillips Curve – India")
plt.show()

fig, ax=plt.subplots()
inflation=ax.plot(df["year"], df["inflation"], color="blue", label="Inflation Rate")
unemployment=ax.plot(df["year"], df["unemployment"], color="orange", label="Unemployment Rate")
ax.set_xlabel("Year")
ax.set_ylabel("Rate (%)")
ax.legend()
plt.show()
