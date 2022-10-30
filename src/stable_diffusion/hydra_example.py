import hydra
from utils import print_log, config_dir
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path=join(config_dir, "stable_diffusion"), config_name="stable_diffusion", version_base=None)
def main(conf: DictConfig) -> None:
    print_log(f"{conf = }")

if __name__ == "__main__":
    main()
