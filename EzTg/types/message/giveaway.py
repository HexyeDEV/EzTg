from ..chat import Chat

class Giveaway:
    """This object represents a message about a scheduled giveaway.
    
    Attributes
    ----------
    chats: `array of Chat`
        The list of chats which the user must join to participate in the giveaway.
    winners_selection_date: `int`
        Point in time (Unix timestamp) when winners of the giveaway will be selected.
    winner_count: `int`
        The number of users which are supposed to be selected as winners of the giveaway.
    only_new_members: `bool`
        Optional. True, if only users who join the chats after the giveaway started should be eligible to win.
    has_public_winners: `bool`
        Optional. True, if the list of giveaway winners will be visible to everyone.
    prize_description: `str`
        Optional. Description of additional giveaway prize.
    country_codes: `array of str`
        Optional. A list of two-letter ISO 3166-1 alpha-2 country codes indicating the countries from which eligible users for the giveaway must come. If empty, then all users can participate in the giveaway. Users with a phone number that was bought on Fragment can always participate in giveaways.
    premium_subscription_month_count: `int`
        Optional. The number of months the Telegram Premium subscription won from the giveaway will be active for.
    """

    def __init__(self, data):
        self.chats = [Chat(chat) for chat in data["chats"]]
        self.winners_selection_date = data["winners_selection_date"]
        self.winner_count = data["winner_count"]
        self.only_new_members = data.get("only_new_members")
        self.has_public_winners = data.get("has_public_winners")
        self.prize_description = data.get("prize_description")
        self.country_codes = data.get("country_codes")
        self.premium_subscription_month_count = data.get("premium_subscription_month_count")