import json

class JsonManager:
    def __init__(self, path):
        self.path = path
        self.data = self.load()
        
    def load(self):
        try:
            fichier = open(self.path, "r")
            return json.load(fichier)
        except FileNotFoundError:
            print("le fichier n'existe pas")
            exit(1)
        
        
    def save(self, data):
        try:
            fichier = open(self.path, "w")
            json.dump(self.data, fichier, indent=4)
        except FileNotFoundError:
            print("le fichier n'existe pas")
            exit(1)
            
    def getData(self):
        return self.data

