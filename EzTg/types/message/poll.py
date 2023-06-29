from .messageentity import MessageEntity
from .polloption import PollOption


class Poll:
    """This object contains information about a poll.

    Attributes
    ----------
    id: `str`
        Unique poll identifier.
    question: `str`
        Poll question, 1-300 characters.
    options: `List[PollOption]`
        List of poll options.
    total_voter_count: `int`
        Total number of users that voted in the poll.
    is_closed: `bool`
        True, if the poll is closed.
    is_anonymous: `bool`
        True, if the poll is anonymous.
    type: `str`
        Poll type, currently can be “regular” or “quiz”.
    allows_multiple_answers: `bool`
        True, if the poll allows multiple answers.
    correct_option_id: `int`
        Optional. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    explanation: `str`
        Optional. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters.
    explanation_entities: `List[MessageEntity]`
        Optional. Special entities like usernames, URLs, bot commands, etc. that appear in the explanation.
    open_period: `int`
        Optional. Amount of time in seconds the poll will be active after creation.
    close_date: `int`
        Optional. Point in time (Unix timestamp) when the poll will be automatically closed.
    """

    def __init__(self, data):
        self.id = data["id"]
        self.question = data["question"]
        self.options = [PollOption(option) for option in data["options"]]
        self.total_voter_count = data["total_voter_count"]
        self.is_closed = data["is_closed"]
        self.is_anonymous = data["is_anonymous"]
        self.type = data["type"]
        self.allows_multiple_answers = data["allows_multiple_answers"]
        self.correct_option_id = data.get("correct_option_id")
        self.explanation = data.get("explanation")
        self.explanation_entities = [
            MessageEntity(entity)
            for entity in data.get("explanation_entities", [])
        ]
        self.open_period = data.get("open_period")
        self.close_date = data.get("close_date")
