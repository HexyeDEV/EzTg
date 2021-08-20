"""editMessageText method"""
def editMessageText(self, chat_id, message_id, text, inline_message_id=None, parse_mode='Markdown', entities=None,
                    disable_web_page_preview=False, reply_markup=None):
    """bot.edit(chat_id, message_id, text)"""
    return self.send('editMessageText', chat_id=chat_id, message_id=message_id, inline_message_id=inline_message_id,
                     text=text, parse_mode=parse_mode, entities=entities,
                     disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup)