import os
import cv2
from rich import print
from rich.progress import track

def get_all_img(path):
    f"""
    Get all image files path from a directory.
    
    :param path: Path of the image directory
    :return img_path: An array of all path of images in {path} 
    """
    imgs = os.listdir(path)
    img_path = []
    for image in imgs:
        img_path.append(f'{path}{image}')
    return img_path

def progress_bar(size,status):
    """
    A progress bar that show the statut of the images conversion

    :param size: The number of the images that we need to convert.
    :param status: The number of the images that has been converted.
    :return:
    """
    pourcent = (status/size) * 100
    if pourcent >= 0 and pourcent < 20:
        print("[bold red]Status[/bold red]")
        print("๐ฅโฌโฌโฌโฌโฌโฌโฌโฌโฌโฌโฌโฌ๏ธ")
    elif pourcent >= 20 and pourcent <= 30:
        print("[bold orange]Status[/bold orange]")
        print("๐ง๐ง๐ง๐งโฌโฌโฌโฌโฌโฌโฌโฌโฌ๏ธ")
    elif pourcent >= 30 and pourcent <= 40:
        print("[bold orange]Status[/bold orange]")
        print("๐ง๐ง๐ง๐ง๐ง๐ง๐งโฌโฌโฌโฌโฌ๏ธโฌ๏ธ")
    elif pourcent >= 40 and pourcent <= 60:
        print("[bold yellow]Status[/bold yellow]")
        print("๐จ๐จ๐จ๐จ๐จ๐จ๐จ๐จโฌโฌโฌโฌโฌ๏ธ")
    elif pourcent >= 60 and pourcent <= 80:
        print("[bold blue]Status[/bold blue]")
        print("๐ฆ๐ฆ๐ฆ๐ฆ๐ฆ๐ฆ๐ฆ๐ฆ๐ฆ๐ฆ๐ฆโฌโฌ๏ธ")
    else:
        print("[bold green]Status[/bold green]")
        print("๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๐ฉ๏ธ")