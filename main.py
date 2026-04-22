from flask import Flask, render_template, request, redirect, url_for
import matplotlib.pyplot as plt
import io
import base64
from models import db, Bird
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    birds = Bird.query.all()
    return render_template('index.html', birds=birds)

@app.route('/add', methods=['GET', 'POST'])
def add_bird():
    if request.method == 'POST':
        nazev = request.form['nazev']
        vedecky_nazev = request.form['vedecky_nazev']
        rad = request.form['rad']
        celed = request.form['celed']
        delka_cm = float(request.form['delka_cm']) if request.form['delka_cm'] else None
        rozpeti_cm = float(request.form['rozpeti_cm']) if request.form['rozpeti_cm'] else None
        hmotnost_g = float(request.form['hmotnost_g']) if request.form['hmotnost_g'] else None
        status_ohrozeni = request.form['status_ohrozeni']
        typ_potravy = request.form['typ_potravy']
        migrace = bool(int(request.form['migrace'])) if request.form['migrace'] else False
        vyskyt_kontinent = request.form['vyskyt_kontinent']
        snuska_ks = float(request.form['snuska_ks']) if request.form['snuska_ks'] else None
        
        new_bird = Bird(
            nazev=nazev,
            vedecky_nazev=vedecky_nazev,
            rad=rad,
            celed=celed,
            delka_cm=delka_cm,
            rozpeti_cm=rozpeti_cm,
            hmotnost_g=hmotnost_g,
            status_ohrozeni=status_ohrozeni,
            typ_potravy=typ_potravy,
            migrace=migrace,
            vyskyt_kontinent=vyskyt_kontinent,
            snuska_ks=snuska_ks
        )
        db.session.add(new_bird)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_bird.html')

@app.route('/stats')
def stats():
    birds = Bird.query.all()
    df = pd.DataFrame([{
        'nazev': b.nazev,
        'vedecky_nazev': b.vedecky_nazev,
        'rad': b.rad,
        'celed': b.celed,
        'delka_cm': b.delka_cm,
        'rozpeti_cm': b.rozpeti_cm,
        'hmotnost_g': b.hmotnost_g,
        'status_ohrozeni': b.status_ohrozeni,
        'typ_potravy': b.typ_potravy,
        'migrace': b.migrace,
        'vyskyt_kontinent': b.vyskyt_kontinent,
        'snuska_ks': b.snuska_ks
    } for b in birds])
    
    # Generate plots
    plots = {}
    
    # Length distribution
    if not df['delka_cm'].isnull().all():
        fig, ax = plt.subplots()
        df['delka_cm'].dropna().plot(kind='hist', ax=ax, title='Délka Distribution (cm)')
        plots['delka'] = get_plot_img(fig)
    
    # Weight distribution
    if not df['hmotnost_g'].isnull().all():
        fig, ax = plt.subplots()
        df['hmotnost_g'].dropna().plot(kind='hist', ax=ax, title='Hmotnost Distribution (g)')
        plots['hmotnost'] = get_plot_img(fig)
    
    # Wingspan distribution
    if not df['rozpeti_cm'].isnull().all():
        fig, ax = plt.subplots()
        df['rozpeti_cm'].dropna().plot(kind='hist', ax=ax, title='Rozpětí Distribution (cm)')
        plots['rozpeti'] = get_plot_img(fig)
    
    # Conservation status
    if not df['status_ohrozeni'].isnull().all():
        fig, ax = plt.subplots()
        df['status_ohrozeni'].value_counts().plot(kind='pie', ax=ax, title='Status Ohrožení')
        plots['status'] = get_plot_img(fig)
    
    # Diet type
    if not df['typ_potravy'].isnull().all():
        fig, ax = plt.subplots()
        df['typ_potravy'].value_counts().plot(kind='bar', ax=ax, title='Typ potravy')
        plots['potrava'] = get_plot_img(fig)
    
    return render_template('stats.html', plots=plots, df=df)

def get_plot_img(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close(fig)
    return plot_url

if __name__ == '__main__':
    app.run(debug=True)
