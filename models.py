from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazev = db.Column(db.String(100), nullable=False)  # name
    vedecky_nazev = db.Column(db.String(100), nullable=False)  # scientific name
    rad = db.Column(db.String(100))  # order
    celed = db.Column(db.String(100))  # family
    delka_cm = db.Column(db.Float)  # length in cm
    rozpeti_cm = db.Column(db.Float)  # wingspan in cm
    hmotnost_g = db.Column(db.Float)  # weight in grams
    status_ohrozeni = db.Column(db.String(50))  # conservation status
    typ_potravy = db.Column(db.String(50))  # diet type
    migrace = db.Column(db.Boolean)  # migration (0 or 1)
    vyskyt_kontinent = db.Column(db.String(50))  # continent
    snuska_ks = db.Column(db.Float)  # clutch size

    def __repr__(self):
        return f'<Bird {self.nazev}>'