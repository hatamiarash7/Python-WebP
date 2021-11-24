"""Convert images to WebP format"""

from pathlib import Path
from PIL import Image


def convert_to_webp(source):
    """Convert image to webp.

    Args:
        source (pathlib.Path): Path to source image

    Returns:
        pathlib.Path: path to new image
    """
    destination = source.with_suffix(".webp")

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination


def main():
    """Search for PNG/JPG images and convert them using convert_to_webp()"""

    paths = Path("images").glob("**/*.png")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)

    paths = Path("images").glob("**/*.jpg")
    for path in paths:
        webp_path = convert_to_webp(path)
        print(webp_path)


main()
