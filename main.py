import pygame

from Character import Character
from Shared.GameConstants import GameConstants
# from Shared.Animator import Animator


class ARPG:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()

        # pygame.mouse.set_visible(True)

        self.__screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE)
        self.__clock = pygame.time.Clock()
        self.__playtime = 0
        self.__current_scene = 0
        self.__mainloop = True
        self.__background = pygame.Surface(GameConstants.SCREEN_SIZE).convert_alpha()
        self.__background.fill(GameConstants.BLACK)
        self.__allgroup = pygame.sprite.LayeredUpdates()  # ordered sprite group

    def start(self):
        # animator = Animator(GameConstants.SPRITE_SHEET_ADVENTURER,
        #                     sprite_size=GameConstants.SIZE_ADVENTURER)

        sprite_sheet = GameConstants.SPRITE_SHEET_ADVENTURER
        size = GameConstants.SIZE_ADVENTURER
        position = (GameConstants.SCREEN_SIZE[0]/2-size[0]/2, GameConstants.SCREEN_SIZE[1]/2-size[1]/2)

        hero = Character(sprite_sheet, size, position)
        self.__allgroup.add(hero)
        actions_list = hero.get_actions_list()
        import random
        action = random.choice(actions_list)

        cycletime = 0

        while self.__mainloop:
            milliseconds = self.__clock.tick(GameConstants.FPS)  # ms passed since last tick/frame
            seconds = milliseconds / 1000.0  # seconds since last tick/frame
            self.__playtime += seconds
            cycletime += seconds

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__mainloop = False

            if cycletime > GameConstants.INTERVAL:
                cycletime = 0
                self.__allgroup.clear(self.__screen, self.__background)
                self.__allgroup.update(seconds)
                self.__allgroup.draw(self.__screen)

            pygame.display.set_caption("[FPS]: %.2f action: %s" % (self.__clock.get_fps(), action))
            # pygame.display.set_caption("[FPS]: %.2f action: %s picture: %i" % (self.__clock.get_fps(),
            #                                                                    action,
            #                                                                    hero.get_sprite_index()))

            pygame.display.update()
            # pygame.display.flip()

    def change_scene(self, scene):
        self.__current_scene = scene


ARPG().start()
