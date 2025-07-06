from keras.utils import to_categorical
from numpy import array, ndarray, savez_compressed
from PIL import Image, ImageFile
from PIL.Image import Resampling

from pathlib import Path
from sys import path


script_dir = Path(path[0])
data_dir = script_dir / 'fmr'


# labels:
#   0 — Ferrari
#   1 — Mercedes
#   2 — Renault

def load_images() -> tuple[list[ImageFile], list[int]]:
    """"""
    cars_imgs, cars_lbls = [], []
    for i, subdir in enumerate(data_dir.glob('[!_]*')):
        for img in subdir.iterdir():
            img = Image.open(img)
            cars_imgs.append(img)
            cars_lbls.append(i)
    return cars_imgs, cars_lbls


def coerse_images(
        cars_imgs: list[ImageFile],
        cars_lbls: list[int],
        new_width: int | None = None,
        new_height: int | None = None,
        scale: bool = True,
) -> tuple[ndarray, ndarray]:
    """"""
    resize = new_width is not None and new_height is not None
    for i in range(len(cars_imgs)):
        img = cars_imgs[i]
        if resize:
            img = img.resize((new_width, new_height), Resampling.BICUBIC)
        cars_imgs[i] = array(img)
    
    cars_imgs = array(cars_imgs)
    cars_lbls = array(to_categorical(cars_lbls, num_classes=3))
    
    if scale:
        cars_imgs = cars_imgs / 255
    
    return cars_imgs, cars_lbls


if __name__ == '__main__':
    
    savez_compressed(
        script_dir / 'fmr.npz',
        *coerse_images(*load_images()),
    )

