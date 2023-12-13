import os
import sqlite3
from enum import Enum

from model.db.database_extensions import DatabaseExtensions


class DatabaseFactoryEnum(Enum):
    PROD = 0
    DEV = 1


class DatabaseFactory:
    @staticmethod
    def new_connection(env: DatabaseFactoryEnum):
        extensions = DatabaseExtensions()
        extensions.apply_extensions()
        if env == DatabaseFactoryEnum.PROD:
            check_if_in_cwd("app_data")
            return sqlite3.connect(
                "app_data/linkedinnotesdb.dat", detect_types=sqlite3.PARSE_DECLTYPES
            )
        elif env == DatabaseFactoryEnum.DEV:
            return sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
        else:
            raise TypeError()

    @staticmethod
    def migrate(conn: sqlite3.Connection):
        migrations = get_migrations()
        for migration_path in migrations:
            with open(migration_path, "r") as file:
                sql = file.read()
                cur = conn.cursor()
                cur.execute(sql)
                conn.commit()


def check_if_in_cwd(dir: str):
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, dir)
    if os.path.exists(full_path) and os.path.isdir(full_path):
        return
    else:
        os.makedirs(full_path, exist_ok=True)


def get_migrations():
    migrations_dir = os.path.join(os.getcwd(), "src/model/db/migrations")
    migrations = [
        os.path.join(migrations_dir, migration)
        for migration in os.listdir(migrations_dir)
    ]
    migrations.sort()
    return migrations
