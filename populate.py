from main import app, db
from models import Bird

def populate_db():
    with app.app_context():
        db.create_all()
        
        # Sample data
        birds = [
            Bird(name="Bald Eagle", species="Haliaeetus leucocephalus", habitat="Near water", diet="Fish", size=90.0, weight=5000.0, lifespan=20, conservation_status="Least Concern"),
            Bird(name="American Robin", species="Turdus migratorius", habitat="Forests", diet="Insects", size=25.0, weight=77.0, lifespan=2, conservation_status="Least Concern"),
            Bird(name="Peregrine Falcon", species="Falco peregrinus", habitat="Cliffs", diet="Birds", size=50.0, weight=1000.0, lifespan=15, conservation_status="Least Concern"),
            Bird(name="California Condor", species="Gymnogyps californianus", habitat="Mountains", diet="Carrion", size=120.0, weight=9000.0, lifespan=50, conservation_status="Critically Endangered"),
            Bird(name="Blue Jay", species="Cyanocitta cristata", habitat="Woodlands", diet="Nuts", size=30.0, weight=100.0, lifespan=7, conservation_status="Least Concern"),
            Bird(name="Whooping Crane", species="Grus americana", habitat="Wetlands", diet="Fish", size=150.0, weight=7000.0, lifespan=25, conservation_status="Endangered"),
            Bird(name="Ruby-throated Hummingbird", species="Archilochus colubris", habitat="Gardens", diet="Nectar", size=9.0, weight=3.0, lifespan=5, conservation_status="Least Concern"),
            Bird(name="Great Horned Owl", species="Bubo virginianus", habitat="Forests", diet="Small mammals", size=55.0, weight=1400.0, lifespan=13, conservation_status="Least Concern"),
            Bird(name="Northern Cardinal", species="Cardinalis cardinalis", habitat="Shrubs", diet="Seeds", size=21.0, weight=45.0, lifespan=3, conservation_status="Least Concern"),
            Bird(name="American Goldfinch", species="Spinus tristis", habitat="Fields", diet="Seeds", size=12.0, weight=12.0, lifespan=11, conservation_status="Least Concern"),
        ]
        
        for bird in birds:
            db.session.add(bird)
        db.session.commit()
        print("Database populated with sample data.")

if __name__ == "__main__":
    populate_db()