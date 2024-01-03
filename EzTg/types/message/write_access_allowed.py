class WriteAccessAllowed:
    """This object represents a service message about a user allowing a bot to write messages after adding it to the attachment menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method requestWriteAccess.
    
    Attributes:
    -----------
    from_request: `bool`
        Optional. True, if the access was granted after the user accepted an explicit request from a Web App sent by the method requestWriteAccess.
    web_app_name: `str`
        Optional. Name of the Web App, if the access was granted when the Web App was launched from a link.
    from_attachment_menu: `bool`
        Optional. True, if the access was granted when the bot was added to the attachment or side menu.
    """

    def __init__(self, data):
        self.from_request = data.get("from_request")
        self.web_app_name = data.get("web_app_name")
        self.from_attachment_menu = data.get("from_attachment_menu")