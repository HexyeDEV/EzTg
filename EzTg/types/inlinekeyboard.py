class InlineKeyboard:

    def __init__(self, data=None):
        """Create a new inline keyboard or Represents an inline keyboard that appears right next to the message it belongs to."""
        if data:
            self.keyboard = data
        self.keyboard = [[]]

    def url(self, text, url):
        """Add a new url button to the keyboard.

        Parameters
        ----------
        text : str
            The text of the button
        url : str
            The url of the button"""
        self.keyboard[-1].append({"text": text, "url": url})

    def url_new_row(self, text, url):
        """Add a new url button to the keyboard in a new row.

        Parameters
        ----------
        text : str
            The text of the button
        url : str
            The url of the button"""
        self.keyboard.append([])
        self.keyboard[-1].append({"text": text, "url": url})

    def callback(self, text, callback_data):
        """Add a new callback button to the keyboard.

        Parameters
        ----------
        text : str
            The text of the button
        callback_data : str
            The callback data of the button"""
        self.keyboard[-1].append({
            "text": text,
            "callback_data": callback_data
        })

    def callback_new_row(self, text, callback_data):
        """Add a new callback button to the keyboard in a new row.

        Parameters
        ----------
        text : str
            The text of the button
        callback_data : str
            The callback data of the button"""
        self.keyboard.append([])
        self.keyboard[-1].append({
            "text": text,
            "callback_data": callback_data
        })

    def send(self):
        """Return the keyboard."""
        return {"inline_keyboard": self.keyboard}
