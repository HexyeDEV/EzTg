from ..chat import Chat
from .animation import Animation
from .audio import Audio
from .document import Document
from .link_preview_options import LinkPreviewOptions
from ..location import Location
from .photosize import PhotoSize
from .sticker import Sticker
from .video import Video
from .videonote import VideoNote
from .voice import Voice
from .contact import Contact
from .dice import Dice
from .game import Game
from .giveaway import Giveaway
from .invoice import Invoice
from .message_origin import MessageOrigin
from .poll import Poll
from .story import Story
from .venue import Venue

class ExternalReplyInfo:
    """This object contains information about a message that is being replied to, which may come from another chat or forum topic.
    
    Attributes:
    -----------
    origin: `MessageOrigin`
        Origin of the message replied to by the given message.
    chat: `Chat`
        Optional. Chat the original message belongs to. Available only if the chat is a supergroup or a channel.
    message_id: `int`
        Optional. Unique message identifier inside the original chat. Available only if the original chat is a supergroup or a channel.
    link_preview_options: `LinkPreviewOptions`
        Optional. Options used for link preview generation for the original message, if it is a text message.
    animation: `Animation`
        Optional. Message is an animation, information about the animation.
    audio: `Audio`
        Optional. Message is an audio file, information about the file
    document: `Document`
        Optional. Message is a general file, information about the file
    photo: `array of PhotoSize`
        Optional. Message is a photo, available sizes of the photo.
    sticker: `Sticker`
        Optional. Message is a sticker, information about the sticker.
    story: `Story`
        Optional. Message is a forwarded story
    video: `Video`
        Optional. Message is a video, information about the video.
    video_note: `VideoNote`
        Optional. Message is a video note, information about the video message.
    voice: `Voice`
        Optional. Message is a voice message, information about the file.
    has_media_spoiler: `bool`
        Optional. True, if the message media is covered by a spoiler animation.
    contact: `Contact`
        Optional. Message is a shared contact, information about the contact.
    dice: `Dice`
        Optional. Message is a dice with random value from 1 to 6.
    game: `Game`
        Optional. Message is a game, information about the game.
    giveaway: `Giveaway`
        Optional. Message is a scheduled giveaway, information about the giveaway.
    giveaway_winners: `GiveawayWinners`
        Optional. A giveaway with public winners was completed.
    invoice: `Invoice`
        Optional. Message is an invoice for a payment, information about the invoice.
    location: `Location`
        Optional. Message is a shared location, information about the location
    poll: `Poll`
        Optional. Message is a native poll, information about the poll.
    venue: `Venue`
        Optional. Message is a venue, information about the venue."""
    
    def __init__(self, data):
        self.origin = MessageOrigin(data["origin"])
        self.chat = data.get("chat")
        if self.chat:
            self.chat = Chat(self.chat)
        self.message_id = data.get("message_id")
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
            self.photo = [PhotoSize(photo) for photo in self.photo]
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
        self.giveaway = data.get("giveaway")
        if self.giveaway:
            self.giveaway = Giveaway(self.giveaway)
        self.giveaway_winners = data.get("giveaway_winners")
        if self.giveaway_winners:
            self.giveaway_winners = GiveawayWinners(self.giveaway_winners)
        self.invoice = data.get("invoice")
        if self.invoice:
            self.invoice = Invoice(self.invoice)
        self.location = data.get("location")
        if self.location:
            self.location = Location(self.location)
        self.poll = data.get("poll")
        if self.poll:
            self.poll = Poll(self.poll)
        self.venue = data.get("venue")
        if self.venue:
            self.venue = Venue(self.venue)