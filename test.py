""" print_db.py
Utility script to print all records from the 'users' table.
Run it from the terminal:
    python print_db.py
"""

from database_config import SessionLocal
from models_database import User

def print_all_users():
    """Fetch and print every row in the users table."""
    db = SessionLocal()
    try:
        users = db.query(User).all()
        if not users:
            print("No users found in the database.")
            return

        print(f"\n{'='*80}")
        print(f"Total users: {len(users)}")
        print('-' * 80)
        for user in users:
            print(f"ID          : {user.id}")
            print(f"Name        : {user.name}")
            print(f"Username    : {user.username}")
            print(f"Email       : {user.email}")
            print(f"Password hash: {user.password_hash[:20]}...")   # only first 20 chars
            print(f"Created at  : {user.created_at}")
            print('-' * 80)
        print(f"{'='*80}\n")

    finally:
        db.close()

if __name__ == "__main__":
    print_all_users()