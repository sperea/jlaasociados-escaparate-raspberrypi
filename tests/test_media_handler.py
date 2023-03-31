import pytest
from unittest.mock import patch, MagicMock
from PIL import Image
from lib.media_handler import MediaHandler, ImageHandler, VideoHandler


class DummyCanvas:
    def __init__(self):
        self.img_object = None

    def delete(self, _):
        pass

    def create_image(self, _, __, image, anchor):
        self.img_object = image


class DummyWindow:
    def update(self):
        pass


class TestMediaHandlers:
    @patch('PIL.Image.open')
    def test_image_handler_show(self, mock_open):
        # Arrange
        mock_image = MagicMock()
        mock_open.return_value = mock_image
        image_handler = ImageHandler(self.resize_image)
        original_image_path = "path/to/image.jpg"
        canvas = DummyCanvas()
        window = DummyWindow()
        window_width = 200
        window_height = 100

        # Act
        image_handler.show(original_image_path, canvas,
                            window, window_width, window_height)

        # Assert
        mock_open.assert_called_once_with(original_image_path)
        mock_image.resize.assert_called_once()

    @patch('PIL.Image.open')
    def test_video_handler_show(self, mock_open):
        # Arrange
        mock_image = MagicMock()
        mock_open.return_value = mock_image
        video_handler = VideoHandler(self.resize_image)
        video_path = "path/to/video.mp4"
        canvas = DummyCanvas()
        window = DummyWindow()
        window_width = 200
        window_height = 100

        # Act
        video_handler.show(video_path, canvas, window,
                            window_width, window_height)

        # Assert
        mock_open.assert_called_once_with(video_path)
        mock_image.resize.assert_called_once()

    def test_show_invalid_path(self):
        # Arrange
        media_handler = MediaHandler()
        canvas = DummyCanvas()
        window = DummyWindow()
        window_width = 800
        window_height = 600
        file_path = "invalid_path.jpg"

        # Act & Assert
        with pytest.raises(Exception):
            media_handler.show(file_path, canvas, window,
                               window_width, window_height)

    def resize_image(self, image, width, height):
        aspect_ratio = image.width / image.height

        if image.width > width:
            image_width = width
            image_height = int(image_width / aspect_ratio)
            image = image.resize((image_width, image_height), Image.ANTIALIAS)

        if image.height > height:
            image_height = height
            image_width = int(image_height * aspect_ratio)
            image = image.resize((image_width, image_height), Image.ANTIALIAS)

        return image