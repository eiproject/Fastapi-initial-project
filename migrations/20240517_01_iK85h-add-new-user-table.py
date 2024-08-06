"""
add new users table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""CREATE TABLE "users"
(
    user_id         SERIAL PRIMARY KEY,
    email           VARCHAR(100) NOT NULL UNIQUE,
    password_hash   VARCHAR(100) NOT NULL,
    date_created    TIMESTAMP NOT NULL,
    date_updated    TIMESTAMP
);""",
    'DROP TABLE "users";')
]
