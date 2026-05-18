import yaml
import os

# ─────────────────────────────────────────────
#  ConfigReader  –  loads config/config.yaml
#  Usage:  config = ConfigReader().get()
# ─────────────────────────────────────────────

class ConfigReader:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
        with open(config_path) as f:
            self._data = yaml.safe_load(f)   # load YAML into a dict

    def get(self):
        return self._data  # return the config dict to the caller



