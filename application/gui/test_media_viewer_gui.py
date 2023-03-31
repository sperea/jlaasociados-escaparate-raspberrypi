import os
import tempfile
import pytest
import unittest
from unittest.mock import MagicMock
from PIL import Image
from application.gui.media_viewer_gui import MediaViewerGUI
import unittest.mock

@pytest.fixture
def sample_media():
    with tempfile.TemporaryDirectory() as tmpdir:
        image_file = os.path.join(tmpdir, "image.jpg")

        with Image.new("RGB", (10, 10)) as img:
            img.save(image_file)

        yield tmpdir

@pytest.fixture
def media_viewer(sample_media):
    with unittest.mock.patch("tkinter.Tk.mainloop"):
        viewer = MediaViewerGUI(sample_media, image_time=0.5)
    yield viewer
    viewer.exit_program(None)

def test_init(media_viewer):
    assert media_viewer is not None
    assert media_viewer.window_open

#def test_exit_program(media_viewer):
#    with unittest.mock.patch.object(media_viewer, "exit_program", wraps=media_viewer.exit_program) as mock_exit_program:
#        media_viewer.window.event_generate("<Escape>")
#        media_viewer.window.update()
#        
#    mock_exit_program.assert_called_once()

def test_show_image(media_viewer, sample_media):
    image_file = os.path.join(sample_media, "image.jpg")
    media_viewer.show_image(image_file)
    assert media_viewer.img_object is not None

@pytest.mark.skip(reason="Testing video display requires testing the cv2 library, which is out of scope")
def test_show_video(media_viewer):
    pass