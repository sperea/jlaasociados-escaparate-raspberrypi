from PIL import Image
from media_viewer import MediaViewer

class TestMediaViewer:

    def setup_method(self):
        self.viewer = MediaViewer("", image_time=0)
        self.original_image = Image.new("RGB", (100, 50), color="red")

    def test_resize_image_no_resize_needed(self):
        resized_image = self.viewer.resize_image(self.original_image, 200, 100)
        assert resized_image.size == self.original_image.size

    def test_resize_image_width_bound(self):
        resized_image = self.viewer.resize_image(self.original_image, 50, 100)
        assert resized_image.size == (50, 25)

    def test_resize_image_height_bound(self):
        resized_image = self.viewer.resize_image(self.original_image, 200, 25)
        assert resized_image.size == (50, 25)

    def test_resize_image_both_dimensions_bound(self):
        resized_image = self.viewer.resize_image(self.original_image, 50, 10)
        assert resized_image.size == (20, 10)