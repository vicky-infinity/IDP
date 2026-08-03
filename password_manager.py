"""
security.py

Purpose:
---------
This file handles everything related to password security.

Current Functions:
1. Hash Password
2. Verify Password

Later:
- JWT Token Generation
- JWT Verification
"""

from passlib.context import CryptContext

# Configure the hashing algorithm
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Convert a plain password into a secure hashed password.
    
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compare the entered password with the stored hash.

    Returns:
        True  -> Password matches
        False -> Password does not match
    """
    return pwd_context.verify(plain_password,hashed_password)