class ReplyKeyboardMarkup:

    def __init__(
        self,
        is_persistent=False,
        resize_keyboard=False,
        one_time_keyboard=False,
        selective=False,
        input_field_placeholder=None,
    ):
        """Create a new reply keyboard markup

        Parameters
        ----------
        is_persistent : bool
            Optional. The keyboard is persistent, by default False
        resize_keyboard : bool
            Optional. The keyboard is resized, by default False
        one_time_keyboard : bool
            Optional. The keyboard is one time, by default False
        selective : bool
            Optional. The keyboard is selective, by default False
        input_field_placeholder : str
            Optional. The placeholder of the input field, by default None"""
        self.keyboard = [[]]
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective
        self.input_field_placeholder = input_field_placeholder

    def add(
        self,
        text,
        request_user=None,
        request_chat=None,
        request_contact=False,
        request_location=False,
        request_poll=False,
        web_app=None,
    ):
        """Add a new button to the keyboard.

        Parameters
        ----------
        text : str
            The text of the button
        request_user : str
            Optional. The request user of the button, by default None
        request_chat : str
            Optional. The request chat of the button, by default None
        request_contact : bool
            Optional. The request contact of the button, by default False
        request_location : bool
            Optional. The request location of the button, by default False
        request_poll : bool
            Optional. The request poll of the button, by default False
        web_app : str
            Optional. The web app of the button, by default None"""
        self.keyboard[-1].append({
            "text": text,
            "request_user": request_user,
            "request_chat": request_chat,
            "request_contact": request_contact,
            "request_location": request_location,
            "request_poll": request_poll,
            "web_app": web_app,
        })

    def add_new_row(
        self,
        text,
        request_user=None,
        request_chat=None,
        request_contact=False,
        request_location=False,
        request_poll=False,
        web_app=None,
    ):
        """Add a new button to the keyboard in a new row.

        Parameters
        ----------
        text : str
            The text of the button
        request_user : str
            Optional. The request user of the button, by default None
        request_chat : str
            Optional. The request chat of the button, by default None
        request_contact : bool
            Optional. The request contact of the button, by default False
        request_location : bool
            Optional. The request location of the button, by default False
        request_poll : bool
            Optional. The request poll of the button, by default False
        web_app : str
            Optional. The web app of the button, by default None"""
        self.keyboard.append([])
        self.keyboard[-1].append({
            "text": text,
            "request_user": request_user,
            "request_chat": request_chat,
            "request_contact": request_contact,
            "request_location": request_location,
            "request_poll": request_poll,
            "web_app": web_app,
        })

    def send(self):
        """Return the keyboard."""
        return {
            "reply_markup": self.keyboard,
            "is_persistent": self.is_persistent,
            "resize_keyboard": self.resize_keyboard,
            "one_time_keyboard": self.one_time_keyboard,
            "selective": self.selective,
            "input_field_placeholder": self.input_field_placeholder,
        }
