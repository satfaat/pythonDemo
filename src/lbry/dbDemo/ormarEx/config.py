import sqlalchemy
import databases


# Initialization
DATABASE_URL = "sqlite:///.tmp/db.sqlite"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
