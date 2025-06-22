from app import create_app
from models import db, User, Guest, Episode, Appearance
from datetime import date

def seed_data():
    app = create_app()
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # Create sample users
        user1 = User(username='admin')
        user1.set_password('password123')
        
        user2 = User(username='testuser')
        user2.set_password('test123')
        
        db.session.add(user1)
        db.session.add(user2)
        
        # Create sample guests
        guests = [
            Guest(name='Jennifer Lawrence', occupation='Actress'),
            Guest(name='Elon Musk', occupation='Entrepreneur'),
            Guest(name='Taylor Swift', occupation='Musician'),
            Guest(name='Neil deGrasse Tyson', occupation='Astrophysicist'),
            Guest(name='Amy Schumer', occupation='Comedian'),
        ]
        
        for guest in guests:
            db.session.add(guest)
        
        # Create sample episodes
        episodes = [
            Episode(date=date(2024, 1, 15), number=101),
            Episode(date=date(2024, 1, 16), number=102),
            Episode(date=date(2024, 1, 17), number=103),
            Episode(date=date(2024, 1, 18), number=104),
            Episode(date=date(2024, 1, 19), number=105),
        ]
        
        for episode in episodes:
            db.session.add(episode)
        
        db.session.commit()
        
        # Create sample appearances
        appearances = [
            Appearance(rating=5, guest_id=1, episode_id=1),
            Appearance(rating=4, guest_id=2, episode_id=1),
            Appearance(rating=5, guest_id=3, episode_id=2),
            Appearance(rating=4, guest_id=4, episode_id=3),
            Appearance(rating=3, guest_id=5, episode_id=4),
            Appearance(rating=5, guest_id=1, episode_id=5),
        ]
        
        for appearance in appearances:
            db.session.add(appearance)
        
        db.session.commit()
        
        print("Database seeded successfully!")
        print(f"Created {len(guests)} guests, {len(episodes)} episodes, and {len(appearances)} appearances")

if __name__ == '__main__':
    seed_data()