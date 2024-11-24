import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://postgres:1234@localhost/todo_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


