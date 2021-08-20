"""sendMessage method"""
def sendMessage(self, chat_id, text, parse_mode='Markdown', disable_web_page_preview=False, disable_notification=False,
                reply_to_message_id=None, reply_markup=None):
    """bot.sendMessage(chat_id, message_id, text, parse_mode(Optional), reply_to_message_id(Optional))"""
    return self.send('sendMessage', chat_id=chat_id, text=text, parse_mode=parse_mode,
                     disable_web_page_preview=disable_web_page_preview, disable_notification=disable_notification,
                     reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)