from database import db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_database():
    # Check if admin user already exists
    if db.users.find_one({"email": "admin@bridge.com"}):
        print("Admin user already exists.")
        return

    # Create admin user
    hashed_password = pwd_context.hash("adminpassword")
    db.users.insert_one({
        "firstName": "Admin",
        "lastName": "User",
        "email": "admin@bridge.com",
        "password": hashed_password,
        "role": "admin"
    })
    print("Admin user created successfully.")

if __name__ == "__main__":
    seed_database()