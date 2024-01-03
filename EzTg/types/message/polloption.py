class PollOption:
    """Represents one answer option in a poll.

    Attributes
    ----------
    text: `str`
        Option text, 1-100 characters.
    voter_count: `int`
        Number of users that voted for this option"""

    def __init__(self, data):
        self.text = data["text"]
        self.voter_count = data["voter_count"]
