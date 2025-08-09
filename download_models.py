import gdown
import os

os.makedirs("models", exist_ok=True)


def download_folder(folder_id, output_dir):
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    gdown.download_folder(url, output=output_dir, quiet=False, use_cookies=False)


download_folder("10ctqnrEiQLrZ0XdTCo7u78XFHM670Eh8", "models/google")

download_folder("1drHBlYnZcFEuAKs6o_g7hWqdPQqV36Gc", "models/resnet50")

download_folder("1Pi6TLH6bBi_oFKJeO7H1Vgb0JIK7VH_f", "models/facebook")


