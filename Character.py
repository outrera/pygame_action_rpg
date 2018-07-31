import pygame

from Shared.GameConstants import GameConstants
from Shared.GameObject import GameObject
from Shared.Animator import Animator


class Character(GameObject):

    def __init__(self, spritesheet_file, size, position):

        self.__animator = Animator(spritesheet_file, sprite_size=size)
        self.__actions_list = self.__animator.get_animations_keys()
        self.__action = "idle"  # every character must have idle stance!
        image = self.__animator.get_next_sprite(self.__action)
        super(Character, self).__init__(image, position)

        self.__speed = (0, 0)

    def update(self, seconds):
        self.image = self.__animator.get_next_sprite(self.__action)

        if self.__speed[0] < 0:  # move left
            self.__animator.set_flip()
        elif self.__speed[0] > 0:
            self.__animator.unset_flip()

        x = self.rect.x
        y = self.rect.y

        self.set_position((x + self.__speed[0], y + self.__speed[1]))  # update position

        # if self.__speed[0] == 0 and self.__speed[1] == 0:
        #     self.set_action("idle")
        # elif abs(self.__speed[0]) == GameConstants.ADVENTURER_SPEED[0] or abs(self.__speed[1]) == GameConstants.ADVENTURER_SPEED[1]:
        #     self.set_action("run")
        # else:
        #     self.set_action("walk")
        # pass

    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

    def set_action(self, action):
        if action not in self.get_actions_list():
            return
        self.__action = action

    def get_action(self):
        return self.__action

    def get_actions_list(self):
        return self.__animator.get_animations_keys()

    def turn_right(self):
        self.__animator.unset_flip()

    def turn_left(self):
        self.__animator.set_flip()
