from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


sqlite_db_path = '../.dbs/alch.sqlite'
sqlite_url = f"sqlite:///{sqlite_db_path}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# is needed only for SQLite
connect_args = {"check_same_thread": False}

engine = create_engine(
    sqlite_url, connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
