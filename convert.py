"""Convert images to WebP format"""

from pathlib import Path
from PIL import Image


def convert_to_webp(source, image):
    """Convert image to webp.

    Args:
        source (pathlib.Path): Path to source image
        image (PIL.Image): Base image with watermark
    """

    destination = source.with_suffix(".webp")
    image.save(destination, format="webp")


def add_watermark(image_path, watermark):
    """Add logo watermark to given image

    Args:
        image_path (pathlib.Path): Base image file path
        watermark (pathlib.Path): Watermark file path

    Returns:
        image (PIL.Image): Base image with watermark
    """
    image = Image.open(image_path)
    watermark = Image.open(watermark)

    if image.size[0] > image.size[1]:
        multiplier = 0.05
    else:
        multiplier = 0.1

    new_width = int(image.size[0] * multiplier)
    concat = (new_width / float(watermark.size[0]))
    new_height = int((float(watermark.size[1])*float(concat)))
    watermark = watermark.resize((new_width, new_height), Image.ANTIALIAS)

    position = ((image.size[0] - 15 - new_width),
                (image.size[1] - 15 - new_height))
    image.paste(watermark, position, watermark)
    return image


def main():
    """Search for PNG/JPG images and convert them using convert_to_webp()"""

    for path in filter(lambda p: p.suffix in {".jpg", ".jpeg", ".png"}, Path("images").glob("*")):
        print("Convert ", path)
        image = add_watermark(path, 'logo.png')
        convert_to_webp(path, image)


if __name__ == "__main__":
    main()
