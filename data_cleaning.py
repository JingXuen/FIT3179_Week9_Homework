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
merged_df['Entity'] = merged_df['Entity'].replace('Democratic Republic of Congo', 'Dem. Rep. Congo')
merged_df['Entity'] = merged_df['Entity'].replace('South Sudan', 'S. Sudan')
merged_df['Entity'] = merged_df['Entity'].replace('Central African Republic', 'Central African Rep.')
merged_df['Entity'] = merged_df['Entity'].replace('Côte d\'Ivoire', 'Côte d\'Ivoire')
merged_df['Entity'] = merged_df['Entity'].replace('Equatorial Guinea', 'Eq. Guinea')

# Calculate Nitrogen oxide (NOx) per population and add new column
merged_df['Nitrogen oxide (NOx) per population (kg)'] = (merged_df['Nitrogen oxide (NOx)'] / merged_df['Population (historical)']) * 1000

# Remove all other pollutant columns
columns_to_remove = [
    'Sulphur dioxide (SO₂) emissions', 
    'Carbon monoxide (CO) emissions', 
    'Black carbon (BC) emissions', 
    'Ammonia (NH₃) emissions', 
    'Non-methane volatile organic compounds (NMVOC) emissions'
]
merged_df = merged_df.drop(columns=columns_to_remove)

# Add 'Entity_Year' column for joining purposes
merged_df['Entity_Year'] = merged_df['Entity'] + '_' + merged_df['Year'].astype(str)

# Save the cleaned data to a new CSV file
merged_df.to_csv('pollutants_per_population_1922_2022.csv', index=False)

# Print the first few rows of the resulting dataframe
print(merged_df.head())

