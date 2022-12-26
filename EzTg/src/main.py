import aiohttp
import requests


class Parse(dict):

    def __getattr__(*args):
        args = dict.get(*args)

        return (Parse(args) if isinstance(args, dict) else
                [[Parse(y) for y in x] if isinstance(x, list) else Parse(x)
                 for x in args] if isinstance(args, list) else args)

    __setattr__ = dict.__setitem__

    __delattr__ = dict.__delitem__


class TokenError(Exception):
    pass


class EzTg:
    """Giving token"""

    def __init__(self, token):
        if (requests.get("https://api.telegram.org/bot" + token +
                         "/getMe").json()["ok"] == False):
            raise TokenError("The token you provided is wrong")
        else:
            self.token = token
            self.api = "https://api.telegram.org/bot{}/{}"

    async def send(self, method, **kwargs):
        """Send a request to the telegram api
        :param method: The method to be called
        :param kwargs: The parameters to be passed to the method"""
        async with aiohttp.request("POST",
                                   self.api.format(self.token, method),
                                   json=kwargs) as response:
            r = await response.json()
            return Parse(r)

    async def start_polling(self, callback, callback_query=None):
        """Run the bot and wait for updates
        :param callback: A callback function that will be called when a new message update is received
        :param callback_query: A callback function that will be called when a new callback_query update is received"""
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


    async def sendMessage(
        self,
        chat_id,
        text,
        parse_mode="Markdown",
        disable_web_page_preview=False,
        disable_notification=False,
        reply_to_message_id=None,
        reply_markup=None,
    ):
        """sendMessage method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param text: Text of the message to be sent
        :param parse_mode: Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :param disable_web_page_preview: Disables link previews for links in this message
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param reply_markup: Additional interface options. Use the InlineKeyboard class to create a new inline keyboard"""
        if reply_markup:
            return await self.send(
                "sendMessage",
                chat_id=chat_id,
                text=text,
                parse_mode=parse_mode,
                disable_web_page_preview=disable_web_page_preview,
                disable_notification=disable_notification,
                reply_to_message_id=reply_to_message_id,
                reply_markup=reply_markup,
            )
        else:
            return await self.send(
                "sendMessage",
                chat_id=chat_id,
                text=text,
                parse_mode=parse_mode,
                disable_web_page_preview=disable_web_page_preview,
                disable_notification=disable_notification,
                reply_to_message_id=reply_to_message_id,
            )


    async def deleteMessage(self, chat_id, message_id):
        """deleteMessage method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param message_id: Identifier of the message to delete"""
        return await self.send("deleteMessage",
                               chat_id=chat_id,
                               message_id=message_id)


    async def editMessageText(
        self,
        chat_id,
        message_id,
        text,
        inline_message_id=None,
        parse_mode="Markdown",
        entities=None,
        disable_web_page_preview=False,
        reply_markup=None,
    ):
        """editMessageText method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param message_id: Identifier of the message to edit
        :param inline_message_id: Identifier of the inline message
        :param text: New text of the message
        :param parse_mode: Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.
        :param entities: List of special entities that appear in message text, which can be specified instead of parse_mode
        :param disable_web_page_preview: Disables link previews for links in this message
        :param reply_markup: Additional interface options. Use the InlineKeyboard class to create a new inline keyboard"""
        if reply_markup:
            return await self.send(
                "editMessageText",
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                text=text,
                parse_mode=parse_mode,
                entities=entities,
                disable_web_page_preview=disable_web_page_preview,
                reply_markup=reply_markup,
            )
        else:
            return await self.send(
                "editMessageText",
                chat_id=chat_id,
                message_id=message_id,
                inline_message_id=inline_message_id,
                text=text,
                parse_mode=parse_mode,
                entities=entities,
                disable_web_page_preview=disable_web_page_preview,
            )


    async def forwardMessage(self,
                             chat_id,
                             from_chat_id,
                             message_id,
                             disable_notification=False):
        """forwardMessage method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param from_chat_id: Unique identifier for the chat where the original message was sent
        :param message_id: Message identifier in the chat specified in from_chat_id
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound."""
        return await self.send(
            "forwardMessage",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
        )


    async def getMe(self):
        """getMe method"""
        return await self.send("getMe")


    async def copyMessage(
        self,
        chat_id,
        message_id,
        caption=None,
        disable_notification=False,
        reply_to_message_id=None,
        allow_sending_without_reply=False,
        reply_markup=None,
    ):
        """copyMessage method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param message_id: Identifier of the message to copy
        :param caption: New caption of the message
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True, if the message should be sent even if the specified replied-to message is not found
        :param reply_markup: Additional interface options. Use the InlineKeyboard class to create a new inline keyboard"""
        if reply_markup:
            return await self.send(
                "copyMessage",
                chat_id=chat_id,
                message_id=message_id,
                caption=caption,
                disable_notification=disable_notification,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
                reply_markup=reply_markup,
            )
        else:
            return await self.send(
                "copyMessage",
                chat_id=chat_id,
                message_id=message_id,
                caption=caption,
                disable_notification=disable_notification,
                reply_to_message_id=reply_to_message_id,
                allow_sending_without_reply=allow_sending_without_reply,
            )


    async def exportChatInviteLink(self, chat_id):
        """exportChatInviteLink method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)"""
        return await self.send("exportChatInviteLink", chat_id=chat_id)


    async def createChatInviteLink(
        self,
        chat_id,
        name=None,
        expire_date=None,
        member_limit=None,
        creates_join_request=False,
    ):
        """createChatInviteLink method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param name: Point in time (Unix timestamp) when the link will expire
        :param expire_date: Point in time (Unix timestamp) when the link will expire
        :param member_limit: Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
        :param creates_join_request: Pass True to create a new chat members invite link that can be used only by users invited by another chat administrator; requires appropriate administrator rights in the chat"""
        return await self.send(
            "createChatInviteLink",
            chat_id=chat_id,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request,
        )

    async def setChatPhoto(self, chat_id, photo):
        """setChatPhoto method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param photo: New chat photo, uploaded using multipart/form-data"""
        return await self.send("setChatPhoto", chat_id=chat_id, photo=photo)


    async def pinChatMessage(self,
                             chat_id,
                             message_id,
                             disable_notification=False):
        """pinChatMessage method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param message_id: Identifier of a message to pin
        :param disable_notification: Pass True, if it is not necessary to send a notification to all chat members about the new pinned message. Notifications are always disabled in channels."""
        return await self.send(
            "pinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
        )

    async def unpinChatMessage(self, chat_id, message_id):
        """unpinChatMessage method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername)
        :param message_id: Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned."""
        return await self.send("unpinChatMessage",
                               chat_id=chat_id,
                               message_id=message_id)


    async def leaveChat(self, chat_id):
        """leaveChat method
        :param chat_id: Unique identifier for the target chat or username of the target supergroup or channel (in the format @channelusername"""
        return await self.send("leaveChat", chat_id=chat_id)


    async def get_author_id(self, message):
        """Get author id from message
        :param message: Message object"""
        return message["from"]["id"]


    async def get_chat_id(self, message):
        """Get chat id from message
        :param message: Message object"""
        return message["chat"]["id"]
