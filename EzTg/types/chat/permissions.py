class ChatPermissions:
    """Describes actions that a non-administrator user is allowed to take in a chat.

    Attributes
    ----------
    can_send_messages: `bool`
        Optional. True, if the user is allowed to send text messages, contacts, locations and venues.
    can_send_audios: `bool`
        Optional. True, if the user is allowed to send audios.
    can_send_documents: `bool`
        Optional. True, if the user is allowed to send documents.
    cabn_send_photos: `bool`
        Optional. True, if the user is allowed to send photos.
    can_send_videos: `bool`
        Optional. True, if the user is allowed to send videos.
    can_send_videos_notes: `bool`
        Optional. True, if the user is allowed to send video notes.
    can_send_voice_notes: `bool`
        Optional. True, if the user is allowed to send voice notes.
    can_send_polls: `bool`
        Optional. True, if the user is allowed to send polls.
    can_send_other_messages: `bool`
        Optional. True, if the user is allowed to send animations, games, stickers and use inline bots.
    can_add_web_page_previews: `bool`
        Optional. True, if the user is allowed to add web page previews to their messages.
    can_change_info: `bool`
        Optional. True, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups.
    can_invite_users: `bool`
        Optional. True, if the user is allowed to invite new users to the chat.
    can_pin_messages: `bool`
        Optional. True, if the user is allowed to pin messages. Ignored in public supergroups.
    can_manage_topics: `bool`
        Optional. True, if the user is allowed to create forum topics. If omitted defaults to the value of can_pin_messages.
    """

    def __init__(self, data):
        self.can_send_messages = data.get("can_send_messages")
        self.can_send_audios = data.get("can_send_audios")
        self.can_send_documents = data.get("can_send_documents")
        self.cabn_send_photos = data.get("cabn_send_photos")
        self.can_send_videos = data.get("can_send_videos")
        self.can_send_videos_notes = data.get("can_send_videos_notes")
        self.can_send_voice_notes = data.get("can_send_voice_notes")
        self.can_send_polls = data.get("can_send_polls")
        self.can_send_other_messages = data.get("can_send_other_messages")
        self.can_add_web_page_previews = data.get("can_add_web_page_previews")
        self.can_change_info = data.get("can_change_info")
        self.can_invite_users = data.get("can_invite_users")
        self.can_pin_messages = data.get("can_pin_messages")
        self.can_manage_topics = data.get("can_manage_topics")
        if self.can_manage_topics is None:
            self.can_manage_topics = self.can_pin_messages
