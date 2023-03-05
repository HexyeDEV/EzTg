from .user import User
from .chat import Chat

class Message:
    """Represents a message.
    
    Attributes
    ----------
    message_id: `int`
        Unique message identifier inside this chat.
    message_thread_id: `int`
        Optional. Unique identifier of a message thread to which the message belongs; for supergroups only
    from_user: `User`
        Optional. Sender, empty for messages sent to channels.
    sender_chat: `Chat`
        Optional. Sender of the message, sent on behalf of a chat. The channel itself for channel messages. The supergroup itself for messages from anonymous group administrators. The linked channel for messages automatically forwarded to the discussion group.
    date: `int`
        Date the message was sent in Unix time.
    chat: `Chat`
        Conversation the message belongs to.
    forward_from: `User`
        Optional. For forwarded messages, sender of the original message.
    forward_from_chat: `Chat`
        Optional. For messages forwarded from channels, information about the original channel.
    forward_from_message_id: `int`
        Optional. For messages forwarded from channels, identifier of the original message in the channel.
    forward_signature: `str`
        Optional. For messages forwarded from channels, signature of the post author if present.
    forward_sender_name: `str`
        Optional. For messages forwarded from channels, sender's name for messages forwarded to the discussion group.
    forward_date: `int`
        Optional. For forwarded messages, date the original message was sent in Unix time.
    is_topic_message: `bool`
        Optional. True, if the message is sent to a forum topic
    is_automatic_forward: `bool`
        Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group
    reply_to_message: `Message`
        Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    via_bot: `User`
        Optional. Bot through which the message was sent.
    edit_date: `int`
        Optional. Date the message was last edited in Unix time.
    has_protected_content: `bool`
        Optional. True, if the message can't be forwarded.
    media_group_id: `str`
        Optional. The unique identifier of a media message group this message belongs to.
    author_signature: `str`
        Optional. Signature of the post author for messages in channels.
    text: `str`
        Optional. For text messages, the actual UTF-8 text of the message.
    animation: `Animation`
        Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set.
    audio: `Audio`
        Optional. Message is an audio file, information about the file.
    document: `Document`
        Optional. Message is a general file, information about the file.
    photo: `list[PhotoSize]`
        Optional. Message is a photo, available sizes of the photo.
    sticker: `Sticker`
        Optional. Message is a sticker, information about the sticker.
    video: `Video`
        Optional. Message is a video, information about the video.
    video_note: `VideoNote`
        Optional. Message is a video note, information about the video message.
    voice: `Voice`
        Optional. Message is a voice message, information about the file.
    caption: `str`
        Optional. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters.
    caption_entities: `list[MessageEntity]`
        Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption.
    has_media_spoiler: `bool`
        Optional. True, if the message media is covered by a spoiler animation
    contact: `Contact`
        Optional. Message is a shared contact, information about the contact.
    dice: `Dice`
        Optional. Message is a dice with random value from 1 to 6.
    game: `Game`
        Optional. Message is a game, information about the game.
    poll: `Poll`
        Optional. Message is a native poll, information about the poll.
    venue: `Venue`
        Optional. Message is a venue, information about the venue.
    location: `Location`
        Optional. Message is a shared location, information about the location.
    new_chat_members: `list[User]`
        Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members).
    left_chat_member: `User`
        Optional. A member was removed from the group, information about them (this member may be the bot itself).
    new_chat_title: `str`
        Optional. A chat title was changed to this value.
    new_chat_photo: `list[PhotoSize]`
        Optional. A chat photo was change to this value.
    delete_chat_photo: `bool`
        Optional. Service message: the chat photo was deleted.
    group_chat_created: `bool`
        Optional. Service message: the group has been created.
    supergroup_chat_created: `bool`
        Optional. Service message: the supergroup has been created.
    """

    def __init__(self, data):
        self.message_id = data['message_id']
        self.message_thread_id = data.get('message_thread_id')
        self.from_user = User(data.get('from'))
        self.sender_chat = Chat(data.get('sender_chat'))
        self.date = data['date']
        self.chat = Chat(data['chat'])
        self.forward_from = User(data.get('forward_from'))
        self.forward_from_chat = Chat(data.get('forward_from_chat'))
        self.forward_from_message_id = data.get('forward_from_message_id')
        self.forward_signature = data.get('forward_signature')
        self.forward_sender_name = data.get('forward_sender_name')
        self.forward_date = data.get('forward_date')
        self.is_topic_message = data.get('is_topic_message')
        self.is_automatic_forward = data.get('is_automatic_forward')
        self.reply_to_message = Message(data.get('reply_to_message'))
        self.via_bot = User(data.get('via_bot'))
        self.edit_date = data.get('edit_date')
        self.has_protected_content = data.get('has_protected_content')
        self.media_group_id = data.get('media_group_id')
        self.author_signature = data.get('author_signature')
        self.text = data.get('text')
        self.animation = data.get('animation')
        self.audio = data.get('audio')
        self.document = data.get('document')
        self.photo = data.get('photo')
        self.sticker = data.get('sticker')
        self.video = data.get('video')
        self.video_note = data.get('video_note')
        self.voice = data.get('voice')
        self.caption = data.get('caption')
        self.caption_entities = data.get('caption_entities')
        self.has_media_spoiler = data.get('has_media_spoiler')
        self.contact = data.get('contact')
        self.dice = data.get('dice')
        self.game = data.get('game')
        self.poll = data.get('poll')
        self.venue = data.get('venue')
        self.location = data.get('location')
        self.new_chat_members = data.get('new_chat_members')
        if self.new_chat_members:
            self.new_chat_members = [User(x) for x in self.new_chat_members]
        self.left_chat_member = data.get('left_chat_member')
        if self.left_chat_member:
            self.left_chat_member = User(self.left_chat_member)
        self.new_chat_title = data.get('new_chat_title')