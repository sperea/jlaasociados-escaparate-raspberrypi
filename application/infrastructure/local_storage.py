import os
from application.infrastructure.media_storage import MediaStorage


class MediaTypeExtensions:
    @classmethod
    def contains(cls, extension):
        return extension.lower() in cls.EXTENSIONS


class ImageExtensions(MediaTypeExtensions):
    EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}


class VideoExtensions(MediaTypeExtensions):
    EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov"}


class LocalMediaStorage(MediaStorage):
    def get_media_files(self, folder, extensions):
        media_files = []

        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file_path)[1]

                if extensions.contains(file_extension):
                    media_files.append(file_path)

        return media_files


class LocalImageStorage(LocalMediaStorage):
    def get_media_files(self, folder):
        return super().get_media_files(folder, ImageExtensions)


class LocalVideoStorage(LocalMediaStorage):
    def get_media_files(self, folder):
        return super().get_media_files(folder, VideoExtensions)
