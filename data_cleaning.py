import pandas as pd

df_population = pd.read_csv('C:/Users/ASUS/Documents/GitHub/FIT3179_Week9_Homework/data/population.csv')
filtered_df_population = df_population[(df_population['Year'] >= 1922) & (df_population['Year'] <= 2022)]

df_air_pollutants = pd.read_csv('C:/Users/ASUS/Documents/GitHub/FIT3179_Week9_Homework/data/amount_of_air_pollutants.csv')
filtered_df_air_pollutants = df_air_pollutants[(df_air_pollutants['Year'] >= 1922) & (df_air_pollutants['Year'] <= 2022)]

merged_df = pd.merge(filtered_df_population, filtered_df_air_pollutants, on=['Year', 'Entity', 'Code'], how='inner')

pollutants_columns = [
    'Nitrogen oxide (NOx)', 
    'Sulphur dioxide (SO₂) emissions', 
    'Carbon monoxide (CO) emissions', 
    'Black carbon (BC) emissions', 
    'Ammonia (NH₃) emissions', 
    'Non-methane volatile organic compounds (NMVOC) emissions'
]

for pollutant in pollutants_columns:
    merged_df[f'{pollutant} per population (kg)'] = (merged_df[pollutant] / merged_df['Population (historical)']) * 1000

merged_df.to_csv('pollutants_per_population_1922_2022.csv', index=False)

print(merged_df.head())