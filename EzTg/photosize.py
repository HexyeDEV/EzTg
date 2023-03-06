class PhotoSize:
    """Represents one size of a photo or a file / sticker thumbnail.

    Attributes
    ----------

    file_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    width: `int`
        Photo width.
    height: `int`
        Photo height.
    file_size: `int`
        Optional. File size.
    """

    def __init__(self, data):
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.width = data["width"]
        self.height = data["height"]
        self.file_size = data.get("file_size")
