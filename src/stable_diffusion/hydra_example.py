import hydra
from os.path import join, exists, dirname, abspath, basename, relpath
from os import getcwd, pardir
from omegaconf import DictConfig, OmegaConf

def print_log(text: str): print(f"[ log ]: {text}")
def print_error(text: str): print(f"[ error ]: {text}")

parent_dir = dirname(dirname(abspath(__file__)))
print_log(f"{parent_dir = }")
# config_dir = join(, "config")

@hydra.main(config_path=join(config_dir, "stable_diffusion"), config_name="stable_diffusion", version_base=None)
def main(conf: DictConfig) -> None:
    print_log(f"{conf = }")

if __name__ == "__main__":
    main()
