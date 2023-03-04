import unittest
from pathlib import Path
from PIL import Image
from convert import *


class TestImageConversion(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path("test_images")
        self.test_dir.mkdir(exist_ok=True)
        self.image_path = self.test_dir / "test_image.jpg"
        self.watermark_path = self.test_dir / "test_logo.png"
        self.webp_path = self.image_path.with_suffix(".webp")
        self.image_size = (100, 100)
        self.watermark_size = (20, 20)
        self.create_test_images()

    def create_test_images(self):
        image = Image.new("RGB", self.image_size, color="red")
        watermark = Image.new("RGBA", self.watermark_size, color=(0, 0, 0, 0))
        image.save(self.image_path)
        watermark.save(self.watermark_path)

    def tearDown(self):
        self.image_path.unlink(missing_ok=True)
        self.watermark_path.unlink(missing_ok=True)
        self.webp_path.unlink(missing_ok=True)
        self.test_dir.rmdir()

    def test_add_watermark(self):
        image = add_watermark(self.image_path, self.watermark_path)
        self.assertEqual(image.size, self.image_size)

    def test_convert_to_webp(self):
        image = Image.open(self.image_path)
        convert_to_webp(self.image_path, image)
        self.assertTrue(self.webp_path.exists())

    def test_process_image(self):
        process_image(self.image_path, self.watermark_path)
        self.assertTrue(self.webp_path.exists())

    def test_get_image_paths(self):
        image_paths = get_image_paths(self.test_dir)
        self.assertEqual(len(image_paths), 2)
        self.assertEqual(image_paths[0], self.watermark_path)
        self.assertEqual(image_paths[1], self.image_path)


if __name__ == "__main__":
    unittest.main()
