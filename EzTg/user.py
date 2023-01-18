class User:
    """Represents a Telegram user or bot.

    Attributes
    ----------
    id: `int`
        The unique identifier for this user or bot.
    is_bot: `bool`
        True, if this user is a bot.
    first_name: `str`
        User's or bot's first name.
    last_name: `str`
        User's or bot's last name.
    username: `str`
        User's or bot's username.
    language_code: `str`
        IETF language tag of the user's language.
    is_premium: `bool`
        True, if this user is a Telegram Premium user
    added_to_attachment_menu: `bool`
        True, if this user added the bot to the attachment menu
    can_join_groups: `bool`
        Optional. True, if the bot can be invited to groups. Returned only in getMe.
    can_read_all_group_messages: `bool`
        Optional. True, if privacy mode is disabled for the bot. Returned only in getMe.
    supports_inline_queries: `bool`
        Optional. True, if the bot supports inline queries. Returned only in getMe."""

    def __init__(
        self,
        id,
        is_bot,
        first_name,
        last_name,
        username,
        language_code,
        is_premium,
        added_to_attachment_menu,
        can_join_groups=None,
        can_read_all_group_messages=None,
        supports_inline_queries=None,
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries
