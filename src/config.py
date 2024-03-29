import toml
import logging
import os

EXAMPLE_CONFIG="""\"target_file\"=\"\"
\"backup_dir\"=\"\"
[server]
\"host\"=\"\"
\"port\"=21
\"username\"=\"\"
\"password\"=\"\"
"""

def load_config(path="./config.toml"):
    """Loads the config from `path`"""
    if os.path.exists(path) and os.path.isfile(path):
        config = toml.load(path)
        return config
    else:
        with open(path, "w") as config:
            config.write(EXAMPLE_CONFIG)
            logging.warn(
                f"No config file found. Creating a default config file at {path}"
            )
            raise ValueError("Please fill in your config file.")
