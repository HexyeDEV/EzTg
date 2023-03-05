class ReplyKeyboardMarkup:

    def __init__(
        self,
        is_persistent=False,
        resize_keyboard=False,
        one_time_keyboard=False,
        selective=False,
        input_field_placeholder=None,
    ):
        self.keyboard = [[]]
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

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
        return {
            "reply_markup": self.keyboard,
            "is_persistent": self.is_persistent,
            "resize_keyboard": self.resize_keyboard,
            "one_time_keyboard": self.one_time_keyboard,
            "selective": self.selective,
        }