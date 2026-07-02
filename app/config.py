import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_config(path):
    with open(path, 'r') as f:
        return json.load(f)

CONFIG = load_config(os.path.join(BASE_DIR, 'config.json'))