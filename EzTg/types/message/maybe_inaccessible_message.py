from ..chat import Chat

class MaybeInaccessibleMessage:
    """This object describes a message that can be inaccessible to the bot. It can be one of
    
    - `Message`
    - `InaccessibleMessage`"""
            
    def __init__(self, data: dict):
        self.type = data["type"]
        if self.type == "message":
            from .message import Message # Lazy import to avoid circular imports until finding a better solution
            return Message(data)
        elif self.type == "inaccessible_message":
            return InaccessibleMessage(data)
        else:
            raise ValueError(f"Unknown message type: {self.type}")
    
class InaccessibleMessage:
    """This object describes a message that was deleted or is otherwise inaccessible to the bot.
    
    Attributes:
    -----------
    chat: `Chat`
        Chat the message belonged to.
    message_id: `int`
        Unique message identifier inside the chat.
    date: `int`
        Always 0. The field can be used to differentiate regular and inaccessible messages."""
    
    def __init__(self, data: dict):
        self.chat = Chat(data["chat"])
        self.message_id = data["message_id"]
        self.date = data["date"]