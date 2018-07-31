import pygame
from Shared.GameConstants import GameConstants
from Shared.Animator import Animator


class ARPG:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()

        # pygame.mouse.set_visible(True)

        self.__screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE)
        self.__clock = pygame.time.Clock()
        self.__playtime = 0

        self.__current_scene = 0

    def start(self):
        animator = Animator(GameConstants.SPRITE_SHEET_ADVENTURER,
                            sprite_size=GameConstants.SIZE_ADVENTURER)

        actions_list = animator.get_animations_keys()
        import random
        action = random.choice(actions_list)

        cycletime = 0

        while 1:
            milliseconds = self.__clock.tick(GameConstants.FPS)  # ms passed since last tick/frame
            seconds = milliseconds / 1000.0  # seconds since last tick/frame
            self.__playtime += seconds
            cycletime += seconds
            if cycletime > GameConstants.INTERVAL:
                self.__screen.fill(GameConstants.BLACK)

                image = animator.get_next_sprite(action)
                size = image.get_rect().size
                self.__screen.blit(image,
                                   (GameConstants.SCREEN_SIZE[0]/2 - size[0]/2,
                                    GameConstants.SCREEN_SIZE[1]/2 - size[1]/2))
                cycletime = 0

            pygame.display.set_caption("[FPS]: %.2f action: %s picture: %i" % (self.__clock.get_fps(),
                                                                               action,
                                                                               animator.get_sprite_index()))
            pygame.display.update()
            # pygame.display.flip()

            if animator.get_next_sprite_index() == 0:
                action = random.choice(actions_list)

    def change_scene(self, scene):
        self.__current_scene = scene


try:
    ARPG().start()
except Exception as e:
    print(e)
