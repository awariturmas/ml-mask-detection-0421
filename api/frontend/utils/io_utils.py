from pyaml import yaml


def load_config(path="./config/config.yml"):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config
