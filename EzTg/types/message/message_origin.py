from ..chat import Chat
from ..user import User

class MessageOrigin:
    """This object describes the origin of a message. It can be one of
    
    - `MessageOriginUser`
    - `MessageOriginHiddenUser`
    - `MessageOriginChat`
    - `MessageOriginChannel`"""
        
    def __init__(self, data: dict):
        self.type = data["type"]
        if self.type == "user":
            return MessageOriginUser(data)
        elif self.type == "hidden_user":
            return MessageOriginHiddenUser(data)
        elif self.type == "chat":
            return MessageOriginChat(data)
        elif self.type == "channel":
            return MessageOriginChannel(data)
        else:
            raise ValueError(f"Unknown message origin type: {self.type}")
    
class MessageOriginUser:
    """The message was originally sent by a known user.
    
    Attributes:
    -----------
    type: `str`
        Type of the message origin, always user
    date: `int`
        Date the message was sent originally in Unix time.
    sender_user: `User`
        User that sent the message originally."""
        
    def __init__(self, data: dict):
        self.type = data["type"]
        self.date = data["date"]
        self.sender_user = User(data["sender_user"])

class MessageOriginHiddenUser:
    """The message was originally sent by an anonymous user.
    
    Attributes:
    -----------
    type: `str`
        Type of the message origin, always hidden_user
    date: `int`
        Date the message was sent originally in Unix time.
    sender_user_name: `str`
        Name of the user that sent the message originally."""
        
    def __init__(self, data: dict):
        self.type = data["type"]
        self.date = data["date"]
        self.sender_user_name = data["sender_user_name"]

class MessageOriginChat:
    """The message was originally sent in a chat.
    
    Attributes:
    -----------
    type: `str`
        Type of the message origin, always chat
    date: `int`
        Date the message was sent originally in Unix time.
    sender_chat: `Chat`
        Chat that sent the message originally.
    author_signature: `str`
        Optional. For messages originally sent by an anonymous chat administrator, original message author signature."""
        
    def __init__(self, data: dict):
        self.type = data["type"]
        self.date = data["date"]
        self.sender_chat = Chat(data["sender_chat"])
        self.author_signature = data.get("author_signature")

class MessageOriginChannel:
    """The message was originally sent in a channel.
    
    Attributes:
    -----------
    type: `str`
        Type of the message origin, always channel
    date: `int`
        Date the message was sent originally in Unix time.
    chat: `Chat`
        Channel chat to which the message was originally sent.
    message_id: `int`
        Unique message identifier inside the chat.
    author_signature: `str`
        Optional. Signature of the original post author."""
            
    def __init__(self, data: dict):
        self.type = data["type"]
        self.date = data["date"]
        self.chat = Chat(data["chat"])
        self.message_id = data["message_id"]
        self.author_signature = data.get("author_signature")