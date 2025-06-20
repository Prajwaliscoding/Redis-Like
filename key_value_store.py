import json  

class KVStore:
    def __init__(self, file_path="kv_store.aof"):
        self.store = {}
        self.file_path = file_path
        self._load() 

    def _load(self):
        """Load data from disk on startup"""
        try:
            with open(self.file_path, "r") as f:
                for line in f:
                    command = json.loads(line.strip())
                    if command["op"] == "set":
                        self.store[command["key"]] = command["value"]
        except FileNotFoundError:
            pass 

    def _append_to_log(self, op, key, value):
        """Log operations to disk"""
        with open(self.file_path, "a") as f:
            f.write(json.dumps({"op": op, "key": key, "value": value}) + "\n")

    def set(self, key, value):
        self.store[key] = value
        self._append_to_log("set", key, value) 

    def get(self, key):
        return self.store.get(key, None)