import sqlite3

# if we use this class with context manager "with"  use 2 dender method __enter__ and __exit__
class DatabaseConnection:
    def __init__(self,host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
