import pathlib
import logging
import sqlite3

logger = logging.getLogger(__name__)

class CacheManager:
    def __init__(self): 
        self.__setup__()
    
    def __setup__(self):
        try:
            self.conn = sqlite3.connect(f"{pathlib.Path(__file__).parent}\\cache.db")
            self.cursor = self.conn.cursor()
            
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS github_visited (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            """)
            logger.info("__SETUP__ : ")
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS github_tracking (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    plataform TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            """)
        except Exception as e:
            logger.error(f"__SETUP__ : {e}")
    
    def using_squema(self, schema: str):
        return self.SchemaEmulator(schema)
    
    class SchemaEmulator:
        def __init__(self, schema: str):
            self.conn = super().conn
            self.cursor = self.conn.cursor()
            self.schema_name = schema
        
        def from_table(self, table: str):
            self.table_name = table
            return self
        
        def get(self, key: str, value: str):
            self.cursor.execute(f"SELECT * FROM {self.schema_name}_{self.table_name} WHERE {key} = '{value}'")
            return self.cursor.fetchone()