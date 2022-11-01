from os.path import join, exists, dirname, abspath, basename, relpath
from os import getcwd, pardir

def print_log(text: str): print(f"[ log ]: {text}")
def print_error(text: str): print(f"[ error ]: {text}")

parent_dir = abspath(join(join(join(abspath(__file__), pardir), pardir), pardir))
config_dir = join(parent_dir, "configs")