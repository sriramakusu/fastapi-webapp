from passlib.context import CryptContext

#used to verify if plain password and hashed passwords match and create hashed passwords
pwd_context = CryptContext(schemes=["bcrypt"],
                           deprecated = "auto")

class Hasher():
    # Static method that checks if the passwords match
    @staticmethod
    def verify_password(plain_password, hash_password):
        return pwd_context.verify(plain_password, hash_password)
    
    # static method to get the hashed password
    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)