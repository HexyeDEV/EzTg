class message:

    """sendMessage method"""
    def sendMessage(app, chat_id, text, parse_mode='Markdown', disable_web_page_preview=False,
                    disable_notification=False,
                    reply_to_message_id=None, reply_markup=None):
        if reply_markup:
            return app.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                            disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                            reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)
        else:
            return app.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                            disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                            reply_to_message_id=reply_to_message_id)

    """deleteMessage method"""
    def deleteMessage(app, chat_id, message_id):
        return app.send('deleteMessage', chat_id=chat_id, message_id=message_id)

    """editMessageText method"""
    def editMessageText(app, chat_id, message_id, text, inline_message_id=None, parse_mode='Markdown', entities=None,
                        disable_web_page_preview=False, reply_markup=None):
        if reply_markup:
            return app.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                            text=text, parse_mode=parse_mode, entities=entities,
                            disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup)
        else:
            return app.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                            text=text, parse_mode=parse_mode, entities=entities,
                            disable_web_page_preview=disable_web_page_preview)

    """forwardMessage method"""
    def forwardMessage(app, chat_id, from_chat_id, message_id, disable_notification=False):
        return app.send('forwardMessage', chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id, disable_notification=disable_notification)

    """copyMessage method"""
    def copyMessage(app, chat_id, message_id, caption=None, disable_notification=False, reply_to_message_id=None, allow_sending_without_reply=False, reply_markup=None):
        if reply_markup:
            return app.send('copyMessage', chat_id=chat_id, message_id=message_id, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup)
        else:
            return app.send('copyMessage', chat_id=chat_id, message_id=message_id, caption=caption, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply)
