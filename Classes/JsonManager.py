import json

class JsonManager:
    def __init__(self, path):
        self.path = path
        self.data = self.load()
        
    def load(self):
        with open(self.path, 'r') as f:
            return json.load(f)
        
    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)
            
    def getData(self):
        return self.data

