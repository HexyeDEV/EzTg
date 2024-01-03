from .photosize import PhotoSize


class Animation:
    """Represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Attributes
    ----------
    file_id: `str`
        Identifier for this file, which can be used to download or reuse the file.
    file_unique_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    width: `int`
        Video width as defined by sender.
    height: `int`
        Video height as defined by sender.
    duration: `int`
        Duration of the video in seconds as defined by sender.
    thumb: `PhotoSize`
        Optional. Animation thumbnail as defined by sender.
    file_name: `str`
        Optional. Original animation filename as defined by sender.
    mime_type: `str`
        Optional. MIME type of the file as defined by sender.
    file_size: `int`
        Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    """

    def __init__(self, data):
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.width = data["width"]
        self.height = data["height"]
        self.duration = data["duration"]
        self.thumb = data.get("thumb")
        if self.thumb:
            self.thumb = PhotoSize(self.thumb)
        self.file_name = data.get("file_name")
        self.mime_type = data.get("mime_type")
        self.file_size = data.get("file_size")
