import bcrypt

def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against a hashed password."""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

if __name__ == "__main__":
    # Example usage
    password = "test123"
    hashed = hash_password(password)
    print(f"Plain: {password}")
    print(f"Hashed: {hashed}")
    print(f"Verified: {verify_password(password, hashed)}")