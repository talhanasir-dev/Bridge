#!/usr/bin/env python3
"""
Script to reset password for parent1@bridge.com user
"""
from passlib.context import CryptContext
from database import db

# Password hashing context (same as in auth.py)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def reset_parent_password():
    """Reset password for parent1@bridge.com to a known value"""
    
    email = "parent1@bridge.com"
    new_password = "password123"  # Simple password for testing
    
    # Check if user exists
    user = db.users.find_one({"email": email})
    
    if not user:
        print(f"❌ User with email {email} does not exist!")
        return
    
    # Hash the new password
    hashed_password = pwd_context.hash(new_password)
    
    # Update the user's password
    try:
        db.users.update_one(
            {"email": email},
            {"$set": {"password": hashed_password}}
        )
        print(f"✅ Password reset successfully for {email}!")
        print(f"   New password: {new_password}")
        print(f"\n🔐 You can now login with:")
        print(f"   Email: {email}")
        print(f"   Password: {new_password}")
    except Exception as e:
        print(f"❌ Error resetting password: {str(e)}")

if __name__ == "__main__":
    print("=" * 60)
    print("Resetting Password for parent1@bridge.com")
    print("=" * 60)
    reset_parent_password()
    print("=" * 60)

