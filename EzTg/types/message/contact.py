class Contact:
    """This object represents a phone contact.
    
    Attributes
    ----------
    phone_number: `str`
        Contact's phone number.
    first_name: `str`
        Contact's first name.
    last_name: `str`
        Optional. Contact's last name.
    user_id: `int`
        Optional. Contact's user identifier in Telegram.
    vcard: `str`
        Optional. Additional data about the contact in the form of a vCard."""
    
    def __init__(self, data):
        self.phone_number = data["phone_number"]
        self.first_name = data["first_name"]
        self.last_name = data.get("last_name")
        self.user_id = data.get("user_id")
        self.vcard = data.get("vcard")