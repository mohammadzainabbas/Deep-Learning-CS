from os.path import join
from utils import print_log, config_dir
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(config_path=join(config_dir, "stable_diffusion"), config_name="stable_diffusion", version_base=None)
def main(conf: DictConfig) -> None:

    verbose = conf.get("verbose", False) 

    if verbose: print_log(f"Configurations loaded via Hydra!\n{conf = }")


if __name__ == "__main__":
    main()
