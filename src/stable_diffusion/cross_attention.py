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


def init_attention_weights(weight_tuples):
    tokens_length = clip_tokenizer.model_max_length
    weights = torch.ones(tokens_length)
    
    for i, w in weight_tuples:
        if i < tokens_length and i >= 0:
            weights[i] = w
    
    
    for name, module in unet.named_modules():
        module_name = type(module).__name__
        if module_name == "CrossAttention" and "attn2" in name:
            module.last_attn_slice_weights = weights.to(device)
        if module_name == "CrossAttention" and "attn1" in name:
            module.last_attn_slice_weights = None
    

@hydra.main(config_path=join(config_dir, "stable_diffusion"), config_name="stable_diffusion", version_base=None)
def main(conf: DictConfig) -> None:

    verbose, show_config = conf.get("verbose", False), conf.get("show_config", False)
    if show_config: print_log(f"Configurations loaded via Hydra!\n\n{conf = }\n\n")
    
    device = "cuda" if torch.cuda.is_available() and conf.get("use_gpu", True) else "cpu"
    if verbose: print_log(f"Using {device = }")

    # Huggingface Authentication Token
    auth_token = conf.auth_token

    # Initialise CLIP tokenizer and model
    clip_tokenizer = CLIPTokenizer.from_pretrained(conf.clip_model)
    clip_model = CLIPModel.from_pretrained(conf.clip_model, torch_dtype=torch.float16)
    clip = clip_model.text_model

    # Initialise Stable diffusion model
    unet = UNet2DConditionModel.from_pretrained(conf.diffusion_model, subfolder="unet", use_auth_token=auth_token, revision="fp16", torch_dtype=torch.float16)
    vae = AutoencoderKL.from_pretrained(conf.diffusion_model, subfolder="vae", use_auth_token=auth_token, revision="fp16", torch_dtype=torch.float16)

    # Move to GPU (if available)
    unet = unet.to(device)
    vae = vae.to(device)
    clip = clip.to(device)

    if verbose: print_log(f"CLIP and diffusion models loaded")


    

if __name__ == "__main__":
    main()
