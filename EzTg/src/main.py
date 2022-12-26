import requests
import aiohttp


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

    """Send method to api website"""
    async def send(self, method, **kwargs):
        async with aiohttp.request("POST", self.api.format(self.token, method), json=kwargs) as response:
            r = await response.json()
            return Parse(r)

    """Run main"""
    async def start_polling(self, callback, callback_query=None):
        offset = None
        while 1:
            update = await self.send("getUpdates", offset=offset)
            self.update = update
            if update:
                for x in update:
                    if "message" in x.keys():
                        await callback(x)
                        offset = update[-1].update_id + 1
                    elif "callback_query" in x.keys() and callback_query:
                        await callback_query(x)
                        offset = update[-1].update_id + 1

    """sendMessage method"""
    async def sendMessage(self, chat_id, text, parse_mode='Markdown', disable_web_page_preview=False,
                          disable_notification=False,
                          reply_to_message_id=None, reply_markup=None):
        if reply_markup:
            return await self.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                                   disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                                   reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        else:
            return await self.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                                   disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                                   reply_to_message_id=reply_to_message_id)

    """deleteMessage method"""
    async def deleteMessage(self, chat_id, message_id):
        return await self.send('deleteMessage', chat_id=chat_id, message_id=message_id)

    """editMessageText method"""
    async def editMessageText(self, chat_id, message_id, text, inline_message_id=None, parse_mode='Markdown', entities=None,
                              disable_web_page_preview=False, reply_markup=None):
        if reply_markup:
            return await self.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                                   text=text, parse_mode=parse_mode, entities=entities,
                                   disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup)
        else:
            return await self.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                                   text=text, parse_mode=parse_mode, entities=entities,
                                   disable_web_page_preview=disable_web_page_preview)

    """forwardMessage method"""
    async def forwardMessage(self, chat_id, from_chat_id, message_id, disable_notification=False):
        return await self.send('forwardMessage', chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id, disable_notification=disable_notification)

    """getMe method"""
    async def getMe(self):
        return await self.send('getMe')

    """copyMessage method"""
    async def copyMessage(self, chat_id, message_id, caption=None, disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=False, reply_markup=None):
        if reply_markup:
            return await self.send('copyMessage', chat_id=chat_id, message_id=message_id, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup)
        else:
            return await self.send('copyMessage', chat_id=chat_id, message_id=message_id, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply)

    """exportChatInviteLink method"""
    async def exportChatInviteLink(self, chat_id):
        return await self.send('exportChatInviteLink', chat_id=chat_id)

    """createChatInviteLink method"""
    async def createChatInviteLink(self, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=False):
        return await self.send('createChatInviteLink', chat_id=chat_id, name=name, expire_date=expire_date, member_limit=member_limit, creates_join_request=creates_join_request)

    """setChatPhoto method"""
    async def setChatPhoto(self, chat_id, photo):
        return await self.send('setChatPhoto', chat_id=chat_id, photo=photo)

    """pinChatMessage method"""
    async def pinChatMessage(self, chat_id, message_id, disable_notification=False):
        return await self.send('pinChatMessage', chat_id=chat_id, message_id=message_id, disable_notification=disable_notification)

    """unpinChatMessage method"""
    async def unpinChatMessage(self, chat_id, message_id):
        return await self.send('unpinChatMessage', chat_id=chat_id, message_id=message_id)

    """leaveChat method"""
    async def leaveChat(self, chat_id):
        return await self.send('leaveChat', chat_id=chat_id)

    """Get user id from message"""
    async def get_author_id(self, message):
        return message['from']['id']

    """Get chat id from message"""
    async def get_chat_id(self, message):
        return message['chat']['id']
