import gdown
import os

os.makedirs("models", exist_ok=True)


def download_model(file_id, name):
   
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, f"models/{name}")


# https://drive.google.com/drive/folders/10ctqnrEiQLrZ0XdTCo7u78XFHM670Eh8?usp=sharing
download_model("10ctqnrEiQLrZ0XdTCo7u78XFHM670Eh8", "google")
# https://drive.google.com/drive/folders/1drHBlYnZcFEuAKs6o_g7hWqdPQqV36Gc?usp=sharing
download_model("1drHBlYnZcFEuAKs6o_g7hWqdPQqV36Gc", "resnet50")
# https://drive.google.com/drive/folders/1Pi6TLH6bBi_oFKJeO7H1Vgb0JIK7VH_f?usp=sharing
download_model("1Pi6TLH6bBi_oFKJeO7H1Vgb0JIK7VH_f", "facebook")

