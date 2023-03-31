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