# Building-Financial-Reports

# Financial Ratios Analysis of Companies

## Overview

This project analyzes the relationship between two financial ratios, the **Leverage Ratio** and the **Profitability Ratio**, for different company types. The data used includes a balance sheet and income statement, from which we compute the ratios, analyze the relationships, and plot relevant graphs to visually represent the data.

The project uses the following libraries:
- `pandas` for data manipulation and analysis
- `seaborn` for statistical visualization
- `matplotlib` for creating plots

## Files

- **data/Balance_Sheet.xlsx** - Contains the balance sheet data for companies.
- **data/Income_Statement.xlsx** - Contains the income statement data for companies.
- **![image](https://github.com/user-attachments/assets/b64f1a39-035c-42d5-ac59-904a2b2b503d)** - A generated plot representing the relationship between leverage and profitability ratios.

## Requirements

Before running the project, ensure the required libraries are installed:

# Financial Data Analysis Project

## Required Libraries
To run the project, you need to install the following Python libraries:

```bash
pip install pandas numpy seaborn matplotlib
````
Steps to Run the Project
1. Load the Data
The project starts by loading the balance sheet and income statement data using pandas.read_excel():

````
import pandas as pd
Income_data = pd.read_excel('data/Balance_Sheet.xlsx')
Balance_data = pd.read_excel('data/Income_Statement.xlsx')
````
2. Merge the DataFrames
The data is merged on the comp_type, company, and Year columns to create a consolidated DataFrame:

````
df = pd.merge(Income_data, Balance_data, on=["comp_type", "company", "Year"])
````
3. Compute Ratios
Leverage Ratio: Total Liabilities / Total Stockholder Equity
Profitability Ratio: Gross Profit / Total Revenue
These ratios are stored in a new DataFrame df_ratios:

````
df_ratios = {
    "comp_type": df["comp_type"],
    "leverage_ratio": df["Total Liab"] / df["Total Stockholder Equity"],
    "profitability_ratio": df["Gross Profit"] / df["Total Revenue"]
}
df_ratios = pd.DataFrame(df_ratios)
````
4. Calculate Mean Ratios by Company Type
A pivot table is created to calculate the mean leverage and profitability ratios for each company type:

````
df_ratios_mean = df_ratios.pivot_table(index="comp_type", values=["profitability_ratio", "leverage_ratio"], aggfunc='mean')
````
5. Identify Company Types with Extremes
The company type with the lowest profitability ratio and the highest leverage ratio are identified:

````
lowest_profitability = df_ratios_mean["profitability_ratio"].idxmin()
highest_leverage = df_ratios_mean["leverage_ratio"].idxmax()
````
6. Analyze the Relationship between Leverage and Profitability
The correlation between the leverage ratio and profitability ratio for real estate companies (comp_type = 'real_est') is calculated:

````
real_estate_data = df_ratios[df_ratios['comp_type'] == 'real_est']
correlation = real_estate_data['leverage_ratio'].corr(real_estate_data['profitability_ratio'])
````
The relationship is classified based on the correlation value:

Positive relationship if correlation > 0
Negative relationship if correlation < 0
No relationship if correlation == 0
````
if correlation > 0:
    relationship = "positive"
elif correlation < 0:
    relationship = "negative"
else:
    relationship = "no relationship"
````
7. Plotting
A scatter plot with a line of best fit is created to visually represent the relationship between the leverage ratio and profitability ratio for real estate companies:

````
import seaborn as sns
import matplotlib.pyplot as plt


sns.regplot(data=real_estate_data, x="leverage_ratio", y="profitability_ratio")
plt.title("Relationship Between Leverage Ratio and Profitability Ratio")
plt.xlabel("Leverage Ratio")
plt.ylabel("Profitability Ratio")
plt.show()
````
Output


The company type with the lowest profitability ratio and the highest leverage ratio will be printed.
The relationship between leverage and profitability for real estate companies will be printed as either positive, negative, or no relationship.
A scatter plot with a regression line will be displayed showing the relationship between the two ratios.

Example Output


lowest_profitability real_est
highest_leverage real_est
The relationship between leverage and profitability for real estate companies is: positive
#Conclusion
This project provides insights into the financial behavior of companies across different sectors, focusing particularly on the relationship between leverage and profitability for real estate companies.



### Explanation:
- The markdown structure follows a clear flow, from library installation to the project's final output.
- Each step is labeled, and code snippets are clearly separated with syntax highlighting.
- This ensures the reader can easily follow and execute each step of the process.
