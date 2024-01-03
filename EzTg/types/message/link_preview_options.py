class LinkPreviewOptions:
    """Describes the options used for link preview generation.
    
    Attributes:
    -----------
    is_disabled: `bool`
        Optional. True, if the link preview is disabled.
    url: `str`
        Optional. URL to use for the link preview. If empty, then the first URL found in the message text will be used.
    prefer_small_media: `bool`
        Optional. True, if the media in the link preview is suppposed to be shrunk; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.
    prefer_large_media: `bool`
        Optional. True, if the media in the link preview is suppposed to be enlarged; ignored if the URL isn't explicitly specified or media size change isn't supported for the preview.
    show_above_text: `bool`
        Optional. True, if the link preview must be shown above the message text; otherwise, the link preview will be shown below the message text."""
    
    def __init__(self, data):
        self.is_disabled = data.get("is_disabled")
        self.url = data.get("url")
        self.prefer_small_media = data.get("prefer_small_media")
        self.prefer_large_media = data.get("prefer_large_media")
        self.show_above_text = data.get("show_above_text")