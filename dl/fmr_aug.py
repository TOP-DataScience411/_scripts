from matplotlib import pyplot as plt
from numpy import savez_compressed
from PIL.Image import (
    fromarray,
    Image, 
    Resampling,
)
from PIL.ImageEnhance import (
    Brightness,
    Color,
    Contrast,
    Sharpness,
)
from sklearn.model_selection import train_test_split

from math import cos, radians, sin
from random import (
    choice,
    randrange as rr,
    sample,
    uniform,
)

from fmr_load import coerse_images, load_images, script_dir


def show_two_images(img1: Image, img2: Image, dpi: float = 100):
    """"""
    width = max(img1.width, img2.width)
    height = max(img1.height, img2.height)
    
    fig = plt.figure(
        figsize=(width/dpi*2.2*4, height/dpi*1.1*4),
        layout='tight'
    )
    axs = fig.subplots(1, 2)
    
    # breakpoint()
    
    # axs[0].set_xlim(0, width)
    # axs[0].set_ylim(0, height)
    axs[0].imshow(img1)
    axs[0].set_axis_off()
    # axs[1].set_xlim(0, width)
    # axs[1].set_ylim(0, height)
    axs[1].imshow(img2)
    axs[1].set_axis_off()
    
    plt.show()
    plt.close()


def rand_crop(img: Image, max_crop_percent: float = 0.07) -> Image:
    max_crop_x = int(img.width * max_crop_percent)
    max_crop_y = int(img.height * max_crop_percent)
    return img.crop(
        box=(
            0 + rr(max_crop_x),
            0 + rr(max_crop_y),
            img.width - rr(max_crop_x),
            img.height - rr(max_crop_y),
        )
    )


def rand_angle(
        img: Image, 
        min_angle: float = 2, 
        max_angle: float = 7, 
        auto_crop: bool = True
) -> Image:
    angle = uniform(min_angle, max_angle)
    img_rot = img.rotate(
        angle=choice([1, -1])*angle,
        resample=Resampling.BICUBIC,
        expand=True,
    )
    # breakpoint()
    if auto_crop:
        angle = radians(abs(angle))
        img_rot = img_rot.crop(
            box=(
                sin(angle)*img.height,
                sin(angle)*img.width,
                cos(angle)*img.width,
                cos(angle)*img.height,
            )
        )
    return img_rot


def rand_scale(
        img: Image, 
        min_scale_percent: float = 0.05, 
        max_scale_percent: float = 0.1
) -> Image:
    scale_coef = 1 + choice([1, -1])*uniform(min_scale_percent, max_scale_percent)
    img_sc = img.resize(
        size=(
            round(img.width*scale_coef), 
            round(img.height*scale_coef)
        ),
        resample=Resampling.BICUBIC,
    )
    # breakpoint()
    return img_sc


def rand_bright(
        img: Image, 
        min_factor_delta: float = 0.05, 
        max_factor_delta: float = 0.20
) -> Image:
    factor = 1 + choice([-1, 1])*uniform(min_factor_delta, max_factor_delta)
    return Brightness(img).enhance(factor)


def rand_color(
        img: Image, 
        min_factor_delta: float = 0.1, 
        max_factor_delta: float = 0.3
) -> Image:
    factor = 1 + choice([-1, 1])*uniform(min_factor_delta, max_factor_delta)
    return Color(img).enhance(factor)


def rand_contrast(
        img: Image, 
        min_factor_delta: float = 0.05, 
        max_factor_delta: float = 0.25
) -> Image:
    factor = 1 + choice([-1, 1])*uniform(min_factor_delta, max_factor_delta)
    return Contrast(img).enhance(factor)


def rand_sharp(
        img: Image, 
        min_factor_delta: float = 0.25, 
        max_factor_delta: float = 0.5
) -> Image:
    factor = 1 + choice([-1, 1])*uniform(min_factor_delta, max_factor_delta)
    return Sharpness(img).enhance(factor)


geom_transforms = [
    [rand_angle],
    [rand_scale, rand_angle],
    [rand_crop, rand_scale],
]
color_transforms = [
    rand_bright,
    rand_color,
    rand_contrast,
    rand_sharp
]


def rand_tranform(img: Image, min_transforms: int = 2) -> Image:
    tranforms = (
        choice(geom_transforms)
        + 
        sample(color_transforms, rr(min_transforms // 2, len(color_transforms)))
    )
    if rand_angle in tranforms and rand_crop in tranforms:
        tranforms.remove(choice([rand_angle, rand_crop]))
    for func in tranforms:
        # print(func.__name__)
        img = func(img)
    return img


def augment(imgs: list[Image], lbls: list[int]) -> tuple[list[Image], list[int]]:
    """"""
    imgs_aug, lbls_aug = [], []
    for i in range(len(imgs)):
        imgs_aug.append(imgs[i])
        lbls_aug.append(lbls[i])
        for _ in range(rr(1, 3)):
            imgs_aug.append(rand_tranform(imgs[i]))
            lbls_aug.append(lbls[i])
    return imgs_aug, lbls_aug



if __name__ == '__main__':
    
    cars_imgs, cars_lbls = load_images()
    
    # i = rr(len(cars_imgs))
    # (img1, img2), _ = coerse_images(
    #     [cars_imgs[i], rand_tranform(cars_imgs[i])], 
    #     [0, 1], 
    #     128, 
    #     72,
    #     scale=False
    # )
    # show_two_images(fromarray(img1, mode='RGB'), fromarray(img2, mode='RGB'))
    
    x_train, x_test, y_train, y_test = train_test_split(
        cars_imgs, 
        cars_lbls,
        test_size=0.2,
        random_state=1
    )
    
    x_train, y_train = augment(x_train, y_train)
    
    width = min([img.width for img in x_train])
    height = min([img.height for img in x_train])
    
    x_train, y_train = coerse_images(
        x_train, 
        y_train,
        width,
        height,
    )
    x_test, y_test = coerse_images(
        x_test, 
        y_test,
        width,
        height,
    )

    savez_compressed(
        script_dir / 'fmr_aug.npz',
        x_train, 
        y_train,
        x_test,
        y_test,
    )

