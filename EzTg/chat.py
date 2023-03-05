class Chat:
    """Represents a telegram chat.

    Attributes
    ----------
    id: `int`
        Unique identifier for this chat.
    type: `str`
        Type of chat, can be either `private`, `group`, `supergroup` or `channel`.
    title: `str`
        Optional. Title, for supergroups, channels and group chats.
    username: `str`
        Optional. Username, for private chats, supergroups and channels if available.
    first_name: `str`
        Optional. First name of the other party in a private chat.
    last_name: `str`
        Optional. Last name of the other party in a private chat.
    is_forum: `bool`
        Optional. True, if the supergroup chat is a forum.
    photo: `ChatPhoto`
        Optional. Chat photo. Returned only in getChat.
    active_usernames: `list`
        Optional. Active usernames in the chat. Returned only in getChat.
    emoji_status_custom_emoji_id: `str`
        Optional. Emoji status custom emoji id. Returned only in getChat.
    bio: `str`
        Optional. Bio of the chat. Returned only in getChat.
    has_private_forwards: `bool`
        Optional. True, if privacy settings of the other party in the private chat allows to use tg://user?id=<user_id> links only in chats with the user. Returned only in getChat.
    has_restricted_voice_and_video_messages: `bool`
        Optional. True, if the privacy settings of the other party restrict sending voice and video note messages in the private chat. Returned only in getChat.
    join_to_send_messages: `bool`
        Optional. True, if users need to join the supergroup before they can send messages. Returned only in getChat.
    join_by_request: `bool`
        Optional. True, if all users directly joining the supergroup need to be approved by supergroup administrators. Returned only in getChat.
    description: `str`
        Optional. Description, for groups, supergroups and channel chats. Returned only in getChat.
    invite_link: `str`
        Optional. Primary invite link, for groups, supergroups and channel chats. Returned only in getChat.
    pinned_message: `Message`
        Optional. The most recent pinned message (by sending date). Returned only in getChat.
    permissions: `ChatPermissions`
        Optional. Default chat member permissions, for groups and supergroups. Returned only in getChat.
    slow_mode_delay: `int`
        Optional. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in getChat.
    message_auto_delete_time: `int`
        Optional. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in getChat.
    has_aggressive_anti_spam_enabled: `bool`
        Optional. True, if aggressive anti-spam checks are enabled in the supergroup. The field is only available to chat administrators. Returned only in getChat.
    has_hidden_members: `bool`
        Optional. True, if non-administrators can only get the list of bots and administrators in the chat. Returned only in getChat.
    has_protected_content: `bool`
        Optional. True, if messages from the chat can't be forwarded to other chats. Returned only in getChat.
    sticket_set_name: `str`
        Optional. For supergroups, name of group sticker set. Returned only in getChat.
    can_set_sticker_set: `bool`
        Optional. True, if the bot can change the group sticker set. Returned only in getChat.
    linked_chat_id: `int`
        Optional. Unique identifier for the linked chat. Returned only in getChat.
    location: `ChatLocation`
        Optional. For supergroups, the location to which the supergroup is connected. Returned only in getChat."""

    def __init__(self, data: dict):
        self.id = data["id"]
        self.type = data["type"]
        self.title = data.get("title")
        self.username = data.get("username")
        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.is_forum = data.get("is_forum")
        self.photo = data.get("photo")
        self.active_usernames = data.get("active_usernames")
        self.emoji_status_custom_emoji_id = data.get(
            "emoji_status_custom_emoji_id")
        self.bio = data.get("bio")
        self.has_private_forwards = data.get("has_private_forwards")
        self.has_restricted_voice_and_video_messages = data.get(
            "has_restricted_voice_and_video_messages")
        self.join_to_send_messages = data.get("join_to_send_messages")
        self.join_by_request = data.get("join_by_request")
        self.description = data.get("description")
        self.invite_link = data.get("invite_link")
        self.pinned_message = data.get("pinned_message")
        self.permissions = data.get("permissions")
        self.slow_mode_delay = data.get("slow_mode_delay")
        self.message_auto_delete_time = data.get("message_auto_delete_time")
        self.has_aggressive_anti_spam_enabled = data.get(
            "has_aggressive_anti_spam_enabled")
        self.has_hidden_members = data.get("has_hidden_members")
        self.has_protected_content = data.get("has_protected_content")
        self.sticket_set_name = data.get("sticket_set_name")
        self.can_set_sticker_set = data.get("can_set_sticker_set")
        self.linked_chat_id = data.get("linked_chat_id")
        self.location = data.get("location")
