class MessageAutoDeleteTimerChanged:
    """Represents a service message about a change in auto-delete timer settings.

    Attributes
    ----------
    message_auto_delete_time: `int`
        New auto-delete time for messages in the chat; in seconds
    """

    def __init__(self, data):
        self.message_auto_delete_time = data["message_auto_delete_time"]