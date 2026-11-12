import os

import mysql.connector


def db_connection():
    """Connect to MySQL. Override the defaults with DB_* environment variables."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "MHC"),
    )
