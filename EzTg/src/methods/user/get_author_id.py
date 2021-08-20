"""Get user id from message"""
def get_author_id(self, message):
    return message['from']['id']