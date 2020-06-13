from pathlib import Path
import os


# by default we store data relative to where lagtraj is invoked from
DEFAULT_ROOT_DATA_PATH = Path(os.getcwd()) / "data"


DATA_TYPE_PLURAL = dict(trajectory="trajectories", domain="domains", forcing="forcings")


def build_data_path(root_data_path, data_type):
    data_type_plural = DATA_TYPE_PLURAL[data_type]
    return Path(root_data_path) / data_type_plural
