import tkinter as tk
import unittest.mock
import pytest
from PIL import Image
from io import BytesIO
import cv2
import numpy as np
from application.controller.media_handler import ImageHandler, MediaHandlerError, VideoHandler

# Función de redimensionamiento de imagen simple
def resize_image(image, width, height):
    return image.resize((width, height), Image.LANCZOS)

# Fixture para simular una ventana Tkinter
@pytest.fixture
def window():
    with unittest.mock.patch("tkinter.Tk.mainloop"):
        window = tk.Tk()
    yield window
    window.destroy()


'''
# Fixture para simular un lienzo Tkinter
@pytest.fixture
def canvas(window):
    return tk.Canvas(window)

def test_image_handler_show_valid_image(window, canvas):
    image_handler = ImageHandler(resize_image)
    file_path = "test_image.jpg"
    try:
        image_handler.show(file_path, canvas, window, 300, 300)
    except MediaHandlerError:
        pytest.fail("Unexpected MediaHandlerError")

def test_image_handler_show_invalid_image(window, canvas):
    image_handler = ImageHandler(resize_image)
    file_path = "non_existent_image.jpg"
    with pytest.raises(MediaHandlerError):
        image_handler.show(file_path, canvas, window, 300, 300)


# Pruebas para VideoHandler
def test_video_handler_show_valid_video(window, canvas):
    video_handler = VideoHandler(resize_image)

    # Crear un video de prueba usando OpenCV
    height = width = 100
    video = cv2.VideoWriter("test_video.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    for _ in range(10):
        video.write(frame)
    video.release()

    file_path = "test_video.avi"

    with unittest.mock.patch("tkinter.Canvas.update") as mocked_update:
        video_handler.show(file_path, canvas, window, 300, 300)
        assert mocked_update.called

def test_video_handler_show_invalid_video(window, canvas):
    video_handler = VideoHandler(resize_image)
    file_path = "non_existent_video.avi"

    with unittest.mock.patch("builtins.print") as mocked_print:
        video_handler.show(file_path, canvas, window, 300, 300)
        mocked_print.assert_called_with("Execution canceled by user")
'''