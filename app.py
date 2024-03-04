from Repository import SQLiteRepository
from ProductService import ProductService

repository = SQLiteRepository(db_path="database.db")

repository.connect()

product = ProductService(repository=repository)

print(product.get_all_items())
