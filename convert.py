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
        PIL.Image: Base image with watermark
    """
    image = Image.open(image_path)
    watermark = Image.open(watermark)

    multiplier = 0.05 if image.size[0] > image.size[1] else 0.1
    new_width = int(image.size[0] * multiplier)
    new_height = int(watermark.size[1] *
                     (new_width / float(watermark.size[0])))
    watermark = watermark.resize((new_width, new_height), Image.ANTIALIAS)

    position = ((image.size[0] - 15 - new_width),
                (image.size[1] - 15 - new_height))
    image.paste(watermark, position, watermark)
    return image


def get_image_paths(directory):
    """Get image file paths in the given directory

    Args:
        directory (str): Path to the directory containing images

    Returns:
        list: List of pathlib.Path objects representing image files
    """
    return list(filter(lambda p: p.suffix in {".jpg", ".jpeg", ".png"}, Path(directory).glob("*")))


def process_image(image_path, watermark_path):
    """Process the given image by adding watermark and converting to webp format

    Args:
        image_path (pathlib.Path): Base image file path
        watermark_path (pathlib.Path): Watermark file path
    """
    print("Convert ", image_path)
    image = add_watermark(image_path, watermark_path)
    convert_to_webp(image_path, image)


def main():
    """Search for PNG/JPG images then
        - Add watermark
        - Convert to WebP format
    """

    image_paths = get_image_paths("images")
    watermark_path = 'logo.png'

    for path in image_paths:
        process_image(path, watermark_path)


if __name__ == "__main__":
    main()
