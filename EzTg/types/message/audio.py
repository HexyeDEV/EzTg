from .photosize import PhotoSize


class Audio:
    """Represents an audio file to be treated as music by the Telegram clients.

    Attributes
    ----------
    file_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    file_unique_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    duration: `int`
        Duration of the audio in seconds as defined by sender.
    performer: `str`
        Optional. Performer of the audio as defined by sender or by audio tags.
    title: `str`
        Optional. Title of the audio as defined by sender or by audio tags.
    file_name: `str`
        Optional. Original filename as defined by sender.
    mime_type: `str`
        Optional. MIME type of the file as defined by sender.
    file_size: `int`
        Optional. File size.
    thumb: `PhotoSize`
        Optional. Thumbnail of the album cover to which the music file belongs.
    """

    def __init__(self, data):
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.duration = data["duration"]
        self.performer = data.get("performer")
        self.title = data.get("title")
        self.file_name = data.get("file_name")
        self.mime_type = data.get("mime_type")
        self.file_size = data.get("file_size")
        self.thumb = data.get("thumb")
        if self.thumb:
            self.thumb = PhotoSize(self.thumb)
