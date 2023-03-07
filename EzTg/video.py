from .photosize import PhotoSize

class Video:
    """Represents a video file.
    
    Attributes
    ----------
    file_id: `str`
        Unique identifier for this file.
    file_unique_id: `str`
        Unique identifier for this file.
    width: `int`
        Video width as defined by sender.
    height: `int`
        Video height as defined by sender.
    duration: `int`
        Duration of the video in seconds as defined by sender.
    thumb: `PhotoSize`
        Optional. Video thumbnail.
    file_name: `str`
        Optional. Original filename as defined by sender.
    mime_type: `str`
        Optional. MIME type of the file as defined by sender.
    file_size: `int`
        Optional. File size.
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
        