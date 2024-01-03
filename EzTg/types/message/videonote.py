from .photosize import PhotoSize


class VideoNote:
    """Represents a video message (available in Telegram apps as of v.4.0).

    Attributes:
        file_id: `str`
            Unique identifier for this file.
        file_unique_id: `str`
            Unique file identifier, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
        length: `int`
            Video width and height as defined by sender.
        duration: `int`
            Duration of the video in seconds as defined by sender.
        thumb: `PhotoSize`
            Optional. Video thumbnail.
        file_size: `int`
            Optional. File size.
    """

    def __init__(self, data):
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.length = data["length"]
        self.duration = data["duration"]
        self.thumb = data.get("thumb")
        if self.thumb:
            self.thumb = PhotoSize(self.thumb)
        self.file_size = data.get("file_size")
