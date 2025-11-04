"""Create the SQLite database and seed initial activities.

Run this script to create the DB file and tables:

    python scripts/init_db.py

"""
from pathlib import Path
from src.db import engine, Base
from src.models import Activity

def seed_activities(session):
    # Minimal seed data copied from the existing in-memory app
    activities = [
        {
            "name": "Chess Club",
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
        },
        {
            "name": "Programming Class",
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
        },
        {
            "name": "Gym Class",
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
        },
    ]

    for a in activities:
        exists = session.query(Activity).filter_by(name=a["name"]).first()
        if not exists:
            act = Activity(
                name=a["name"],
                description=a.get("description"),
                schedule=a.get("schedule"),
                max_participants=a.get("max_participants"),
            )
            session.add(act)
    session.commit()


def main():
    # Ensure DB directory
    db_path = Path("./mcp.db")
    Base.metadata.create_all(bind=engine)
    from src.db import SessionLocal
    session = SessionLocal()
    try:
        seed_activities(session)
        print("Database initialized and seed data added (if missing).")
    finally:
        session.close()


if __name__ == "__main__":
    main()
