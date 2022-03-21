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

    image = Image.open(source)
    image.save(destination, format="webp")


def main():
    """Search for PNG/JPG images and convert them using convert_to_webp()"""

    for path in filter(lambda p: p.suffix in {".jpg", ".png"}, Path("images").glob("*")):
        convert_to_webp(path)
        print("Convert ", path)


if __name__ == "__main__":
    main()
