import pandas as pd
from main import app, db
from models import Bird

def populate_from_csv():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        df = pd.read_csv('dataset_ptaci_final.csv')
        
        for _, row in df.iterrows():
            bird = Bird(
                nazev=row['nazev'],
                vedecky_nazev=row['vedecky_nazev'],
                rad=row['rad'],
                celed=row['celed'],
                delka_cm=row['delka_cm'] if pd.notna(row['delka_cm']) else None,
                rozpeti_cm=row['rozpeti_cm'] if pd.notna(row['rozpeti_cm']) else None,
                hmotnost_g=row['hmotnost_g'] if pd.notna(row['hmotnost_g']) else None,
                status_ohrozeni=row['status_ohrozeni'],
                typ_potravy=row['typ_potravy'],
                migrace=bool(row['migrace']),
                vyskyt_kontinent=row['vyskyt_kontinent'],
                snuska_ks=row['snuska_ks'] if pd.notna(row['snuska_ks']) else None
            )
            db.session.add(bird)
        db.session.commit()
        print(f"Database populated with {len(df)} birds from CSV.")

if __name__ == "__main__":
    populate_from_csv()