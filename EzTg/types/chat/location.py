from ..location import Location


class ChatLocation:
    """Represents a location to which a chat is connected.

    Attributes
    ----------
    location: `Location`
        The location to which the supergroup is connected. Can't be a live location.
    address: `str`
        Location address; 1-64 characters, as defined by the chat owner
    """

    def __init__(self, data):
        self.location = Location(data["location"])
        self.address = data["address"]
