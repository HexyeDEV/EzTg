from .shipping_address import ShippingAddress

class OrderInfo:
    """This object represents information about an order.
    
    Attributes
    ----------
    name: `str`
        Optional. User name.
    phone_number: `str`
        Optional. User's phone number.
    email: `str`
        Optional. User email.
    shipping_address: `ShippingAddress`
        Optional. User shipping address.
    """

    def __init__(self, data):
        self.name = data.get("name")
        self.phone_number = data.get("phone_number")
        self.email = data.get("email")
        self.shipping_address = data.get("shipping_address")
        if self.shipping_address:
            self.shipping_address = ShippingAddress(self.shipping_address)