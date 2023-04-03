# local_media_storage.py

import os
from application.infrastructure.media_storage import MediaStorage


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


class LocalImageStorage(MediaStorage):

    def get_media_files(self, folder):
        media_files = []

        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file_path)[1]

                if ImageExtensions.contains(file_extension):
                    media_files.append(file_path)

        return media_files


class LocalVideoStorage(MediaStorage):

    def get_media_files(self, folder):
        media_files = []

        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file_path)[1]

                if VideoExtensions.contains(file_extension):
                    media_files.append(file_path)

        return media_files