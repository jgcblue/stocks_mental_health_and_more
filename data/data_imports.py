import pandas as pd
from data_utils import calculate_and_set_average_by_year, calculate_average_by_year_micro, merge_and_drop_na, read_stock_data, rename_columns

'''
This script performs data manipulation and analysis on stock market data for three companies: Apple, Microsoft, and Nvidia.
It calculates average closing prices by year, merges the data, and prepares a final DataFrame for further analysis.

Requirements:
- The data_utils module must contain the functions specified in its documentation.

'''

# Read stock data for each company
bigApple = read_stock_data('More_BigThree_data/bapple.csv')
bigMicrosoft = read_stock_data('More_BigThree_data/bMicrosoft.csv')
bigNvda = read_stock_data('More_BigThree_data/bNvda.csv')

# Calculate average closing prices by year and set index
average_apple = calculate_and_set_average_by_year(bigApple, 'Date', 'Close')
average_Nvda = calculate_and_set_average_by_year(bigNvda, 'Date', 'Close')
average_Microsoft = calculate_and_set_average_by_year_micro(bigMicrosoft, 'date', 'close')

# Merge dataframes and drop rows with NaN values
merged_1 = merge_and_drop_na([average_apple, average_Microsoft])
merged_2 = merge_and_drop_na([merged_1, average_Nvda])

# Rename columns
merged_3 = rename_columns(merged_2, ['apple_closing_avg', 'msft_closing_avg', 'nvda_closing_avg'])

# Create a final DataFrame for further analysis
final = merged_3.copy()

'''
The script first imports necessary libraries and functions from the data_utils module.
It then reads stock data for Apple, Microsoft, and Nvidia.
Average closing prices are calculated by year for each company using different functions.
The calculated averages are merged and rows with missing values are dropped.
Columns are renamed for clarity, and the final DataFrame is created for analysis.

Please ensure that the data_utils module contains the following functions:
- calculate_and_set_average_by_year
- calculate_average_by_year_micro
- merge_and_drop_na
- read_stock_data
- rename_columns
'''

