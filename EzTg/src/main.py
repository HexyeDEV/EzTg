import requests


class Parse(dict):
    def __getattr__(*args):
        args = dict.get(*args)

        return (
            Parse(args)
            if isinstance(args, dict)
            else [
                [Parse(y) for y in x] if isinstance(x, list) else Parse(x) for x in args
            ]
            if isinstance(args, list)
            else args
        )

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__

class TokenError(Exception):
    pass


class EzTg:

    """Giving token"""
    def __init__(self, token):
        if requests.get('https://api.telegram.org/bot'+token).json()['ok'] == False:
            raise TokenError('The token you provided is wrong')
        else:
            self.token = token
            self.api = "https://api.telegram.org/bot{}/{}"
            self.session = requests.Session()

    """Send method to api website"""
    def send(self, method, **kwargs):
        return Parse(
           self.session.post(
               url=self.api.format(self.token, method),
               json=kwargs,
           ).json()
       )

    """Run main"""
    def start_polling(self, callback):
        offset = None
        while 1:
            update = self.send("getUpdates", offset=offset).result
            if update:
                for x in update:
                    callback(self, x)

                offset = update[-1].update_id + 1

    """sendMessage method"""
    def sendMessage(self, chat_id, text, parse_mode='Markdown', disable_web_page_preview=False,
                    disable_notification=False,
                    reply_to_message_id=None, reply_markup=None):
        """bot.sendMessage(chat_id, message_id, text, parse_mode(Optional), reply_to_message_id(Optional))"""
        return self.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                         disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                         reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

    """deleteMessage method"""
    def deleteMessage(self, chat_id, message_id):
        """bot.deleteMessage(chat_id, message_id)"""
        return self.send('deleteMessage', chat_id=chat_id, message_id=message_id)

    """editMessageText method"""
    def editMessageText(self, chat_id, message_id, text, inline_message_id=None, parse_mode='Markdown', entities=None,
                        disable_web_page_preview=False, reply_markup=None):
        """bot.edit(chat_id, message_id, text)"""
        return self.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                         text=text, parse_mode=parse_mode, entities=entities,
                         disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup)

    """User info Methods"""

    """Get user id from message"""
    def get_author_id(self, message):
        return message['from']['id']

    """Chat info Methods"""

    """Get chat id from message"""
    def get_chat_id(self, message):
        return message['chat']['id']
