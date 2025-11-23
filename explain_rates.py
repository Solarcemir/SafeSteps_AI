import pandas as pd

df = pd.read_csv('Neighbourhood_Crime_Rates_Open_Data_6759951416839911996.csv')

print('=' * 80)
print('QUE SIGNIFICA EL "RATE" EN EL DATASET?')
print('=' * 80)

print('\n=== EJEMPLO 1: South Eglinton-Davisville ===\n')
row = df.iloc[0]
print(f'Poblacion 2024: {row["POPULATION_2024"]:,} personas')
print(f'ASSAULTS en 2024: {row["ASSAULT_2024"]} casos')
print(f'ASSAULT_RATE_2024: {row["ASSAULT_RATE_2024"]:.2f}')
print(f'\nCALCULO:')
print(f'{row["ASSAULT_2024"]} assaults / {row["POPULATION_2024"]:,} personas × 100,000 = {(row["ASSAULT_2024"] / row["POPULATION_2024"]) * 100000:.2f}')

print('\n' + '=' * 80)
print('EXPLICACION: El RATE es "por cada 100,000 habitantes"')
print('=' * 80)
print('\nEs una forma de NORMALIZAR los datos para comparar areas con poblaciones diferentes.')
print('Si solo usaras el numero de casos, las areas grandes siempre parecerian mas peligrosas.')

print('\n=== EJEMPLO 2: Trinity-Bellwoods (Area Peligrosa) ===\n')
trinity = df[df['NEIGHBOURHOOD_NAME'] == 'Trinity-Bellwoods'].iloc[0]
print(f'Poblacion 2024: {trinity["POPULATION_2024"]:,} personas')
print(f'ASSAULTS 2024: {trinity["ASSAULT_2024"]} casos')
print(f'ASSAULT_RATE_2024: {trinity["ASSAULT_RATE_2024"]:.2f}')
print(f'\nCALCULO:')
print(f'{trinity["ASSAULT_2024"]} / {trinity["POPULATION_2024"]:,} × 100,000 = {(trinity["ASSAULT_2024"] / trinity["POPULATION_2024"]) * 100000:.2f}')

print('\n=== COMPARACION ===')
print(f'South Eglinton: {row["ASSAULT_RATE_2024"]:.1f} assaults por 100k habitantes')
print(f'Trinity-Bellwoods: {trinity["ASSAULT_RATE_2024"]:.1f} assaults por 100k habitantes')
print(f'\nTrinity-Bellwoods es {trinity["ASSAULT_RATE_2024"] / row["ASSAULT_RATE_2024"]:.1f}x MAS PELIGROSO!')

print('\n' + '=' * 80)
print('RESUMEN DEL DATASET')
print('=' * 80)
print(f'Total de barrios: {len(df)}')
print(f'Poblacion total Toronto: {df["POPULATION_2024"].sum():,} personas')
print(f'\nTipos de crimen con RATE:')
rate_cols = [col for col in df.columns if 'RATE_2024' in col]
for col in rate_cols:
    crime_type = col.replace('_RATE_2024', '')
    print(f'  - {crime_type}')

print(f'\nRango de poblaciones:')
print(f'  - Barrio mas pequeno: {df["POPULATION_2024"].min():,} personas')
print(f'  - Barrio mas grande: {df["POPULATION_2024"].max():,} personas')
print(f'  - Promedio: {df["POPULATION_2024"].mean():.0f} personas')
