import json
import os

def load_config(filename):
    default_config = {
        "app_name": "DefaultApp",
        "version": "1.0",
        "settings": {
            "theme": "light",
            "language": "en"
        }
    }
    if not os.path.exists(filename):
        return default_config
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return default_config

def save_config(filename, config):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

config = load_config("config.json")
config["settings"]["theme"] = "dark"
save_config("config.json", config)