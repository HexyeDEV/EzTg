"""deleteMessage method"""
def deleteMessage(self, chat_id, message_id):
    """bot.deleteMessage(chat_id, message_id)"""
    return self.send('deleteMessage', chat_id=chat_id, message_id=message_id)