import pandas as pd 
from openpyxl import Workbook

training_data = {
    'Day': [],
    'Morning Warm-up': [],
    'Morning Session': [],
    'Morning Km': [],
    'Afternoon Warm-up': [],
    'Afternoon Session': [],
    'Afternoon Km': []
}   

def generate_training_plan(month, year):
    # Création d'un DataFrame vide pour le mois
    df = pd.DataFrame(training_data)
    
    # Génération des semaines et jours pour le mois donné
    weeks_in_month = pd.date_range(start=f'{year}-{month}-01', periods=4, freq='W-MON')
    
    for week_start in weeks_in_month:
        for i in range(7):  # 7 jours par semaine
            day = week_start + pd.Timedelta(days=i)
            df = df.append({
                'Day': day.strftime('%Y-%m-%d'),
                'Morning Warm-up': '',
                'Morning Session': '',
                'Morning Km': '',
                'Afternoon Warm-up': '',
                'Afternoon Session': '',
                'Afternoon Km': ''
            }, ignore_index=True)
        
        # Calculer le total des km pour la semaine
        week_total_km = df.loc[df['Day'].between(week_start, week_start + pd.Timedelta(days=6)), 'Morning Km'].sum() + \
                        df.loc[df['Day'].between(week_start, week_start + pd.Timedelta(days=6)), 'Afternoon Km'].sum()
        
        # Ajouter une ligne pour le total des km de la semaine
        df = df.append({
            'Day': 'Total Km',
            'Morning Warm-up': '',
            'Morning Session': '',
            'Morning Km': '',
            'Afternoon Warm-up': '',
            'Afternoon Session': '',
            'Afternoon Km': week_total_km
        }, ignore_index=True)
    return df


def export_training_plan_to_excel(training_plan, month, year):
    wb = Workbook()
    ws = wb.active
    ws.title = f'Training Plan - {month}-{year}'
    
    for r in dataframe_to_rows(training_plan, index=False, header=True):
        ws.append(r)
    
    file_path = f'training_plan_{month}_{year}.xlsx'
    wb.save(file_path)
    print(f"Training plan saved to {file_path}")