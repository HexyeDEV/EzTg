class File:
    """This object represents a file ready to be downloaded. The file can be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling `getFile`.

    Attributes
    ----------
    file_id: `str`
        Unique identifier for this file.
    file_unique_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_size: `int`
        Optional. File size, if known.
    file_path: `str`
        Optional. File path. Use `https://api.telegram.org/file/bot<token>/<file_path>` to get the file.
    """

    def __init__(self, data):
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.file_size = data.get("file_size")
        self.file_path = data.get("file_path")
