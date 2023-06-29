class MaskPosition:
    """Represents a point on the mask position of a sticker sent by the bot.
    
    Attributes
    ----------
    point: `str`
        The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
    x_shift: `float`
        Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    y_shift: `float`
        Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    scale: `float`
        Mask scaling coefficient. For example, 2.0 means double size.
    """

    def __init__(self, data):
        self.point = data["point"]
        self.x_shift = data["x_shift"]
        self.y_shift = data["y_shift"]
        self.scale = data["scale"]