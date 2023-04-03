# media_storage.py

from abc import ABC, abstractmethod

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

class MediaStorage(ABC):

    @abstractmethod
    def get_media_files(self, folder):
        pass