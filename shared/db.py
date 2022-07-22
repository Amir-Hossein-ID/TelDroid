from redis import Redis
import sqlite3

class RedisDB():
    def __init__(self, url, password):
        host = ":".join(url.split(':')[:-1])
        port = url.split(':')[-1]
        self.redis = Redis(host=host, port=port, password=password)
        self._local = {}
        self._fill_local()
    
    def _fill_local(self):
        for key in self.redis.keys():
            self._local[key] = self.redis.get(key)

    def get(self, key, default=None):
        if default != None:
            return self._local.get(key, default)
        else:
            return self._local.get(key)

    def set(self, key, value):
        self.redis.set(key, value)
        self._local[key] = value

    def delete(self, key):
        self.redis.delete(key)
        del self._local[key]

    def get_all(self):
        return self._local.keys()

class SQLiteDB():
    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (key TEXT, value TEXT)")
        self._local = {}
        self._fill_local()

    def _fill_local(self):
        for key, value in self.cursor.execute("SELECT * FROM data"):
            self._local[key] = value

    def get(self, key, default=None):
        if default != None:
            return self._local.get(key, default)
        else:
            return self._local.get(key)

    def set(self, key, value):
        self.cursor.execute("INSERT OR REPLACE INTO data VALUES (?, ?)", (key, value))
        self.conn.commit()
        self._local[key] = value

    def delete(self, key):
        self.cursor.execute("DELETE FROM data WHERE key = ?", (key,))
        self.conn.commit()
        del self._local[key]

    def get_all(self):
        return self._local.keys()