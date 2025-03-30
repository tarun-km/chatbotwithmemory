import sqlite3

class MemoryManager:
    def __init__(self):
        self.conn = sqlite3.connect("chatbot_memory.db")
        self.cursor = self.conn.cursor()
        self._initialize_db()

    def _initialize_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT,
                response TEXT
            )
        """)
        self.conn.commit()

    def save_interaction(self, prompt, response):
        self.cursor.execute("""
            INSERT INTO conversations (prompt, response) VALUES (?, ?)
        """, (prompt, response))
        self.conn.commit()

    def get_context(self):
        self.cursor.execute("SELECT prompt, response FROM conversations ORDER BY id DESC LIMIT 5")
        return self.cursor.fetchall()
