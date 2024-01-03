from ..chat.chat import Chat
from ..inlinekeyboard import InlineKeyboard
from ..location import Location
from ..user.user import User
from .animation import Animation
from .audio import Audio
from .chat_shared import ChatShared
from .contact import Contact
from .dice import Dice
from .document import Document
from .external_reply_info import ExternalReplyInfo
from .game import Game
from .giveaway import Giveaway
from .invoice import Invoice
from .link_preview_options import LinkPreviewOptions
from .maybe_inaccessible_message import MaybeInaccessibleMessage
from .message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from .message_origin import MessageOrigin
from .messageentity import MessageEntity
from .photosize import PhotoSize
from .poll import Poll
from .sticker import Sticker
from .story import Story
from .successful_payment import SuccessfulPayment
from .text_quote import TextQuote
from .users_shared import UsersShared
from .venue import Venue
from .video import Video
from .videonote import VideoNote
from .voice import Voice
from .write_access_allowed import WriteAccessAllowed


class Message:
    """Represents a message.

    Attributes
    ----------
    message_id: `int`
        Unique message identifier inside this chat.
    message_thread_id: `int`
        Optional. Unique identifier of a message thread to which the message belongs; for supergroups only
    from: `User`
        Optional. Sender, empty for messages sent to channels.
    sender_chat: `Chat`
        Optional. Sender of the message, sent on behalf of a chat. The channel itself for channel messages. The supergroup itself for messages from anonymous group administrators. The linked channel for messages automatically forwarded to the discussion group.
    date: `int`
        Date the message was sent in Unix time.
    chat: `Chat`
        Conversation the message belongs to.
    forward_origin: `MessageOrigin`
        Optional. For forwarded messages, sender of the original message.
    is_topic_message: `bool`
        Optional. True, if message is sent to a forum topic.
    is_automaitc_forward: `bool`
        Optional. True, if the message is a channel post that was automatically forwarded to the connected discussion group.
    reply_to_message: `Message`
        Optional. For replies, the original message. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    external_reply: `ExternalReplyInfo`
        Optional. Information about the message that is being replied to, which may come from another chat or forum topic.
    quote: `TextQuote`
        Optional. For replies that quote part of the original message, the quoted part of the message
    edit_date: `int`
        Optional. Date the message was last edited in Unix time
    media_group_id: `str`
        Optional. The unique identifier of a media message group this message belongs to.
    author_signature: `str`
        Optional. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator.
    text: `str`
        Optional. For text messages, the actual UTF-8 text of the message.
    entities: `Array of MessageEntity`
        Optional. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    link_preview_options: `LinkPreviewOptions`
        Optional. Options used for link preview generation for the message, if it is a text message and link preview options were changed.
    animation: `Animation`
        Optional. Message is an animation, information about the animation. For backward compatibility, when this field is set, the document field will also be set.
    audio: `Audio`
        Optional. Message is an audio file, information about the file.
    document: `Document`
        Optional. Message is a general file, information about the file.
    photo: `Array of PhotoSize`
        Optional. Message is a photo, available sizes of the photo.
    sticker: `Sticker`
        Optional. Message is a sticker, information about the sticker.
    story: `Story`
        Optional. Message is a forwarded story.
    video: `Video`
        Optional. Message is a video, information about the video.
    video_note: `VideoNote`
        Optional. Message is a video note, information about the video message.
    voice: `Voice`
        Optional. Message is a voice message, information about the file.
    caption: `str`
        Optional. Caption for the animation, audio, document, photo, video or voice
    caption_entities: `Array of MessageEntity`
        Optional. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption.
    has_media_spoiler: `bool`
        Optional. True, if the message media is covered by a spoiler animation.
    contact: `Contact`
        Optional. Message is a shared contact, information about the contact.
    dice: `Dice`
        Optional. Message is a dice with random value.
    game: `Game`
        Optional. Message is a game, information about the game.
    poll: `Poll`
        Optional. Message is a native poll, information about the poll.
    venue: `Venue`
        Optional. Message is a venue, information about the venue. For backward compatibility, when this field is set, the location field will also be set
    location: `Location`
        Optional. Message is a shared location, information about the location.
    new_chat_members: `Array of User`
        Optional. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members).
    left_chat_member: `User`
        Optional. A member was removed from the group, information about them (this member may be the bot itself).
    new_chat_title: `str`
        Optional. A chat title was changed to this value.
    new_chat_photo: `Array of PhotoSize`
        Optional. A chat photo was change to this value.
    delete_chat_photo: `bool`
        Optional. Service message: the chat photo was deleted.
    group_chat_created: `bool`
        Optional. Service message: the group has been created.
    supergroup_chat_created: `bool`
        Optional. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply_to_message if someone replies to a very first message in a directly created supergroup.
    channel_chat_created: `bool`
        Optional. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply_to_message if someone replies to a very first message in a channel.
    message_auto_delete_timer_changed: `MessageAutoDeleteTimerChanged`
        Optional. Service message: auto-delete timer settings changed in the chat.
    migrate_to_chat_id: `int`
        Optional. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    migrate_from_chat_id: `int`
        Optional. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    pinned_message: `MaybeInaccessibleMessage`
        Optional. Specified message was pinned. Note that the Message object in this field will not contain further reply_to_message fields even if it itself is a reply.
    invoice: `Invoice`
        Optional. Message is an invoice for a payment, information about the invoice. For backward compatibility, when this field is set, the document field will also be set.
    successful_payment: `SuccessfulPayment`
        Optional. Message is a service message about a successful payment, information about the payment. For backward compatibility, when this field is set, the invoice field will also be set.
    users_shared `UsersShared`
        Optional. Service message: users were shared with the bot.
    chat_shared `ChatShared`
        Optional. Service message: a chat was shared with the bot.
    connected_website `str`
        Optional. The domain name of the website on which the user has logged in.
    write_access_allowed `WriteAccessAllowed`
        Optional. Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess
    passport_data `PassportData`
        Optional. Telegram Passport data
    proximity_alert_triggered `ProximityAlertTriggered`
        Optional. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    forum_topic_created: `ForumTopicCreated`
        Optional. Service message: forum topic created.
    forum_topic_edited: `ForumTopicEdited`
        Optional. Service message: forum topic edited.
    forum_topic_closed: `ForumTopicClosed`
        Optional. Service message: forum topic closed.
    forum_topic_reopened: `ForumTopicReopened`
        Optional. Service message: forum topic reopened.
    general_forum_topic_hidden `GeneralForumTopicHidden`
        Optional. Service message: the 'General' forum topic hidden.
    general_forum_topic_unhidden `GeneralForumTopicUnhidden`
        Optional. Service message: the 'General' forum topic unhidden.
    giveaway_created: `GiveawayCreated`
        Optional. Service message: a scheduled giveaway was created.
    giveaway: `Giveaway`
        Optional. The message is a scheduled giveaway message.
    giveaway_winners: `GiveawayWinners`
        Optional. A giveaway with public winners was completed.
    giveaway_completed: `GiveawayCompleted`
        Optional. Service message: a giveaway without public winners was completed.
    video_chat_scheduled: `VideoChatScheduled`
        Optional. Service message: video chat scheduled.
    video_chat_started: `VideoChatStarted`
        Optional. Service message: video chat started.
    video_chat_ended: `VideoChatEnded`
        Optional. Service message: video chat ended.
    video_chat_participants_invited: `VideoChatParticipantsInvited`
        Optional. Service message: new participants invited to a video chat.
    web_app_data: `WebAppData`
        Optional. Service message: data sent by a Web App.
    reply_markup: `InlineKeyboard`
        Optional. Inline keyboard attached to the message. login_url buttons are represented as ordinary url buttons.
    """

    def __init__(self, data):
        self.message_id = data["message_id"]
        self.message_thread_id = data.get("message_thread_id")
        self.from_ = data.get("from")
        if self.from_:
            self.from_ = User(self.from_)
        self.sender_chat = data.get("sender_chat")
        if self.sender_chat:
            self.sender_chat = Chat(self.sender_chat)
        self.date = data["date"]
        self.chat = Chat(data["chat"])
        self.forward_origin = data.get("forward_origin")
        if self.forward_origin:
            self.forward_origin = MessageOrigin(self.forward_origin)
        self.is_topic_message = data.get("is_topic_message")
        self.is_automaitc_forward = data.get("is_automaitc_forward")
        self.reply_to_message = data.get("reply_to_message")
        if self.reply_to_message:
            self.reply_to_message = Message(self.reply_to_message)
        self.external_reply = data.get("external_reply")
        if self.external_reply:
            self.external_reply = ExternalReplyInfo(self.external_reply)
        self.quote = data.get("quote")
        if self.quote:
            self.quote = TextQuote(self.quote)
        self.edit_date = data.get("edit_date")
        self.media_group_id = data.get("media_group_id")
        self.author_signature = data.get("author_signature")
        self.text = data.get("text")
        self.entities = data.get("entities")
        if self.entities:
            self.entities = [MessageEntity(i) for i in self.entities]
        self.link_preview_options = data.get("link_preview_options")
        if self.link_preview_options:
            self.link_preview_options = LinkPreviewOptions(
                self.link_preview_options)
        self.animation = data.get("animation")
        if self.animation:
            self.animation = Animation(self.animation)
        self.audio = data.get("audio")
        if self.audio:
            self.audio = Audio(self.audio)
        self.document = data.get("document")
        if self.document:
            self.document = Document(self.document)
        self.photo = data.get("photo")
        if self.photo:
            self.photo = [PhotoSize(i) for i in self.photo]
        self.sticker = data.get("sticker")
        if self.sticker:
            self.sticker = Sticker(self.sticker)
        self.story = data.get("story")
        if self.story:
            self.story = Story(self.story)
        self.video = data.get("video")
        if self.video:
            self.video = Video(self.video)
        self.video_note = data.get("video_note")
        if self.video_note:
            self.video_note = VideoNote(self.video_note)
        self.voice = data.get("voice")
        if self.voice:
            self.voice = Voice(self.voice)
        self.caption = data.get("caption")
        self.caption_entities = data.get("caption_entities")
        if self.caption_entities:
            self.caption_entities = [
                MessageEntity(i) for i in self.caption_entities]
        self.has_media_spoiler = data.get("has_media_spoiler")
        self.contact = data.get("contact")
        if self.contact:
            self.contact = Contact(self.contact)
        self.dice = data.get("dice")
        if self.dice:
            self.dice = Dice(self.dice)
        self.game = data.get("game")
        if self.game:
            self.game = Game(self.game)
        self.poll = data.get("poll")
        if self.poll:
            self.poll = Poll(self.poll)
        self.venue = data.get("venue")
        if self.venue:
            self.venue = Venue(self.venue)
        self.location = data.get("location")
        if self.location:
            self.location = Location(self.location)
        self.new_chat_members = data.get("new_chat_members")
        if self.new_chat_members:
            self.new_chat_members = [User(i) for i in self.new_chat_members]
        self.left_chat_member = data.get("left_chat_member")
        if self.left_chat_member:
            self.left_chat_member = User(self.left_chat_member)
        self.new_chat_title = data.get("new_chat_title")
        self.new_chat_photo = data.get("new_chat_photo")
        if self.new_chat_photo:
            self.new_chat_photo = [PhotoSize(i) for i in self.new_chat_photo]
        self.delete_chat_photo = data.get("delete_chat_photo")
        self.group_chat_created = data.get("group_chat_created")
        self.supergroup_chat_created = data.get("supergroup_chat_created")
        self.channel_chat_created = data.get("channel_chat_created")
        self.message_auto_delete_timer_changed = data.get("message_auto_delete_timer_changed")
        if self.message_auto_delete_timer_changed:
            self.message_auto_delete_timer_changed = MessageAutoDeleteTimerChanged(self.message_auto_delete_timer_changed)
        self.migrate_to_chat_id = data.get("migrate_to_chat_id")
        self.migrate_from_chat_id = data.get("migrate_from_chat_id")
        self.pinned_message = data.get("pinned_message")
        if self.pinned_message:
            self.pinned_message = MaybeInaccessibleMessage(self.pinned_message)
        self.invoice = data.get("invoice")
        if self.invoice:
            self.invoice = Invoice(self.invoice)
        self.successful_payment = data.get("successful_payment")
        if self.successful_payment:
            self.successful_payment = SuccessfulPayment(self.successful_payment)
        self.users_shared = data.get("users_shared")
        if self.users_shared:
            self.users_shared = UsersShared(self.users_shared)
        self.chat_shared = data.get("chat_shared")
        if self.chat_shared:
            self.chat_shared = ChatShared(self.chat_shared)
        self.connected_website = data.get("connected_website")
        self.write_access_allowed = data.get("write_access_allowed")
        if self.write_access_allowed:
            self.write_access_allowed = WriteAccessAllowed(self.write_access_allowed)
        self.passport_data = data.get("passport_data")
        if self.passport_data:
            self.passport_data = PassportData(self.passport_data)
        self.proximity_alert_triggered = data.get("proximity_alert_triggered")
        if self.proximity_alert_triggered:
            self.proximity_alert_triggered = ProximityAlertTriggered(self.proximity_alert_triggered)
        self.forum_topic_created = data.get("forum_topic_created")
        if self.forum_topic_created:
            self.forum_topic_created = ForumTopicCreated(self.forum_topic_created)
        self.forum_topic_edited = data.get("forum_topic_edited")
        if self.forum_topic_edited:
            self.forum_topic_edited = ForumTopicEdited(self.forum_topic_edited)
        self.forum_topic_closed = data.get("forum_topic_closed")
        if self.forum_topic_closed:
            self.forum_topic_closed = ForumTopicClosed(self.forum_topic_closed)
        self.forum_topic_reopened = data.get("forum_topic_reopened")
        if self.forum_topic_reopened:
            self.forum_topic_reopened = ForumTopicReopened(self.forum_topic_reopened)
        self.general_forum_topic_hidden = data.get("general_forum_topic_hidden")
        if self.general_forum_topic_hidden:
            self.general_forum_topic_hidden = GeneralForumTopicHidden(self.general_forum_topic_hidden)
        self.general_forum_topic_unhidden = data.get("general_forum_topic_unhidden")
        if self.general_forum_topic_unhidden:
            self.general_forum_topic_unhidden = GeneralForumTopicUnhidden(self.general_forum_topic_unhidden)
        self.giveaway_created = data.get("giveaway_created")
        if self.giveaway_created:
            self.giveaway_created = GiveawayCreated(self.giveaway_created)
        self.giveaway = data.get("giveaway")
        if self.giveaway:
            self.giveaway = Giveaway(self.giveaway)
        self.giveaway_winners = data.get("giveaway_winners")
        if self.giveaway_winners:
            self.giveaway_winners = GiveawayWinners(self.giveaway_winners)
        self.giveaway_completed = data.get("giveaway_completed")
        if self.giveaway_completed:
            self.giveaway_completed = GiveawayCompleted(self.giveaway_completed)
        self.video_chat_scheduled = data.get("video_chat_scheduled")
        if self.video_chat_scheduled:
            self.video_chat_scheduled = VideoChatScheduled(self.video_chat_scheduled)
        self.video_chat_started = data.get("video_chat_started")
        if self.video_chat_started:
            self.video_chat_started = VideoChatStarted(self.video_chat_started)
        self.video_chat_ended = data.get("video_chat_ended")
        if self.video_chat_ended:
            self.video_chat_ended = VideoChatEnded(self.video_chat_ended)
        self.video_chat_participants_invited = data.get("video_chat_participants_invited")
        if self.video_chat_participants_invited:
            self.video_chat_participants_invited = VideoChatParticipantsInvited(self.video_chat_participants_invited)
        self.web_app_data = data.get("web_app_data")
        if self.web_app_data:
            self.web_app_data = WebAppData(self.web_app_data)
        self.reply_markup = data.get("reply_markup")
        if self.reply_markup:
            self.reply_markup = InlineKeyboard(self.reply_markup)