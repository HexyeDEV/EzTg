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
        if requests.get('https://api.telegram.org/bot'+token+"/getMe").json()['ok'] == False:
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
            self.update = update
            if update:
                for x in update:
                    callback(x)

                offset = update[-1].update_id + 1

    """sendMessage method"""
    def sendMessage(self, chat_id, text, parse_mode='Markdown', disable_web_page_preview=False,
                    disable_notification=False,
                    reply_to_message_id=None, reply_markup=None):
        if reply_markup:
            return self.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                         disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                         reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        else:
            return self.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                         disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                         reply_to_message_id=reply_to_message_id)

    """deleteMessage method"""
    def deleteMessage(self, chat_id, message_id):
        return self.send('deleteMessage', chat_id=chat_id, message_id=message_id)

    """editMessageText method"""
    def editMessageText(self, chat_id, message_id, text, inline_message_id=None, parse_mode='Markdown', entities=None,
                        disable_web_page_preview=False, reply_markup=None):
        if reply_markup:
            return self.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                         text=text, parse_mode=parse_mode, entities=entities,
                         disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup)
        else:
            return self.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                         text=text, parse_mode=parse_mode, entities=entities,
                         disable_web_page_preview=disable_web_page_preview)

    """forwardMessage method"""
    def forwardMessage(self, chat_id, from_chat_id, message_id, disable_notification=False):
        return self.send('forwardMessage', chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id, disable_notification=disable_notification)

    """getMe method"""
    def getMe(self):
        return self.send('getMe')

    """copyMessage method"""
    def copyMessage(self, chat_id, message_id, caption=None, disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=False, reply_markup=None):
        if reply_markup:
            return self.send('copyMessage', chat_id=chat_id, message_id=message_id, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup)
        else:
            return self.send('copyMessage', chat_id=chat_id, message_id=message_id, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply)


    """exportChatInviteLink method"""
    def exportChatInviteLink(self, chat_id):
        return self.send('exportChatInviteLink', chat_id=chat_id)

    """createChatInviteLink method"""
    def createChatInviteLink(self, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=False):
        return self.send('createChatInviteLink', chat_id=chat_id, name=name, expire_date=expire_date, member_limit=member_limit, creates_join_request=creates_join_request)

    """setChatPhoto method"""
    def setChatPhoto(self, chat_id, photo):
        return self.send('setChatPhoto', chat_id=chat_id, photo=photo)

    """pinChatMessage method"""
    def pinChatMessage(self, chat_id, message_id, disable_notification=False):
        return self.send('pinChatMessage', chat_id=chat_id, message_id=message_id, disable_notification=disable_notification)

    """unpinChatMessage method"""
    def unpinChatMessage(self, chat_id, message_id):
        return self.send('unpinChatMessage', chat_id=chat_id, message_id=message_id)

    """leaveChat method"""
    def leaveChat(self, chat_id):
        return self.send('leaveChat', chat_id=chat_id)

    """Get user id from message"""
    def get_author_id(self, message):
        return message['from']['id']

    """Get chat id from message"""
    def get_chat_id(self, message):
        return message['chat']['id']
