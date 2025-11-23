import pandas as pd
import json

df = pd.read_csv('Neighbourhood_Crime_Rates_Open_Data_6759951416839911996.csv')

print('=' * 80)
print('ANÁLISIS DE DATOS DISPONIBLES PARA LAYERS')
print('=' * 80)

# Crime types 2024
rate_cols_2024 = [col for col in df.columns if '2024' in col and 'RATE' in col]

print('\n1. CRIME TYPES DISPONIBLES (2024 RATES):\n')
crime_stats = {}
for col in rate_cols_2024:
    crime = col.replace('_RATE_2024', '')
    min_val = df[col].min()
    max_val = df[col].max()
    mean_val = df[col].mean()
    crime_stats[crime] = {'min': min_val, 'max': max_val, 'mean': mean_val}
    print(f'{crime:15s} - Min: {min_val:7.1f}  Max: {max_val:7.1f}  Avg: {mean_val:7.1f}')

print(f'\nTotal: {len(rate_cols_2024)} tipos de crimen')

# Count columns (absolute numbers)
count_cols_2024 = [col for col in df.columns if '2024' in col and 'RATE' not in col and col != 'POPULATION_2024']

print('\n' + '=' * 80)
print('2. DATOS ABSOLUTOS (2024 COUNTS):')
print('=' * 80)
for col in count_cols_2024:
    crime = col.replace('_2024', '')
    total = df[col].sum()
    print(f'{crime:15s} - Total en Toronto: {total:,} casos')

# Top dangerous neighborhoods per crime type
print('\n' + '=' * 80)
print('3. BARRIOS MÁS PELIGROSOS POR TIPO DE CRIMEN:')
print('=' * 80)

top_crimes = ['ASSAULT', 'ROBBERY', 'SHOOTING', 'HOMICIDE', 'AUTOTHEFT', 'BREAKENTER']
for crime in top_crimes:
    col = f'{crime}_RATE_2024'
    if col in df.columns:
        top_hood = df.nlargest(1, col).iloc[0]
        print(f'\n{crime}:')
        print(f'  Barrio: {top_hood["NEIGHBOURHOOD_NAME"]}')
        print(f'  Rate: {top_hood[col]:.1f} por 100k')
        print(f'  Casos: {top_hood[f"{crime}_2024"]}')

# Population stats
print('\n' + '=' * 80)
print('4. ESTADÍSTICAS DE POBLACIÓN:')
print('=' * 80)
print(f'Total población: {df["POPULATION_2024"].sum():,}')
print(f'Barrio más poblado: {df.nlargest(1, "POPULATION_2024").iloc[0]["NEIGHBOURHOOD_NAME"]} ({df["POPULATION_2024"].max():,})')
print(f'Barrio menos poblado: {df.nsmallest(1, "POPULATION_2024").iloc[0]["NEIGHBOURHOOD_NAME"]} ({df["POPULATION_2024"].min():,})')

# Time series available
years = sorted(list(set([col.split('_')[-1] for col in df.columns if col.startswith('ASSAULT_') and 'RATE' not in col])))
print('\n' + '=' * 80)
print('5. AÑOS DISPONIBLES PARA ANÁLISIS TEMPORAL:')
print('=' * 80)
print(f'Años: {", ".join(years)}')
print(f'Total: {len(years)} años de datos')

# Suggest layer ideas
print('\n' + '=' * 80)
print('6. SUGERENCIAS DE LAYERS PARA IMPLEMENTAR:')
print('=' * 80)
print('''
LAYERS POR TIPO DE CRIMEN:
✅ Violent Crimes Layer (ASSAULT + ROBBERY + SHOOTING + HOMICIDE)
✅ Property Crimes Layer (AUTOTHEFT + BREAKENTER + THEFTFROMMV + THEFTOVER)
✅ Personal Safety Layer (solo ASSAULT + SHOOTING + HOMICIDE + ROBBERY)
✅ Vehicle Safety Layer (AUTOTHEFT + THEFTFROMMV)
✅ Bike Safety Layer (BIKETHEFT)

LAYERS POR SEVERIDAD:
✅ Critical Crimes (HOMICIDE + SHOOTING)
✅ Major Crimes (ROBBERY + ASSAULT)
✅ Minor Crimes (THEFTOVER + BIKETHEFT)

LAYERS COMPARATIVOS:
✅ Trend Analysis (compare 2014 vs 2024)
✅ Crime Density Heatmap
✅ Population Density
✅ Crime per Capita (already implemented)

LAYERS INTERACTIVOS:
✅ Filter by Crime Type dropdown
✅ Time slider (2014-2024)
✅ Risk threshold slider
''')
