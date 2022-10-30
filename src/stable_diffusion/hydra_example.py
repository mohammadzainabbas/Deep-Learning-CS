import hydra
from os.path import join
from omegaconf import DictConfig, OmegaConf

def print_log(text: str): print(f"[ log ]: {text}")
def print_error(text: str): print(f"[ error ]: {text}")

config_dir = join(hydra.utils.get_original_cwd(), "config")

@hydra.main(config_path=join(config_dir, "stable_diffusion"), config_name="stable_diffusion", version_base=None)
def main(conf: DictConfig) -> None:
    print_log(f"{conf = }")

if __name__ == "__main__":
    main()
