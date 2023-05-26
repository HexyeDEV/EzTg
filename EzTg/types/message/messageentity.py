from ..user import User


class MessageEntity:
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    Attributes
    ----------
    type: `str`
        Type of the entity. Can be mention (@username), hashtag, cashtag, bot_command, url, email, phone_number, bold (bold text), italic (italic text), underline (underlined text), strikethrough (strikethrough text), code (monowidth string), pre (monowidth block), text_link (for clickable text URLs), text_mention (for users without usernames).
    offset: `int`
        Offset in UTF-16 code units to the start of the entity.
    url: `str`
        Optional. For “text_link” only, URL that will be opened after user taps on the text.
    user: `User`
        Optional. For “text_mention” only, the mentioned user.
    language: `str`
        Optional. For “pre” only, the programming language of the entity text.
    custom_emoji_id: `str`
        Optional. For “custom_emoji” only, unique identifier of the custom emoji.
    """

    def __init__(self, data):
        self.type = data['type']
        self.offset = data['offset']
        self.url = data.get('url')
        self.user = data.get('user')
        if self.user:
            self.user = User(self.user)
        self.language = data.get('language')
        self.custom_emoji_id = data.get('custom_emoji_id')
