class Invoice:
    """
    This object contains basic information about an invoice.

    Attributes:
    -----------
    title: `str`
        Product name
    description: `str`
        Product description
    start_parameter: `str`
        Unique bot deep-linking parameter that can be used to generate this invoice
    currency: `str`
        Three-letter ISO 4217 currency code
    total_amount: `int`
        Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """
    
    def __init__(self, data):
        self.title = data["title"]
        self.description = data["description"]
        self.start_parameter = data["start_parameter"]
        self.currency = data["currency"]
        self.total_amount = data["total_amount"]