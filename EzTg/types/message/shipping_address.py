class ShippingAddress:
    """This object represents a shipping address.
    
    Attributes
    ----------
    country_code: `str`
        ISO 3166-1 alpha-2 country code.
    state: `str`
        State, if applicable.
    city: `str`
        City.
    street_line1: `str`
        First line for the address.
    street_line2: `str`
        Second line for the address.
    post_code: `str`
        Address post code.
    """

    def __init__(self, data):
        self.country_code = data["country_code"]
        self.state = data["state"]
        self.city = data["city"]
        self.street_line1 = data["street_line1"]
        self.street_line2 = data["street_line2"]
        self.post_code = data["post_code"]