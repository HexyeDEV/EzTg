from .animation import Animation
from .messageentity import MessageEntity
from .photosize import PhotoSize


class Game:
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    Attributes
    ----------
    title: `str`
        Title of the game.
    description: `str`
        Description of the game.
    photo: `List[PhotoSize]`
        Photo that will be displayed in the game message in chats.
    text: `str`
        Optional. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls setGameScore, or manually edited using editMessageText. 0-4096 characters.
    text_entities: `List[MessageEntity]`
        Optional. Special entities that appear in text, such as usernames, URLs, bot commands, etc.
    animation: `Animation`
        Optional. Animation that will be displayed in the game message in chats. Upload via BotFather.
    """

    def __init__(self, data):
        self.title = data["title"]
        self.description = data["description"]
        self.photo = [PhotoSize(photo) for photo in data["photo"]]
        self.text = data.get("text")
        self.text_entities = [
            MessageEntity(entity) for entity in data.get("text_entities", [])
        ]
        self.animation = Animation(data.get("animation"))
