from .. import pwd_context

def generate_hash(text: str) -> str:
    return pwd_context.hash(text)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
