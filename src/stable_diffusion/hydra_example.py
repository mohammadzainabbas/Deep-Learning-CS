import hydra
from os.path import join
from omegaconf import DictConfig, OmegaConf

def print_log(text: str): print(f"[ log ]: {text}")
def print_error(text: str): print(f"[ error ]: {text}")

@hydra.main(config_path="../../configs/stable_diffusion", config_name="stable_diffusion", version_base=None)
def main(conf: DictConfig) -> None:

    print_log(f"{conf = }")
    config = OmegaConf.to_yaml(conf, resolve=True)
    print_log(f"{config = }")
    print(config)

if __name__ == "__main__":
    main()
