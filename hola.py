from Repository import SQLiteRepository

repository = SQLiteRepository(db_path="database.db")

repository.connect()