class Voice:
    """This object represents a voice note.

    Attributes
    ----------
    file_id: `str`
        Unique identifier for this file.
    file_unique_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    duration: `int`
        Duration of the audio in seconds as defined by sender.
    mime_type: `str`
        Optional. MIME type of the file as defined by sender.
    file_size: `int`
        Optional. File size in bytes. It can be bigger than 2^31 and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this value.
    """

    def __init__(self, data):
        self.file_id = data['file_id']
        self.file_unique_id = data['file_unique_id']
        self.duration = data['duration']
        self.mime_type = data.get('mime_type')
        self.file_size = data.get('file_size')
