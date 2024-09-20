import pandas as pd

# Load population data and filter for years between 1922 and 2022
df_population = pd.read_csv('C:/Users/ASUS/Documents/GitHub/FIT3179_Week9_Homework/data/population.csv')
filtered_df_population = df_population[(df_population['Year'] >= 1922) & (df_population['Year'] <= 2022)]

# Load air pollutants data and filter for years between 1922 and 2022
df_air_pollutants = pd.read_csv('C:/Users/ASUS/Documents/GitHub/FIT3179_Week9_Homework/data/amount_of_air_pollutants.csv')
filtered_df_air_pollutants = df_air_pollutants[(df_air_pollutants['Year'] >= 1922) & (df_air_pollutants['Year'] <= 2022)]

# Merge datasets on 'Year', 'Entity', and 'Code'
merged_df = pd.merge(filtered_df_population, filtered_df_air_pollutants, on=['Year', 'Entity', 'Code'], how='inner')

# Replace "United States" with "United States of America" in the 'Entity' column
merged_df['Entity'] = merged_df['Entity'].replace('United States', 'United States of America')

# List of pollutant columns
pollutants_columns = [
    'Nitrogen oxide (NOx)', 
    'Sulphur dioxide (SO₂) emissions', 
    'Carbon monoxide (CO) emissions', 
    'Black carbon (BC) emissions', 
    'Ammonia (NH₃) emissions', 
    'Non-methane volatile organic compounds (NMVOC) emissions'
]

# Calculate pollutants per population and add new columns
for pollutant in pollutants_columns:
    merged_df[f'{pollutant} per population (kg)'] = (merged_df[pollutant] / merged_df['Population (historical)']) * 1000

# Save the modified dataframe to a new CSV file
merged_df.to_csv('pollutants_per_population_1922_2022.csv', index=False)

# Print the first few rows of the resulting dataframe
print(merged_df.head())
