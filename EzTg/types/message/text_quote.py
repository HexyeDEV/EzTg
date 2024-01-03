class TextQuote:
    """This object contains information about the quoted part of a message that is replied to by the given message.
    
    Attributes:
    -----------
    text: `str`
        Text of the quoted part of a message that is replied to by the given message.
    entities: `array of MessageEntity`
        Optional. Special entities that appear in the quote. Currently, only bold, italic, underline, strikethrough, spoiler, and custom_emoji entities are kept in quotes.
    position: `Integer`
        Approximate quote position in the original message in UTF-16 code units as specified by the sender
    is_manual: `bool`
        Optional. True, if the quote was chosen manually by the message sender. Otherwise, the quote was added automatically by the server."""
    
    def __init__(self, data: dict):
        self.text = data["text"]
        self.entities = data.get("entities")
        self.position = data["position"]
        self.is_manual = data.get("is_manual")