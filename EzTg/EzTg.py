import aiohttp

from .types.chat.chat import Chat
from .types.user.user import User


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


class TelegramClient:
    """A class that represents a telegram client."""

    def __init__(self, token):
        """Initialize the client.

        Parameters
        ----------
        token: `str`
            The token of your bot."""

        self.token = token
        self.api = "https://api.telegram.org/bot{}/{}"

    async def send(self, method, **kwargs):
        """Send a request to the telegram api.

        Parameters
        ----------
        method: `str`
            The method you want to use.
        \*\*kwargs: `dict`
            The parameters you want to send to the method."""
        async with aiohttp.request(
            "POST", self.api.format(self.token, method), json=kwargs
        ) as response:
            r = await response.json()
            return Parse(r)

    async def start_polling(self, callback, callback_query=None):
        """Start polling for updates.

        Parameters
        ----------
        callback: `function`
            The function you want to call when a message is received.
        callback_query: `function`
            The function you want to call when a callback query is received."""
        if self.send("getMe").ok == False:
            raise TokenError("The token you provided is wrong")
        offset = None
        while 1:
            update = await self.send("getUpdates", offset=offset)
            update = update.result
            self.update = update
            if update:
                for x in update:
                    if "message" in x.keys():
                        await callback(x)
                        offset = update[-1].update_id + 1
                    elif "callback_query" in x.keys() and callback_query:
                        await callback_query(x)
                        offset = update[-1].update_id + 1

    async def send_message(
        self,
        chat_id,
        text,
        parse_mode="Markdown",
        disable_web_page_preview=False,
        disable_notification=False,
        reply_to_message_id=None,
        reply_markup=None,
    ):
        """Send a message to a chat.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to send the message to.
        text: `str`
            The text you want to send.
        parse_mode: `str`
            The parse mode you want to use.
        disable_web_page_preview: `bool`
            Disable link previews for links in this message.
        disable_notification: `bool`
            Sends the message silently. Users will receive a notification with no sound.
        reply_to_message_id: `int`
            If the message is a reply, ID of the original message.
        reply_markup: `dict`
            Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        """
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

    async def delete_message(self, chat_id, message_id):
        """Delete a message.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to delete the message from.
        message_id: `int`
            The message id you want to delete."""
        return await self.send("deleteMessage", chat_id=chat_id, message_id=message_id)

    async def edit_message_text(
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
        """Edit a message.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to edit the message from.
        message_id: `int`
            The message id you want to edit.
        text: `str`
            The text you want to send.
        inline_message_id: `int`
            The inline message id you want to edit.
        parse_mode: `str`
            The parse mode you want to use.
        entities: `list`
            List of special entities that appear in message text, which can be specified instead of parse_mode.
        disable_web_page_preview: `bool`
            Disable link previews for links in this message.
        reply_markup: `InlineKeyboard.send`
            Additional interface options. Use the InlineKeyboard class to create a keyboard and use the send method to send it.
        """
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

    async def forward_message(
        self, chat_id, from_chat_id, message_id, disable_notification=False
    ):
        """Foward a message.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to forward the message to.
        from_chat_id: `int`
            The chat id you want to forward the message from.
        message_id: `int`
            The message id you want to forward.
        disable_notification: `bool`
            Sends the message silently. Users will receive a notification with no sound.
        """
        return await self.send(
            "forwardMessage",
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
        )

    async def get_me(self):
        """Get information about the bot."""
        r = await self.send("getMe")
        user = User(
            r["id"],
            r["is_bot"],
            r["first_name"],
            r["last_name"],
            r["username"],
            r["language_code"],
            r["is_premium"],
            r["added_to_attachment_menu"],
            r["can_join_groups"],
            r["can_read_all_group_messages"],
            r["supports_inline_queries"],
        )
        return user

    async def copy_message(
        self,
        chat_id,
        message_id,
        caption=None,
        disable_notification=False,
        reply_to_message_id=None,
        allow_sending_without_reply=False,
        reply_markup=None,
    ):
        """Copy a message.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to forward the message to.
        message_id: `int`
            The message id you want to forward.
        caption: `str`
            The caption you want to send.
        disable_notification: `bool`
            Sends the message silently. Users will receive a notification with no sound.
        reply_to_message_id: `int`
            If the message is a reply, ID of the original message.
        allow_sending_without_reply: `bool`
            Pass True, if the message should be sent even if the specified replied-to message is not found.
        reply_markup: `InlineKeyboard.send`
            Additional interface options. Use the InlineKeyboard class to create a keyboard and use the send method to send it.
        """
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

    async def export_chat_invite_link(self, chat_id):
        """Export a chat invite link.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to make the invite link."""
        return await self.send("exportChatInviteLink", chat_id=chat_id)

    async def create_chat_invite_link(
        self,
        chat_id,
        name=None,
        expire_date=None,
        member_limit=None,
        creates_join_request=False,
    ):
        """Create a chat invite link.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to make the invite link.
        name: `str`
            The name of the invite link.
        expire_date: `int`
            The expire date of the invite link.
        member_limit: `int`
            The member limit of the invite link.
        creates_join_request: `bool`
            Pass True, if the link should be created without a chat member limit."""
        return await self.send(
            "createChatInviteLink",
            chat_id=chat_id,
            name=name,
            expire_date=expire_date,
            member_limit=member_limit,
            creates_join_request=creates_join_request,
        )

    async def set_chat_photo(self, chat_id, photo):
        """Set the chat photo.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to set the photo.
        photo: `str`
            The photo you want to use."""
        return await self.send("setChatPhoto", chat_id=chat_id, photo=photo)

    async def pin_chat_message(self, chat_id, message_id, disable_notification=False):
        """Pin a message.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to pin the message.
        message_id: `int`
            The message id you want to pin.
        disable_notification: `bool`
            Sends the message silently. Users will receive a notification with no sound.
        """
        return await self.send(
            "pinChatMessage",
            chat_id=chat_id,
            message_id=message_id,
            disable_notification=disable_notification,
        )

    async def unpin_chat_message(self, chat_id, message_id):
        """Unpin a message.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to unpin the message.
        message_id: `int`
            The message id you want to unpin."""
        return await self.send(
            "unpinChatMessage", chat_id=chat_id, message_id=message_id
        )

    async def leave_chat(self, chat_id):
        """Leave a chat.

        Parameters
        ----------
        chat_id: `int`
            The chat id you want to leave."""
        return await self.send("leaveChat", chat_id=chat_id)

    async def get_author_id(self, message):
        """Get author id from message.

        Parameters
        ----------
        message: `dict`
            The message object."""
        return message["from"]["id"]

    async def get_chat_id(self, message):
        """Get chat id from message.

        Parameters
        ----------
        message: `dict`
            The message object.s"""
        return message["chat"]["id"]

    async def get_sender_object(self, message) -> User:
        """Get sender object from message.

        Parameters
        ----------
        message: `dict`
            The message object."""

        sender = message["from"]
        user = User(sender)
        return user

    async def get_user_object(self, user) -> User:
        """Get user object from user dict.

        Parameters
        ----------
        user: `dict`
            The user dict."""
        user = User(user)
        return user

    async def get_entity_object(self, entity) -> Chat:
        """Get entity object from entity dict.

        Parameters
        ----------
        entity: `dict`
            The entity dict."""
        return Chat(entity)

    async def get_entity(self, entity_id) -> Chat:
        """Get entity from id.

        Parameters
        ----------
        entity_id: `int` or `str`
            The entity id or username of the target supergroup or channel (in the format @channelusername)
        """
        raw = await self.send("getChat", chat_id=entity_id)
        return await self.get_entity_object(raw)
