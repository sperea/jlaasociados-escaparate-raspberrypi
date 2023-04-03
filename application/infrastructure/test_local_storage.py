import os
import unittest
from tempfile import TemporaryDirectory
from application.infrastructure.local_storage import LocalImageStorage
from application.infrastructure.local_storage import LocalVideoStorage
from application.infrastructure.local_storage import ImageExtensions
from application.infrastructure.local_storage import VideoExtensions


class TestLocalImageStorage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()

        # Crear archivos de imagen de prueba en la carpeta temporal
        self.test_files = [
            "image1.jpg",
            "image2.png",
            "image3.gif",
            "not_an_image.txt",
            "video.mp4",
        ]

        for file in self.test_files:
            with open(os.path.join(self.temp_dir.name, file), "w") as f:
                f.write("test content")

        self.local_image_storage = LocalImageStorage()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_get_media_files(self):
        media_files = self.local_image_storage.get_media_files(self.temp_dir.name)

        # Comprobar si se encuentran las imágenes correctas
        for file in media_files:
            file_name = os.path.basename(file)
            self.assertIn(file_name, self.test_files)
            self.assertTrue(ImageExtensions.contains(os.path.splitext(file_name)[1]))

        # Comprobar si se ignoran los archivos no válidos
        self.assertEqual(len(media_files), 3)


class TestLocalVideoStorage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()

        # Crear archivos de video de prueba en la carpeta temporal
        self.test_files = [
            "video1.mp4",
            "video2.mkv",
            "video3.avi",
            "video4.mov",
            "not_a_video.txt",
            "image.jpg",
        ]

        for file in self.test_files:
            with open(os.path.join(self.temp_dir.name, file), "w") as f:
                f.write("test content")

        self.local_video_storage = LocalVideoStorage()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_get_media_files(self):
        media_files = self.local_video_storage.get_media_files(self.temp_dir.name)

        # Comprobar si se encuentran los videos correctos
        for file in media_files:
            file_name = os.path.basename(file)
            self.assertIn(file_name, self.test_files)
            self.assertTrue(VideoExtensions.contains(os.path.splitext(file_name)[1]))

        # Comprobar si se ignoran los archivos no válidos
        self.assertEqual(len(media_files), 4)
