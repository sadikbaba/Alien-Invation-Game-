class settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialize the game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 70, 70, 70
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed_factor = 1

        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
