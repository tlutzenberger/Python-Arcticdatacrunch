# Tom Lutzenberger
# Arctic Ice/Greenhouse Gas Comparison w Python
# May 19, 2024


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Check the current working directory
print(f"Current working directory: {os.getcwd()}")

# Specify the file paths - absolute paths necessary to update as the program could not
# automaticall see the location of source files even when in the same folder, as in web design.
# Pathways need to change and be update depending where the user runs this program and places
# the data source files. Adding new source files requires updating the code for additional
# source elements to calculate, compile and visualize. 
ghg_data_path = r'C:\python\CO2gas.csv'
ice_data_nh_path = r'C:\python\IceExtentNH.csv'
ice_data_sh_path = r'C:\python\IceExtentSH.csv'

# Load (GHG) greenhouse gas data
ghg_data = pd.read_csv(ghg_data_path)

# Load (NH) ice data
ice_data_nh = pd.read_csv(ice_data_nh_path)

# Load (SH) ice data
ice_data_sh = pd.read_csv(ice_data_sh_path)

# Load Data
# Assume you have CSV files with 'year' and 'value' columns
ghg_data = pd.read_csv(ghg_data_path)
ice_data_nh = pd.read_csv(ice_data_nh_path)
ice_data_sh = pd.read_csv(ice_data_sh_path)

# Print column names to debug
print("Greenhouse Gas Data Columns:", ghg_data.columns)
print("Arctic Ice Data Columns:", ice_data_nh.columns)
print("Antarctic Ice Data Columns:", ice_data_sh.columns)

# Preprocess Data
# Ensure all datasets cover the same time period
start_year = max(ghg_data['year'].min(), ice_data_nh['year'].min(), ice_data_sh['year'].min())
end_year = min(ghg_data['year'].max(), ice_data_nh['year'].max(), ice_data_sh['year'].max())

ghg_data = ghg_data[(ghg_data['year'] >= start_year) & (ghg_data['year'] <= end_year)]
ice_data_nh = ice_data_nh[(ice_data_nh['year'] >= start_year) & (ice_data_nh['year'] <= end_year)]
ice_data_sh = ice_data_sh[(ice_data_sh['year'] >= start_year) & (ice_data_sh['year'] <= end_year)]

# Merge the datasets on the 'year' column
merged_data = pd.merge(ghg_data, ice_data_nh, on='year', suffixes=('_ghg', '_ice_nh'))
merged_data = pd.merge(merged_data, ice_data_sh, on='year')
merged_data.rename(columns={'value': 'value_ice_sh'}, inplace=True)

# Print merged data columns to debug
print("Merged Data Columns:", merged_data.columns)

# Analyze Data
# Calculate correlations
correlation_nh = merged_data['value_ghg'].corr(merged_data['value_ice_nh'])
correlation_sh = merged_data['value_ghg'].corr(merged_data['value_ice_sh'])
print(f'Correlation between greenhouse gas levels and Arctic ice extent: {correlation_nh}')
print(f'Correlation between greenhouse gas levels and Antarctic ice extent: {correlation_sh}')

# Visualize Data
plt.figure(figsize=(14, 7))

# Plot greenhouse gas data
sns.lineplot(x='year', y='value_ghg', data=merged_data, color='orange', label='Greenhouse Gas Levels')
# Create a secondary y-axis for the ice data
ax2 = plt.gca().twinx()
sns.lineplot(x='year', y='value_ice_nh', data=merged_data, ax=ax2, color='blue', label='North Hemisphere Ice Extent')
sns.lineplot(x='year', y='value_ice_sh', data=merged_data, ax=ax2, color='green', label='South Hemisphere Ice Extent')

plt.title('Greenhouse Gas Levels vs. Arctic Northern & Southern Hemisphere Ice Extent Over Time')
plt.xlabel('Year')
plt.ylabel('Greenhouse Gas Levels')
ax2.set_ylabel('Ice Extent')

# Show legends
plt.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

# Results
# Print a summary of the findings
print(f'The data analysis shows a correlation of {correlation_nh} between GHG levels and Northern Hemisphere ice extent.')
print(f'The data analysis shows a correlation of {correlation_sh} between GHG gas levels and Southern Hemisphere ice extent.')

#end program.