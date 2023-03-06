from .photosize import PhotoSize

class Document:
    """Represents a general file (as opposed to photos, voice messages and audio files).
    
    Attributes
    ----------
    file_id: `str`
        Unique file identifier.
    file_unique_id: `str`
        Unique file identifier.
    thumb: `PhotoSize`
        Optional. Document thumbnail as defined by sender.
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
        self.thumb = data.get("thumb")
        if self.thumb:
            self.thumb = PhotoSize(self.thumb)
        self.file_name = data.get("file_name")
        self.mime_type = data.get("mime_type")
        self.file_size = data.get("file_size")