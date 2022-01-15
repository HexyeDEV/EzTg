class chat:

    """exportChatInviteLink method"""
    def exportChatInviteLink(app, chat_id):
        return app.send('exportChatInviteLink', chat_id=chat_id)

    """createChatInviteLink method"""
    def createChatInviteLink(app, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=False):
        return app.send('createChatInviteLink', chat_id=chat_id, name=name, expire_date=expire_date, member_limit=member_limit, creates_join_request=creates_join_request)

    """setChatPhoto method"""
    def setChatPhoto(app, chat_id, photo):
        return app.send('setChatPhoto', chat_id=chat_id, photo=photo)

    """pinChatMessage method"""
    def pinChatMessage(app, chat_id, message_id, disable_notification=False):
        return app.send('pinChatMessage', chat_id=chat_id, message_id=message_id, disable_notification=disable_notification)

    """unpinChatMessage method"""
    def unpinChatMessage(app, chat_id, message_id):
        return app.send('unpinChatMessage', chat_id=chat_id, message_id=message_id)

    """leaveChat method"""
    def leaveChat(app, chat_id):
        return app.send('leaveChat', chat_id=chat_id)
