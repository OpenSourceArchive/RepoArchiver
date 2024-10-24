import pathlib
import logging
import sqlite3

logger = logging.getLogger(__name__)

class CacheManager:
    def __init__(self): 
        if not self.__setup__():
            raise Exception("Failed to setup cache")
    
    def __setup__(self):
        try:
            self.conn = sqlite3.connect(f"{pathlib.Path(__file__).parent}\\cache.db")
            self.cursor = self.conn.cursor()
            
            logger.info("__SETUP__ : Setting up github schema")
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS github_config (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT NOT NULL,
                    value TEXT NOT NULL
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS github_keywords (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    keyword TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    rules TEXT NULL
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS github_whitelisted (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    url TEXT NOT NULL,
                    score INTEGER NOT NULL
                )
            """)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS github_blacklisted (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    reason TEXT NOT NULL
                )
            """)
            
            return True
        except Exception as e:
            logger.error(f"__SETUP__ : {e}")
            return False
    
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