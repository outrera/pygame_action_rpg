from Shared.GameObject import GameObject
from Shared.Animator import Animator


class Character(GameObject):

    def __init__(self, spritesheet_file, size, position):

        self.__animator = Animator(spritesheet_file, sprite_size=size)
        self.__actions_list = self.__animator.get_animations_keys()
        self.__action = "idle"  # every character must have idle stance!
        image = self.__animator.get_next_sprite(self.__action)
        super(Character, self).__init__(image, position)

    def update(self, seconds):
        self.image = self.__animator.get_next_sprite(self.__action)
        pass

    def set_action(self, action):
        if action not in self.get_actions_list():
            return
        self.__action = action

    def get_actions_list(self):
        return self.__animator.get_animations_keys()