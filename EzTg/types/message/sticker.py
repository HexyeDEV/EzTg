from .file import File
from .maskposition import MaskPosition
from .photosize import PhotoSize


class Sticker:
    """This object represents a sticker.

    Attributes
    ----------
    file_id: `str`
        Unique identifier for this file.
    file_unique_id: `str`
        Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    type: `str`
        Type of the sticker, currently one of “regular”, “mask”, “custom_emoji”. The type of the sticker is independent from its format, which is determined by the fields is_animated and is_video.
    width: `int`
        Sticker width.
    height: `int`
        Sticker height.
    is_animated: `bool`
        True, if the sticker is animated.
    is_video: `bool`
        True, if the sticker is a video sticker.
    thumbnail: `PhotoSize`
        Optional. Sticker thumbnail in the .WEBP or .JPG format.
    emoji: `str`
        Optional. Emoji associated with the sticker.
    set_name: `str`
        Optional. Name of the sticker set to which the sticker belongs.
    premium_animation: `File`
        Optional. For premium regular stickers, premium animation for the sticker.
    mask_position: `MaskPosition`
        Optional. For mask stickers, the position where the mask should be placed.
    custom_emoji_id: `str`
        Optional. For custom emoji stickers, unique identifier of the custom emoji.
    needs_repainting: `bool`
        Optional. True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places.
    file_size: `int`
        Optional. File size in bytes.
    """

    def __init__(self, data):
        self.file_id = data["file_id"]
        self.file_unique_id = data["file_unique_id"]
        self.type = data["type"]
        self.width = data["width"]
        self.height = data["height"]
        self.is_animated = data["is_animated"]
        self.is_video = data["is_video"]
        self.thumbnail = data.get("thumb")
        if self.thumbnail:
            self.thumbnail = PhotoSize(self.thumbnail)
        self.emoji = data.get("emoji")
        self.set_name = data.get("set_name")
        self.premium_animation = data.get("premium_animation")
        if self.premium_animation:
            self.premium_animation = File(self.premium_animation)
        self.mask_position = data.get("mask_position")
        if self.mask_position:
            self.mask_position = MaskPosition(self.mask_position)
        self.custom_emoji_id = data.get("custom_emoji_id")
        self.needs_repainting = data.get("needs_repainting")
        self.file_size = data.get("file_size")
