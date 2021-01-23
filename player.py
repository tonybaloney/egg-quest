import arcade


class MainPlayerSprite(arcade.Sprite):
    def __init__(self, sprite_scaling):
        super().__init__(":resources:images/animated_characters/female_person/femalePerson_idle.png", sprite_scaling)