# media_controller.py

import os
import os.path
import time
from PIL import Image
from application.controller.media_handler import ImageHandler
from application.controller.media_handler import VideoHandler

class ImageExtensions:
    EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}

    @classmethod
    def contains(cls, extension):
        return extension.lower() in cls.EXTENSIONS


class VideoExtensions:
    EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov"}

    @classmethod
    def contains(cls, extension):
        return extension.lower() in cls.EXTENSIONS

class MediaController:
    def __init__(self, media_folder, image_time=2):
        self.media_folder = media_folder
        self.image_time = image_time
        self.image_handler = ImageHandler(self.resize_image)
        self.video_handler = VideoHandler(self.resize_image)

    @staticmethod
    def get_file_extension(file_path):
        _, file_extension = os.path.splitext(file_path)
        return file_extension

    @staticmethod
    def resize_image(image, max_width, max_height):
        width_ratio = max_width / image.width
        height_ratio = max_height / image.height
        min_ratio = min(width_ratio, height_ratio)

        new_width = int(image.width * min_ratio)
        new_height = int(image.height * min_ratio)

        return image.resize((new_width, new_height), Image.ANTIALIAS)

    def get_media_files(self):
        media_files = []

        for root, _, files in os.walk(self.media_folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = self.get_file_extension(file_path)

                if ImageExtensions.contains(file_extension) or VideoExtensions.contains(file_extension):
                    media_files.append(file_path)

        return media_files

    def show_media(self):
        media_files = self.get_media_files()
        self.index = 0

        while True:
            if self.index >= len(media_files):
                self.index = 0

            file_path = media_files[self.index]
            file_extension = self.get_file_extension(file_path)

            if ImageExtensions.contains(file_extension):
                self.image_handler.show(file_path)
            elif VideoExtensions.contains(file_extension):
                self.video_handler.show(file_path)

            self.index += 1
            time.sleep(self.image_time)