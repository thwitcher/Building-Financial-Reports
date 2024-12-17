import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Income_data = pd.read_excel('data/Balance_Sheet.xlsx')
Balance_data = pd.read_excel('data/Income_Statement.xlsx')

#Merging DataFrames
df = pd.merge(Income_data, Balance_data, on=["comp_type", "company", "Year"])
#Compution the ratios
df_ratios = { "comp_type": df["comp_type"],
    "leverage_ratio": df["Total Liab"] / df["Total Stockholder Equity"],
    "profitability_ratio": df["Gross Profit"] / df["Total Revenue"]
}
df_ratios = pd.DataFrame(df_ratios)

df_ratios_mean = df_ratios.pivot_table(index="comp_type", values=["profitability_ratio","leverage_ratio"],aggfunc='mean')

#company type that have the lowest profitability ratio
print(df_ratios_mean)

lowest_profitability = df_ratios_mean["profitability_ratio"].idxmin()


print("lowest_profitability", lowest_profitability)

#company type that have the highest leverage ratio

highest_leverage = df_ratios_mean["leverage_ratio"].idxmax()

print("highest_leverage",highest_leverage)



# Assuming "comp_type" is the company type and "Real Estate" is one of the values.
real_estate_data = df_ratios[df_ratios['comp_type'] == 'real_est']

# Calculate the correlation between 'leverage_ratio' and 'profitability_ratio'
correlation = real_estate_data['leverage_ratio'].corr(real_estate_data['profitability_ratio'])

# Determine the relationship based on the correlation
if correlation > 0:
    relationship = "positive"
elif correlation < 0:
    relationship = "negative"
else:
    relationship = "no relationship"

# Print the relationship
print(f"The relationship between leverage and profitability for real estate companies is: {relationship}")

sns.regplot(data=real_estate_data, x="leverage_ratio", y="profitability_ratio")
plt.title("Relationship Between Leverage Ratio and Profitability Ratio")
plt.xlabel("Leverage Ratio")
plt.ylabel("Profitability Ratio")
plt.show()
