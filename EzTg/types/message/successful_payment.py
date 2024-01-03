from .order_info import OrderInfo

class SuccessfulPayment:
    """This object contains basic information about a successful payment.
    
    Attributes
    ----------
    currency: `str`
        Three-letter ISO 4217 currency code.
    total_amount: `int`
        Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    invoice_payload: `str`
        Bot specified invoice payload.
    shipping_option_id: `str`
        Optional. Identifier of the shipping option chosen by the user.
    order_info: `OrderInfo`
        Optional. Order info provided by the user.
    telegram_payment_charge_id: `str`
        Telegram payment identifier.
    provider_payment_charge_id: `str`
        Provider payment identifier.
    """

    def __init__(self, data):
        self.currency = data["currency"]
        self.total_amount = data["total_amount"]
        self.invoice_payload = data["invoice_payload"]
        self.shipping_option_id = data.get("shipping_option_id")
        self.order_info = data.get("order_info")
        if self.order_info:
            self.order_info = OrderInfo(self.order_info)
        self.telegram_payment_charge_id = data["telegram_payment_charge_id"]
        self.provider_payment_charge_id = data["provider_payment_charge_id"]