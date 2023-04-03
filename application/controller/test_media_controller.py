import os
import tempfile
import pytest
from PIL import Image
from application.controller.media_controller import MediaController 
from application.infrastructure.local_storage import ImageExtensions
from application.infrastructure.local_storage import VideoExtensions

@pytest.fixture
def sample_media():
    with tempfile.TemporaryDirectory() as tmpdir:
        image_file = os.path.join(tmpdir, "image.jpg")
        video_file = os.path.join(tmpdir, "video.mp4")

        with Image.new("RGB", (10, 10)) as img:
            img.save(image_file)

        with open(video_file, "wb") as f:
            f.write(b"\x00" * 100)

        yield tmpdir

def test_get_file_extension():
    assert MediaController.get_file_extension("file.jpg") == ".jpg"
    assert MediaController.get_file_extension("file.mp4") == ".mp4"
    assert MediaController.get_file_extension("file.unknown") == ".unknown"

def test_image_extensions_contains():
    assert ImageExtensions.contains(".jpg")
    assert ImageExtensions.contains(".JPG")
    assert not ImageExtensions.contains(".mp4")
    assert not ImageExtensions.contains(".unknown")

def test_video_extensions_contains():
    assert VideoExtensions.contains(".mp4")
    assert VideoExtensions.contains(".MP4")
    assert not VideoExtensions.contains(".jpg")
    assert not VideoExtensions.contains(".unknown")

def test_get_media_files(sample_media):
    controller = MediaController(sample_media)
    media_files = controller.get_media_files()

    assert len(media_files) == 2
    assert any(file.endswith(".jpg") for file in media_files)
    assert any(file.endswith(".mp4") for file in media_files)

def test_resize_image():
    img = Image.new("RGB", (100, 100))
    resized_img = MediaController.resize_image(img, 50, 50)

    assert resized_img.width == 50
    assert resized_img.height == 50

    img = Image.new("RGB", (100, 200))
    resized_img = MediaController.resize_image(img, 50, 50)

    assert resized_img.width == 25
    assert resized_img.height == 50

    img = Image.new("RGB", (200, 100))
    resized_img = MediaController.resize_image(img, 50, 50)

    assert resized_img.width == 50
    assert resized_img.height == 25