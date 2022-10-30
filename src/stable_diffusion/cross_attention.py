from tabnanny import verbose
import torch
from transformers import CLIPModel, CLIPTextModel, CLIPTokenizer
from diffusers import AutoencoderKL, UNet2DConditionModel
from os.path import join
from utils import print_log, config_dir
import hydra
from omegaconf import DictConfig, OmegaConf
import numpy as np
import random
from PIL import Image
from diffusers import LMSDiscreteScheduler
from tqdm.auto import tqdm
from torch import autocast
from difflib import SequenceMatcher
from IPython.display import display
import requests
from io import BytesIO

@hydra.main(config_path=join(config_dir, "stable_diffusion"), config_name="stable_diffusion", version_base=None)
def main(conf: DictConfig) -> None:

    verbose = conf.get("verbose", False) 
    if verbose: print_log(f"Configurations loaded via Hydra!\n\n{conf = }\n\n")

    # Huggingface Authentication Token
    auth_token = conf.auth_token

    # Initialise CLIP tokenizer and model
    clip_tokenizer = CLIPTokenizer.from_pretrained(conf.clip_model)
    clip_model = CLIPModel.from_pretrained(model_path_clip, torch_dtype=torch.float16)
    clip = clip_model.text_model

    # Initialise Stable diffusion model
    unet = UNet2DConditionModel.from_pretrained(model_path_diffusion, subfolder="unet", use_auth_token=auth_token, revision="fp16", torch_dtype=torch.float16)
    vae = AutoencoderKL.from_pretrained(model_path_diffusion, subfolder="vae", use_auth_token=auth_token, revision="fp16", torch_dtype=torch.float16)


    

if __name__ == "__main__":
    main()
