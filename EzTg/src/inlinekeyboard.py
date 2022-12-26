class InlineKeyboard:
    def __init__(self):
        """Create a new inline keyboard"""
        self.keyboard = [[]]
    
    def url(self, text, url):
        """Add a new url button to the keyboard
        :param text: The text of the button
        :param url: The url of the button"""
        self.keyboard[-1].append({"text": text, "url": url})
    
    def url_new_row(self, text, url):
        """Add a new url button to the keyboard in a new row
        :param text: The text of the button
        :param url: The url of the button"""
        self.keyboard.append([])
        self.keyboard[-1].append({"text": text, "url": url})
    
    def send(self):
        """Return the keyboard"""
        return self.keyboard