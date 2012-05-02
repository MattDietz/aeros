class AerosContext(object):
    """Represents the screen blitting and dimensional context for interacting
    with pymonk and pygame"""

    def __init__(self, display_size, screen=None, space=None, **kwargs):
        # Size object for the display dimensions
        #TODO: is there value in a full rect later? Or multiple viewports?
        self.display_size = display_size

        # Pygame screen reference
        self.screen = screen
        
        # The pymunk workspace
        self.space = space
        
        if kwargs.get('screen_mode'):
            self.mode = kwargs['screen_mode']
    
    @property
    def display_width(self):
        return self.display_size.x

    @property
    def display_height(self):
        return self.display_size.y

    @property
    def screen_ref(self):
        return self.screen

    @screen_ref.setter
    def screen_ref(self, v):
        self.screen = v

    @property
    def space_ref(self):
        return self.space

    @space_ref.setter
    def space_ref(self, v):
        self.space = v

    @property
    def screen_mode_flags(self):
        return self.mode
